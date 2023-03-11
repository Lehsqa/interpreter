class Stack:  # stack with commands
    def __init__(self):
        self.stack = []  # stack for store value

    def push(self, value):  # PUSH (add value to stack)
        self.stack.append(value)

    def pop(self):  # POP (delete and get value from stack)
        return self.stack.pop()

    def peek(self):  # PEEK (get last value from stack)
        return self.stack[-1]


class BytecodeInterpreter:  # interpreter for instruction definition
    def __init__(self, bytecode):
        self.bytecode = bytecode  # list of bytecode
        self.ip = 0  # iterator
        self.stack = Stack()  # stack with commands
        self.variables = {}  # additional stack for store variables

    def run(self):
        while True:
            opcode = self.bytecode[self.ip]
            if opcode == 0x00:  # HALT (end code)
                break
            elif opcode == 0x01:  # PUSH (add value to stack)
                value = self.bytecode[self.ip + 1]
                self.stack.push(value)
                self.ip += 2
            elif opcode == 0x02:  # ADD (add two values from stack)
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.push(a + b)
                self.ip += 1
            elif opcode == 0x03:  # SUB (sub two values from stack)
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.push(b - a)
                self.ip += 1
            elif opcode == 0x04:  # MUL (mul two values from stack)
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.push(a * b)
                self.ip += 1
            elif opcode == 0x05:  # DIV (div two values from stack)
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.push(b // a)
                self.ip += 1
            elif opcode == 0x06:  # PRINT (print value at terminal)
                value = self.stack.pop()
                print(value)
                self.ip += 1
            elif opcode == 0x07:  # STORE (store value in self.variables)
                varname = self.bytecode[self.ip + 1]
                value = self.stack.pop()
                self.variables[varname] = value
                self.ip += 2
            elif opcode == 0x08:  # LOAD (load value from self.variables)
                varname = self.bytecode[self.ip + 1]
                value = self.variables[varname]
                self.stack.push(value)
                self.ip += 2
            else:
                raise Exception("Invalid opcode")  # No one code has been detected
