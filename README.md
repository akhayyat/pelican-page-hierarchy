Page Hierarchy
==============
*Author: Ahmad Khayyat (<akhayyat@gmail.com>)*

A [Pelican][1] plugin that creates a URL hierarchy for pages that
matches the filesystem hierarchy of their sources.

For example, the following filesystem structure for page sources will
result in the URLs listed next to each page when this plugin is used and
`PAGE_URL = 'pages/{slug}/'` and  `PAGE_SAVE_AS = 'pages/{slug}/index.html'`
are set.

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
When generating the `url` and `save_as` values, the plugin attaches
relative path prefix to page's `slug` property (which can be
auto-slugified from `title`, `basename`, `PATH_METADATA`, or set manually).

The plugin is aware and works well with translations.

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


[1]: http://getpelican.com/
