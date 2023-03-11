class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]


class BytecodeInterpreter:
    def __init__(self, bytecode):
        self.bytecode = bytecode
        self.ip = 0
        self.stack = Stack()
        self.variables = {}

    def run(self):
        while True:
            opcode = self.bytecode[self.ip]
            if opcode == 0x00:  # HALT
                break
            elif opcode == 0x01:  # PUSH
                value = self.bytecode[self.ip + 1]
                self.stack.push(value)
                self.ip += 2
            elif opcode == 0x02:  # ADD
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.push(a + b)
                self.ip += 1
            elif opcode == 0x03:  # SUB
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.push(b - a)
                self.ip += 1
            elif opcode == 0x04:  # MUL
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.push(a * b)
                self.ip += 1
            elif opcode == 0x05:  # DIV
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.push(b // a)
                self.ip += 1
            elif opcode == 0x06:  # PRINT
                value = self.stack.pop()
                print(value)
                self.ip += 1
            elif opcode == 0x07:  # STORE
                varname = self.bytecode[self.ip + 1]
                value = self.stack.pop()
                self.variables[varname] = value
                self.ip += 2
            elif opcode == 0x08:  # LOAD
                varname = self.bytecode[self.ip + 1]
                value = self.variables[varname]
                self.stack.push(value)
                self.ip += 2
            else:
                raise Exception("Invalid opcode")
