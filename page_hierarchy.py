from pelican import signals
from os.path import splitext, dirname

'''
This plugin creates a URL hierarchy for pages that matches the
filesystem hierarchy of their sources.

To maintain a URL hierarchy that is consistent with the filesystem
hierarchy, the slug of each page is forced to be its source base
filename.
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

def reflect_page_hierarchy(generator):
    # set url and save_as attributes
    for page in generator.pages:
        path = get_path(page, generator.settings)
        if not hasattr(page, 'override_url'):
            page.override_url = '%s/' % path
        if not hasattr(page, 'override_save_as'):
            page.override_save_as = '%s/index.html' % path

        # initialize parents and children lists
        page.parent = None
        page.parents = []
        page.children = []

    # set immediate parents and children
    for page in generator.pages:
        parent = dirname(dirname(page.url))
        if parent: parent += '/'
        for page2 in generator.pages:
            if page2.url == parent:
                page.parent = page2
                page2.children.append(page)

    # set all parents (ancestors)
    for page in generator.pages:
        p = page
        while p.parent:
            page.parents.insert(0, p.parent)
            p = p.parent


def register():
    signals.page_generator_finalized.connect(reflect_page_hierarchy)
