Documentation Structure
=======================

Sphinx Modern Theme assumes a particular organization of your documentation. At the top level of the
heirarchy, there should be a number of categories. Each page should belong to a category. By convention,
you should make a subfolder for each category. For example, this project's documentation has "User Documentation"
and "Developer Documentation". Therefore, our ``docs/`` directory looks like this::

    docs/
        User/
            index.rst
            page1.rst
        Developer/
            index.rst
            page1.rst
            page2.rst

        conf.py
        Makefile
        index.rst

No pages should be in the top level of your folder structure. Each page must belong to a category.


Top-level index page
--------------------

The top-level ``index.rst`` index file should greet the user, and may serve as a homepage for the documentation.
It should include a toctree directive that lists the categories' index files::

    My fancy project
    ================

    Welcome to the project! Some other nonesense here.

    Contents:

    .. toctree::
    :hidden:

    User/index
    Developer/index


Category index pages
--------------------

Each category shouldn't actually have any prose associated with it. Rather, everything should be in a page (which
belongs to a category). The ``index.rst`` file shouldn't ever be seen for each category. Rather, we immediately
re-direct to the first page in the category. It's like having a heading immediately followed by a sub-heading.
The code should look like this::


    .. raw:: html

    <meta http-equiv="refresh" content=1; page1.html>
        <script type="text/javascript">
            window.location.href = "page1.html"
        </script>

    Category Name
    =============

    .. toctree::

        page1
        page2


.. important::

    Change the redirect target to the first subpage (with html extension)


