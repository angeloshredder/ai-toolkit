import os

TOOLKIT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_ROOT = os.path.join(TOOLKIT_ROOT, 'config')
SD_SCRIPTS_ROOT = os.path.join(TOOLKIT_ROOT, "repositories", "sd-scripts")
REPOS_ROOT = os.path.join(TOOLKIT_ROOT, "repositories")

# check if ENV variable is set
if 'MODELS_PATH' in os.environ:
    MODELS_PATH = os.environ['MODELS_PATH']
else:
    MODELS_PATH = os.path.join(TOOLKIT_ROOT, "models")


def get_path(path):
    # we allow absolute paths, but if it is not absolute, we assume it is relative to the toolkit root
    if not os.path.isabs(path):
        path = os.path.join(TOOLKIT_ROOT, path)
    return path
