Introduction
============

This package contains some ZopeSkel templates usefull for development in abstract.


How to use
----------

You can use this product as 'traditional' zopeskel script::

    $ zopeskel <template_name> <egg.name>


Available Templates
-------------------

plonepolicy:
this template creates a plone policy package

plonetheme:
this template creates a plone theme package it depends on plone.app.theming


Local commands
--------------

For plonepolicy template is available a local command which allow to create default content structure with collective.transmogrifier pieline

usage::

   $ zopeskel plonepolicy test.policy
   ...
   $ cd test.policy/src
   $ paster  add loadcontent

