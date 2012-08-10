import os
import copy

from templer.core.basic_namespace import BasicNamespace
from templer.core.base import get_var


class BaseTemplate(BasicNamespace):
    _template_dir = ''
    summary = ""
    category = "Plone Development"
    required_templates = []
    default_required_structures = ['bootstrap', 'test_buildout', 'git', ]

    use_cheetah = True
    vars = copy.deepcopy(BasicNamespace.vars)
    get_var(vars, 'namespace_package').default = 'abstract'
    get_var(vars, 'package').default = ''
    get_var(vars, 'description').default = 'Plone Product'
    get_var(vars, 'license_name').default = 'GPL'
    get_var(vars, 'author').default = 'Abstract'
    get_var(vars, 'author_email').default = 'info@abstract.it'
    get_var(vars, 'url').default = 'http://git.abstract.it'

    def post(self, command, output_dir, vars):
        super(BaseTemplate, self).post(command, output_dir, vars)
        # XXX: zopeskel doesn't support files which starts with dot
        # move gitignore file to .gitignore...
        orig = os.sep.join((output_dir, 'gitignore'))
        dest = os.sep.join((output_dir, '.gitignore'))
        os.rename(orig, dest)
