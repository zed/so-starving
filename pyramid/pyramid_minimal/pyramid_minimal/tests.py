import unittest

from pyramid.configuration import Configurator

class MyControllerTests(unittest.TestCase):
    def setUp(self):
        self.config = Configurator()
        self.config.begin()

    def tearDown(self):
        self.config.end()

    def _makeOne(self, request):
        from pyramid_minimal.handlers import MyHandler
        return MyHandler(request)

    def test_index(self):
        request = DummyRequest()
        controller = self._makeOne(request)
        info = controller.index()
        self.assertEqual(info['project'], 'pyramid_minimal')

class DummyRequest(object):
    pass
