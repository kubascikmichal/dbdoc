# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'DogDetection'
copyright = '2023, Michal Kubaščík'
author = 'Michal Kubaščík'
release = '0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [ 'sphinxcontrib.email' ]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    'navigation_depth': 4,
}
html_static_path = ['_static']


import datetime

current_year = datetime.datetime.now().year
project = u'DogDetection'
copyright = u'2023 - {}, Michal Kubaščík'.format(current_year)

email_automode = True