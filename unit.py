import unittest
from interpreter import BytecodeInterpreter


class TestCases(unittest.TestCase):
    def test_add(self):
        interpreter = BytecodeInterpreter([0x01, 0x03, 0x01, 0x04, 0x02, 0x00])
        interpreter.run()
        result = interpreter.stack.pop()
        self.assertEqual(result, 7)

    def test_sub(self):
        interpreter = BytecodeInterpreter([0x01, 0x06, 0x01, 0x01, 0x03, 0x00])
        interpreter.run()
        result = interpreter.stack.pop()
        self.assertEqual(result, 5)

    def test_mul(self):
        interpreter = BytecodeInterpreter([0x01, 0x06, 0x01, 0x05, 0x04, 0x00])
        interpreter.run()
        result = interpreter.stack.pop()
        self.assertEqual(result, 30)

    def test_div(self):
        interpreter = BytecodeInterpreter([0x01, 0x06, 0x01, 0x03, 0x05, 0x00])
        interpreter.run()
        result = interpreter.stack.pop()
        self.assertEqual(result, 2)
