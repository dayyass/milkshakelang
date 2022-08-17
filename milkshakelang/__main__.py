import sys

from interpreter import Interpreter

if __name__ == "__main__":

    interpreter = Interpreter()

    with open(sys.argv[1], mode="r") as fp:
        script = fp.read()

    interpreter.interpret(script)
