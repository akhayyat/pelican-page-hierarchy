from pelican import signals, contents
from os.path import splitext, dirname

'''
This plugin creates a URL hierarchy for pages that matches the
filesystem hierarchy of their sources.

To maintain a URL hierarchy that is consistent with the filesystem
hierarchy, the slug of each page is forced to be the path of its source
file.
'''

def get_path(page, settings):
    '''
    if a 'path' is defined in PATH_METADATA, extract it. otherwise,
    use the entire path after removing PAGE_DIR and the file
    extension.
    '''
    if '<path>' in settings['PATH_METADATA']:
        return page.path
    else:
        return splitext(page.get_relative_source_path())[0]

def override_metadata(content_object):
    if type(content_object) is contents.Page:
        page = content_object

        # set url, slug, and save_as attributes
        path = get_path(page, page.settings)
        if not hasattr(page, 'override_url'):
            page.override_url = '%s/' % path
            page.slug = '%s' % path
        if not hasattr(page, 'override_save_as'):
            page.override_save_as = '%s/index.html' % path

def set_relationships(generator):
    # initialize parents and children lists
    for page in generator.pages:
        page.parent = None
        page.parents = []
        page.children = []

    # set immediate parents and children
    for page in generator.pages:
        parent_url = dirname(dirname(page.url))
        if parent_url: parent_url += '/'
        for page2 in generator.pages:
            if page2.url == parent_url and page2 != page:
                page.parent = page2
                page2.children.append(page)

    # set all parents (ancestors)
    for page in generator.pages:
        p = page
        while p.parent:
            page.parents.insert(0, p.parent)
            p = p.parent


def register():
    signals.content_object_init.connect(override_metadata)
    signals.page_generator_finalized.connect(set_relationships)
