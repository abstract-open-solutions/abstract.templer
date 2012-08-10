import copy
from .base import BaseTemplate
from templer.core.base import get_var


class PloneTheme(BaseTemplate):
    _template_dir = 'templates/plonetheme'
    summary = "A Plone theme product"

    vars = copy.deepcopy(BaseTemplate.vars)
    get_var(vars, 'package').default = 'theme'
    get_var(vars, 'description').default = 'Plone Theme Product'
