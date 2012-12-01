Introduction
============

This package contains some `ZopeSkel`__ templates useful internal development at

.. image:: http://www.abstract.it/++theme++abstract.theme/theme/static/theme/img/online/logo.png
   :alt: Abstract Website
   :target: http://wwww.abstract.it

Available Templates
-------------------

Once installed the following templates will be available:

plonepolicy
	this template creates a plone policy package

plonetheme
	this template creates a plone theme package it depends on plone.app.theming

How to use
----------

Run zopeskel as usual by passing the name of the template to be used and the name of package to create::

    $ zopeskel <template_name> <my.package>


Local commands
--------------

For `plonepolicy` template is available a local command that allows to create default content structure with a `collective.transmogrifier`__ pipeline

usage::

   $ zopeskel plonepolicy test.policy
   $ cd test.policy/src
   $ paster  add loadcontent 


__ http://pypi.python.org/pypi/ZopeSkel
__ http://pypi.python.org/pypi/collective.transmogrifier

