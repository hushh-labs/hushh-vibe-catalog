import pkg_resources
import subprocess
try:
    VERSION = str(subprocess.check_output(["git", "describe"]).strip())
except ValueError:
    VERSION = pkg_resources.get_distribution('hushh-vibe-catalog-reader').version
