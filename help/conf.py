# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from datetime import datetime
import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'MapsPrinter'
copyright = '2013-{}, DelazJ'.format( datetime.now().year )
author = 'Harrissou Sant-anna'


# -- General configuration ---------------------------------------------------

# The master toctree document.
master_doc = 'help'

#The file extensions of source files. Sphinx considers the files with this suffix as sources.
#The value can be a dictionary mapping file extensions to file types. For example:
source_suffix = {
    '.txt': 'restructuredtext',
}

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '../icons/icon.png'

# If given, this must be the name of an image file (path relative to this directory)
#that is the favicon of the docs. Modern browsers use this as the icon for tabs, windows and bookmarks.
#It should be a Windows-style icon file (.ico), which is 16x16 or 32x32 pixels large. Default: None
html_favicon = '../icons/icon.ico'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx_rtd_theme']

# Add any paths that contain templates here, relative to this directory.
# templates_path = []

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Internationalisation ----------------------------------------------------

locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme' # 'classic'

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['./themes']


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['./images']
