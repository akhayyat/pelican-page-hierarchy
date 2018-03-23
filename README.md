Page Hierarchy
==============
*Author: Ahmad Khayyat (<akhayyat@gmail.com>)*

A [Pelican][1] plugin that creates a URL hierarchy for pages that
matches the filesystem hierarchy of their sources.

For example, to have the following filesystem structure of page
sources result in the URLs listed next to each file,

```text
└── content/pages/           #   PAGE_DIR
    ├── about.md             # URL: pages/about/
    ├── projects.md          # URL: pages/projects/
    ├── projects/            #   (directory)
    │   ├── p1.md            # URL: pages/projects/p1/
    │   ├── p2.md            # URL: pages/projects/p2/
    │   └── p2/              #   (directory)
    │       └── features.md  # URL: pages/projects/p2/features/
    └── contact.md           # URL: pages/contact/
```

you can use this plugin with the following Pelican settings:

```python
# pelicanconf.py
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
SLUGIFY_SOURCE = 'basename'
```

When generating the `url` and `save_as` attributes, the plugin
prefixes the page's `slug` by its relative path. Although the initial
`slug` is generated from the page's `title` by default, it can be
generated from the source file basename by setting the
`SLUGIFY_SOURCE` setting to `'basename'`, as shown in the settings
snippet above. The `slug` can also be set using [`PATH_METADATA`][2].

This plugin is compatible with [Pelican translations][3].

Parent and Children Pages
-------------------------
This plugin also adds three attributes to each page object:

- `parent`: the immediate parent page. `None` if the page is
  top-level. If a translated page has no parent, the default-language
  parent is used.

- `parents`: a list of all ancestor pages, starting from the top-level
  ancestor.

- `children`: a list of all immediate child pages, in no specific
  order.

These attributes can be used to generate breadcrumbs or nested
navigation menus. For example, this is a template excerpt for
breadcrumbs:

```html
<ul class="breadcrumb">
  <li><a href="{{ SITEURL }}/" title="{{ SITENAME }}">
    <i class="fa fa-home fa-lg"></i>
  </a></li>
  {% for parent in page.parents %}
  <li><a href="{{ SITEURL }}/{{ parent.url }}">{{ parent.title }}</a></li>
  {% endfor %}
  <li class="active">{{ page.title }}</li>
</ul>

```


License
-------

Licence: BSD. See the included `LICENSE` file.


[1]: http://getpelican.com/
[2]: http://docs.getpelican.com/en/latest/settings.html#path-metadata
[3]: http://docs.getpelican.com/en/latest/settings.html#translations
