#   from templer.core.vars import var
from templer.localcommands import TemplerLocalTemplate


class DefaultContent(TemplerLocalTemplate):
    use_cheetah = True
    parent_templates = ['plonepolicy', ]

