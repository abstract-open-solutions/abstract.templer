from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='abstract.templer',
      version=version,
      description="Zopeskel templates for Abstract development",
      long_description=open("README.md").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "Framework :: Zope3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone',
      author='Giorgio Borelli',
      author_email='giorgio@abstract.it',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['abstract'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'PasteScript',
          'Paste',
          'ZopeSkel',
          'templer.core',
          'templer.localcommands',

      ],
      setup_requires=["PasteScript"],
      entry_points="""
      # -*- Entry points: -*-
      [paste.paster_create_template]
      plonepolicy = abstract.templer.plonepolicy:PlonePolicy
      plonetheme = abstract.templer.plonetheme:PloneTheme

      [templer.templer_structure]
      test_buildout = abstract.templer.structures:TestBuildoutStructure
      git = abstract.templer.structures:GitStructure

      [templer.templer_sub_template]
      defaultcontent = abstract.templer.defaultcontent:DefaultContent
      """,
      )
