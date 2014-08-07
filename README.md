Page Hierarchy
==============
*Author: Ahmad Khayyat (<akhayyat@gmail.com>)*

A [Pelican][1] plugin that creates a URL hierarchy for pages that
matches the filesystem hierarchy of their sources. For example, the
following filesystem structure for page sources will result in the
URLs listed next to each page when this plugin is used with the
default pelican settings.

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

To remove the `pages/` prefix and have pages at the root of your site:

```python
# pelicanconf.py
PATH_METADATA = 'pages/(?P<path>.*)\..*'
```

More generally, any value for the `PATH_METADATA` pelican setting that
defines a `path` group will result in using the matching part of the
source file path as the path for that page in the URL. This allows
capturing other metadata from the source path.

In order to maintain a URL hierarchy that is consistent with the
filesystem hierarchy, the slug of each page is forced to be its source
base filename. The page title and its slug attribute have no effect.

Parent and Children Pages
-------------------------
This plugin also adds three attributes to each page object:

- `parent`: the immediate parent page. `None` if the page is
  top-level.

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


[1]: http://getpelican.com/
