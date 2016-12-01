from setuptools import setup
from subprocess import check_output
import re


def get_version():
    """Interrogate git to find our version string.

    We require tags of the form v1.y.z

    Development builds should happen on named branches (pref. `master`).
    When crafting a release, start a new branch named 1.y

    """
    tag = check_output(['git', 'describe', '--tags', '--long']).decode()
    ma = re.match(r'v(\d+)\.(\d+)\.(\d+)\-(\d+)\-(\w+)', tag)
    if ma is None:
        print("The git tag {} does not match the format of v1.y.z-n-abcdef1")
        exit(1)
    major, minor, patch, dirty, hash = ma.groups()
    branch = check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode()
    ma = re.match(r'(\d)+\.(\d+)', branch)
    if ma is not None:
        branch_major, branch_minor = ma.groups()
        branch_patch = int(patch) + 1
    else:
        branch_major = major
        branch_minor = int(minor) + 1
        branch_patch = 0
        dirty = 1
    version = "{major}.{minor}.{patch}".format(major=branch_major, minor=branch_minor, patch=branch_patch)
    if int(dirty) > 0:
        version = "{version}.dev{dirty}".format(version=version, dirty=dirty)
    return version


version = get_version()
print("Version:", version)

setup(
    name='sphinx_modern_theme',
    version=version,
    url='http://github.com/mpharrigan/sphinx-modern-theme',
    license='MIT',
    author='Matthew Harrigan',
    author_email='matthew.harrigan@outlook.com',
    description='A modern sphinx theme using Bootstrap',
    zip_safe=False,
    packages=['sphinx_modern_theme'],
    package_data={
        'sphinx_modern_theme': [
            'theme.conf',
            '*.html',
            'static/*.css',
            'static/*.js',
        ]
    },
)
