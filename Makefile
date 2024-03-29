
.PHONY: clean lint dev test preflight, docs, publish_docs, pypi, build, docs

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
BUCKET = [OPTIONAL] your-bucket-for-syncing-data (do not include 's3://')
PROFILE = default
PROJECT_NAME = hushh-vibe-catalog-reader
PYTHON_INTERPRETER = python3

ifeq (,$(shell which conda))
HAS_CONDA=False
else
HAS_CONDA=True
endif

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Set up direnv/Python environment
environment :
	brew install swift
	brew install direnv
	brew install miniforge
	conda env create -f environment.yml
	eval "$(conda shell.zsh hook)" # load conda env
	direnv reload

# Clean environment by rebuilding it completely
clean_environment : | clean
	conda env create -f environment.yml --force

## Install Python dev dependencies
dev :
	$(PYTHON_INTERPRETER) -m pip install -e ".[dev]"

## Delete all compiled Python files
clean:
	find . -type d -name "__pycache__" -delete
	find . -path "*hushh/hcf" -type d -exec rm -rf {} +

docs: readme
	quartodoc build
	git-changelog --provider github > changelog.md
	doq -r -d src/hushh/hcf/ -w --formatter numpy
	quarto render

readme:
	quarto render README.qmd

build:
	python -m build

preflight: test, build
	pip-compile
	conda env export > environment.yml
	twine check dist/*
	docs

test:
	pytest --cov=python/src python/test

publish_docs: docs
	quarto publish

## Lint using flake8
lint:
	black src
	flake8 src

## Generate flatbuffer stubs
flatbuffers:
	flatc --python -o python/src schemas/hushh-catalog.fbs --gen-object-api --gen-json-emit --python-typing
	flatc --swift -o swift/Sources schemas/hushh-catalog.fbs --gen-object-api --gen-json-emit
	flatc --dart -o dart/lib schemas/hushh-catalog.fbs --gen-object-api --gen-json-emit
	# check this file out since flatbuffers will overwrite it.
	git checkout python/src/hushh/__init__.py


#################################################################################
# PROJECT RULES                                                                 #
#################################################################################



#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: help
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
