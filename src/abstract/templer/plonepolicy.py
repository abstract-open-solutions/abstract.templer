import copy
from .base import BaseTemplate
from templer.core.base import get_var


class PlonePolicy(BaseTemplate):
    _template_dir = 'templates/plonepolicy'
    summary = "A Plone policy product"
    use_local_commands = True

    vars = copy.deepcopy(BaseTemplate.vars)
    get_var(vars, 'package').default = 'policy'
    get_var(vars, 'description').default = 'Plone Policy Product'
    # get_var(vars, 'use_localcommands') = True

    def pre(self, command, output_dir, vars):
        super(PlonePolicy, self).pre(command, output_dir, vars)
        vars['use_localcommands'] = self.use_local_commands
