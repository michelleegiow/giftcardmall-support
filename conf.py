# Sphinx configuration for GiftCardMall Balance Guide

project = 'GiftCardMall Balance Guide'
copyright = '2026, Cardholder Community'
author = 'Cardholder Documentation Team'
version = '1.0'
release = '1.0.0'

# Extensions
extensions = []

# Theme
html_theme = 'alabaster'

# Theme options
html_theme_options = {
    'description': 'Comprehensive guide for checking GiftCardMall prepaid card balances',
    'github_button': False,
    'show_powered_by': False,
}

# General configuration
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
master_doc = 'index'
language = 'en'

# HTML output
html_static_path = []
html_show_sourcelink = False
html_show_sphinx = False
