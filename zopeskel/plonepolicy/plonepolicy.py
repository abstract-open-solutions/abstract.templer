import copy

from zopeskel.basic_namespace import BasicNamespace
from zopeskel.base import get_var
# from zopeskel.base import var


class PlonePolicy(BasicNamespace):
    _template_dir = 'templates/plonepolicy'
    summary = "A Plone policy product"

    required_templates = []
    use_cheetah = True
    vars = copy.deepcopy(BasicNamespace.vars)
    get_var(vars, 'namespace_package').default = 'plone'
    get_var(vars, 'package').default = 'example'
    get_var(vars, 'description').default = 'Plone Policy Product'
    get_var(vars, 'license_name').default = 'GPL version 2'
    get_var(vars, 'author').default = 'Abstract'
    get_var(vars, 'author_email').default = 'info@abstract.it'
    get_var(vars, 'url').default = 'http://git.abstract.it'
