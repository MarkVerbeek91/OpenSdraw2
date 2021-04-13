import unittest
import mock

from opensdraw2.opensdraw2_elements.Function import Function, Arguments
from opensdraw2.opensdraw2_elements.Math import Add


class TestFunction(unittest.TestCase):
    def test_function_with_addition_no_arguments(self):
        add_mock = mock.Mock(Add)
        add_mock.return_value = 3
        func = Function(None, "name", mock.MagicMock(), add_mock)
        self.assertEqual(3, func())

    def test_function_with_addition_with_one_argument(self):
        add_mock = mock.Mock(spec=Add(None, None, None))
        add_mock.return_value = 3
        argument_mock = mock.Mock(spec=Arguments)
        argument_mock.return_value = dict(foo=2)
        func = Function(None, "name", argument_mock, add_mock)
        self.assertEqual(3, func(2))
        add_mock.assert_called_with(foo=2)

    def _test_function_with_addition_with_two_arguments(self):
        add_mock = mock.Mock(spec=Add(None, None, None))
        add_mock.return_value = 3
        argument_mock = mock.Mock(spec=Arguments(None, ["foo", "bar"]))
        argument_mock.return_value = dict(foo=2, bar=3)
        func = Function(None, "name", argument_mock, add_mock)
        self.assertEqual(5, func(2, 3))
        add_mock.assert_called_with(foo=2, bar=3)

    def test_function_with_addition_with_two_arguments(self):
        add_instance = Add(None, "foo", "bar")
        arg_instance = Arguments(None, ["foo", "bar"])

        func = Function(None, "name", arg_instance, add_instance)
        self.assertEqual(5, func(2, 3))


class TestArguments(unittest.TestCase):
    def test_arguments(self):
        args = Arguments(None, ["foo"])
        self.assertEqual({"foo": 42}, args(42))

    def test_two_arguments(self):
        args = Arguments(None, ["foo", "bar"])
        self.assertEqual({"foo": 42, "bar": 25}, args(42, 25))
