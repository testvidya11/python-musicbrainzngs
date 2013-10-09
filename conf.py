# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'musicbrainzngs'
copyright = u'2012, Alastair Porter et al'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.0'
# The full version, including alpha/beta/rc tags.
release = '0.0.0'

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

# force default theme on readthedocs
html_style = "/default.css"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
        "footerbgcolor": "#e7e7e7",
        "footertextcolor": "#444444",
        "sidebarbgcolor": "#ffffff",
        "sidebartextcolor": "#000000",
        "sidebarlinkcolor": "002bba",
        "relbarbgcolor": "#5c5789",
        "relbartextcolor": "#000000",
        "bgcolor": "#ffffff",
        "textcolor": "#000000",
        "linkcolor": "#002bba",
        "headbgcolor": "#ffba58",
        "headtextcolor": "#515151",
        "codebgcolor":  "#dddddd",
        "codetextcolor": "#000000"
        }

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = ''
