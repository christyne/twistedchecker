# A module with interfaces for use in the test examples
from zope.interface import Interface


class IFoo(Interface):
    def bar():
        pass
