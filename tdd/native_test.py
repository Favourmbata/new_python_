from unittest import TestCase

from tdd.native import native


class TestNative(TestCase):
    def test_native_object(self):
        our_native = native("tosin","scv123")
        print(our_native)
        print(our_native.get_name())
