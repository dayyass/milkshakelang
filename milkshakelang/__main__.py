import sys

from milkshakelang.interpreter import Interpreter


def main():
    """
    Main function and entrypoint.
    """

    interpreter = Interpreter()

    with open(sys.argv[1], mode="r") as fp:
        script = fp.read()

    interpreter.interpret(script)


if __name__ == "__main__":
    main()
