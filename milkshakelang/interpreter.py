from collections import namedtuple
from typing import List

from milkshakelang.milkshake import MilkShake

Node = namedtuple(
    "Node",
    ["cmd", "args"],
)


class AST:
    """
    Abstract Syntax Tree.
    """

    @staticmethod
    def give_milkshake(tokens: List[str]) -> Node:
        """
                give_milkshake
                /     |     \
            owner   size   milkshake
        """

        # TODO: add try/except
        cmd, owner, size, milkshake = tokens

        return Node(
            cmd=cmd,
            args={
                "owner": owner,
                "size": size,
                "milkshake": milkshake,  # TODO: remove redundant
            },
        )

    @staticmethod
    def drink_milkshake(tokens: List[str]) -> Node:
        """
                drink_milkshake
                /      |      \
            owner  milkshake  ounces
        """

        # TODO: add try/except
        cmd, owner, milkshake, ounces = tokens

        return Node(
            cmd=cmd,
            args={
                "owner": owner,
                "milkshake": milkshake,  # TODO: remove redundant
                "ounces": int(ounces),  # TODO: allow not only int
            },
        )

    @staticmethod
    def refill_milkshake(tokens: List[str]) -> Node:
        """
                refill_milkshake
                /      |      \
            owner  milkshake  ounces
        """

        # the same code
        return AST.drink_milkshake(tokens)


class Interpreter:
    """
    Milkshakelang Interpreter.
    """

    def _lexicalize(
        self,
        statement: str,
    ) -> List[str]:

        return statement.split()

    def _parse(
        self,
        statement_list: List[str],
    ) -> List[Node]:

        nodes = []

        for statement in statement_list:

            if (statement in {"\n", " ", ""}) or statement.startswith("#"):
                continue

            tokens = self._lexicalize(statement)
            cmd = tokens[0]

            if cmd == "give":
                node = AST.give_milkshake(tokens)
            elif cmd == "drink":
                node = AST.drink_milkshake(tokens)
            elif cmd == "refill":
                node = AST.refill_milkshake(tokens)
            else:
                # TODO: choose Exception
                raise Exception(f"Unknown command: {cmd}")

            nodes.append(node)
        return nodes

    # TODO: optimize
    def _interpret(
        self,
        statement_list: List[str],
    ) -> None:

        people = {}
        nodes = self._parse(statement_list)

        for node in nodes:

            # TODO: remove code duplicates from _parse
            if node.cmd == "give":
                people[node.args["owner"]] = MilkShake(
                    owner=node.args["owner"],
                    size=node.args["size"],
                )

            elif node.cmd == "drink":
                # TODO: try/except KeyError
                people[node.args["owner"]].drink(node.args["ounces"])

            elif node.cmd == "refill":
                # TODO: try/except KeyError
                people[node.args["owner"]].refill(node.args["ounces"])

            else:
                # TODO: choose Exception
                raise Exception(f"Unknown command: {node.cmd}")

    def interpret(
        self,
        script: str,
    ) -> None:  # TODO: add exit code

        statement_list = script.splitlines()
        self._interpret(statement_list)
