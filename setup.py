from setuptools import setup

setup(
    name='sphinx_modern_theme',
    version="1.0.0",
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

