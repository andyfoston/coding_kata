#!/usr/bin/env python3

from unittest import TestCase, main, mock

from basic_arithmetic import add, divide, multiply, parse_args, subtract, run


class MockArgs:
    def __init__(self, **args):
        self.items = args
    
    def __getattr__(self, key):
        return self.items.get(key, False)


class TestArithmeticFunctions(TestCase):
    def test_add(self):
        self.assertEqual(4, add(3, 1))

    def test_subtract(self):
        self.assertEqual(4, subtract(7, 3))

    def test_multiply(self):
        self.assertEqual(6, multiply(3, 2))

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(7, 0)
    
    def test_divide(self):
        self.assertEqual(3.5, divide(7, 2))


class TestParseArgs(TestCase):
    def test_parse_add(self):
        args = parse_args(["5", "10", "-a"])
        self.assertEqual(args.operand, [5.0, 10.0])
        self.assertTrue(args.add)
        self.assertFalse(args.subtract)
        self.assertFalse(args.multiply)
        self.assertFalse(args.divide)

    def test_parse_subtract(self):
        args = parse_args(["-s", "7", "6.2"])
        self.assertEqual(args.operand, [7.0, 6.2])
        self.assertTrue(args.subtract)
        self.assertFalse(args.add)
        self.assertFalse(args.multiply)
        self.assertFalse(args.divide)

    def test_parse_multiply(self):
        args = parse_args(["-m", "100", "2"])
        self.assertEqual(args.operand, [100.0, 2.0])
        self.assertTrue(args.multiply)
        self.assertFalse(args.subtract)
        self.assertFalse(args.add)
        self.assertFalse(args.divide)

    def test_parse_divide(self):
        args = parse_args(["-d", "60", "3"])
        self.assertEqual(args.operand, [60.0, 3.0])
        self.assertTrue(args.divide)
        self.assertFalse(args.multiply)
        self.assertFalse(args.subtract)
        self.assertFalse(args.add)

    def test_parse_one_operand(self):
        with mock.patch("basic_arithmetic.ArgumentParser.error") as mock_error:
            parse_args(["-d", "60"])
        mock_error.assert_called()

    def test_parse_three_operands(self):
        with mock.patch("basic_arithmetic.ArgumentParser.error") as mock_error:
            parse_args(["-d", "60", "70", "100"])
        mock_error.assert_called()

    def test_parse_no_operator(self):
        with mock.patch("basic_arithmetic.ArgumentParser.error") as mock_error:
            parse_args(["60", "70"])
        mock_error.assert_called()


class TestRun(TestCase):
    def test_run_add(self):
        args = MockArgs(add=True, operand=[3, 5])
        self.assertEqual(run(args), "3 + 5 = 8")
    
    def test_run_subtract(self):
        args = MockArgs(subtract=True, operand=[6, 4])
        self.assertEqual(run(args), "6 - 4 = 2")

    def test_run_multiply(self):
        args = MockArgs(multiply=True, operand=[2, 6])
        self.assertEqual(run(args), "2 * 6 = 12")

    def test_run_divide(self):
        args = MockArgs(divide=True, operand=[8, 2])
        self.assertEqual(run(args), "8 / 2 = 4.0")

    def test_run_divide_zero(self):
        args = MockArgs(divide=True, operand=[3, 0])
        with self.assertRaises(ZeroDivisionError):
            run(args)


if __name__ == '__main__':
    main()
