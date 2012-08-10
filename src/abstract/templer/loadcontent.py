#   from templer.core.vars import var
from templer.localcommands import TemplerLocalTemplate


class LoadContent(TemplerLocalTemplate):
    _template_dir = 'templates/loadcontent'
    use_cheetah = True
    parent_templates = ['plonepolicy', ]

    summary = ("A boilerplate to load default content "
        "structure with transmogrifier")
