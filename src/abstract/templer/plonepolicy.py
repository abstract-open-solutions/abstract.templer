import copy
from .base import BaseTemplate
from templer.core.base import get_var

try:
    from templer.localcommands import SUPPORTS_LOCAL_COMMANDS
    from templer.localcommands import LOCAL_COMMANDS_MESSAGE
except ImportError:
    SUPPORTS_LOCAL_COMMANDS = False


POST_RUN_TEXT = ""
if SUPPORTS_LOCAL_COMMANDS:
    POST_RUN_TEXT = LOCAL_COMMANDS_MESSAGE


class PlonePolicy(BaseTemplate):
    _template_dir = 'templates/plonepolicy'
    summary = "A Plone policy product"
    use_local_commands = SUPPORTS_LOCAL_COMMANDS
    post_run_msg = POST_RUN_TEXT

    vars = copy.deepcopy(BaseTemplate.vars)
    get_var(vars, 'package').default = 'policy'
    get_var(vars, 'description').default = 'Plone Policy Product'
    # get_var(vars, 'use_localcommands') = True

    def pre(self, command, output_dir, vars):
        super(PlonePolicy, self).pre(command, output_dir, vars)
        vars['use_localcommands'] = self.use_local_commands
