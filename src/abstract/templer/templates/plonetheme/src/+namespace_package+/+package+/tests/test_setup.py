# -*- coding: utf-8 -*-
import unittest2 as unittest
from ..testing import INTEGRATION_TESTING


class TestSetup(unittest.TestCase):
    layer = INTEGRATION_TESTING


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
