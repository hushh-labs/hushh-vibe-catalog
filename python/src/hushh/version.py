from importlib.metadata import version, packages_distributions
import subprocess
try:
    VERSION = str(subprocess.check_output(["git", "describe"]).strip())
except ValueError:
    base_module = __name__.split(".")[0]
    package = packages_distributions()[base_module][0]
    VERSION = version(package)
