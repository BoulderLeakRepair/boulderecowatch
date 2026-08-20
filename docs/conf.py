# Configuration file for the Sphinx documentation builder.

project = 'Boulder Eco Watch'
copyright = '2026, Boulder Eco Watch Team'
author = 'Boulder Eco Watch'

release = '1.0.0'

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Options for HTML output
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
