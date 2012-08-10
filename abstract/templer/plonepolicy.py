import copy
from .base import BaseTemplate
from templer.core.base import get_var


class PlonePolicy(BaseTemplate):
    _template_dir = 'templates/plonepolicy'
    summary = "A Plone policy product"

    vars = copy.deepcopy(BaseTemplate.vars)
    get_var(vars, 'package').default = 'policy'
    get_var(vars, 'description').default = 'Plone Policy Product'
