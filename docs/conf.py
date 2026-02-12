import sphinx_rtd_theme  # noqa: F401
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'oc_lettings_site.settings'


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'oc_lettings_site'
copyright = '2026, faaab84'
author = 'faaab84'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_autodoc_typehints',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['../_static']

autoclass_content = 'both'

extensions += ['sphinx.ext.autodoc', 'sphinx.ext.autosummary']
autosummary_generate = True

autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__str__',
    'undoc-members': False,
}

# Améliore la lisibilité
autodoc_typehints = 'description'
add_module_names = False
