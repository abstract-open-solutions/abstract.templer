import copy

from templer.core.basic_namespace import BasicNamespace
from templer.core.base import get_var


class PloneTheme(BasicNamespace):
    _template_dir = 'templates/plonetheme'
    summary = "A Plone theme product"
    category = "Plone Development"
    required_templates = []

    vars = copy.deepcopy(BasicNamespace.vars)
    get_var(vars, 'namespace_package').default = 'plone'
    get_var(vars, 'package').default = 'example'
    get_var(vars, 'description').default = 'Plone Theme Product'
    get_var(vars, 'license_name').default = 'GPL'
    get_var(vars, 'author').default = 'Abstract'
    get_var(vars, 'author_email').default = 'info@abstract.it'
    get_var(vars, 'url').default = 'http://git.abstract.it'
