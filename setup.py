from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='zopeskel.plonepolicy',
      version=version,
      description="Zopeskel templates for Abstract development",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
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
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['abstract'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'PasteScript',
          'PasteDeploy',
          'Paste',
          'ZopeSkel'
          # -*- Extra requirements: -*-
      ],
      setup_requires=["PasteScript"],
      entry_points="""
      # -*- Entry points: -*-
      [paste.paster_create_template]
      plonepolicy = abstract.zopeskel.plonepolicy:PlonePolicy
      """,
      )
