from setuptools import setup
from subprocess import check_output
import re

tag = check_output(['git', 'describe', '--tags', '--long']).decode()
ma = re.match(r'v(\d+)\.(\d+)\.(\d+)\-(\d+)\-(\w+)', tag)
if ma is None:
    print("The git tag {} does not match the format of v1.y.z-n-abcdef1")
    exit(1)
major, minor, patch, dirty, hash = ma.groups()
if int(dirty) > 0:
    version = "{major}.{minor}.{patch}.dev{dirty}".format(major=major, minor=minor, patch=patch, dirty=dirty)
else:
    version = "{major}.{minor}.{patch}".format(major=major, minor=minor, patch=patch)
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
