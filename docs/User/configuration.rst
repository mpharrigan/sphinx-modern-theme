Configuration
=============

Insert the following into your ``conf.py`` configuration file to enable the theme::


    import sphinx_modern_theme
    html_theme = 'sphinx_modern_theme'
    pygments_style = 'default'
    html_theme_path = [
        sphinx_modern_theme.get_html_theme_path(),
    ]
    html_logo = '_static/logo.png'

.. note:: ``html_theme`` will probably already be set to something. Make sure you only set it once.

.. note:: ``pygments_style = 'default'`` is *not* the default

.. note:: A logo is required


Theme Options
-------------

You can pass options to the theme as a dictionary::


    html_theme_options = {
        'versions_url': '/_static/versions.json'
    }

versions_url
    It is common to support multiple versions of your software (and host multiple versions of the documentation).
    If this configuration option is specified, the file specified by the url will be loaded and used to populate
    a drop-down menu to allow switching between versions. See :ref:`versions` for more.
