from collections import namedtuple
from typing import List

from milkshake import MilkShake

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

        # TODO:
        cmd, owner, size, milkshake = tokens

        return Node(
            cmd=cmd,
            args={
                "owner": owner,
                "size": size,
                "milkshake": milkshake,  # TODO: remove redundant
            },
        )


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

            tokens = self._lexicalize(statement)
            cmd = tokens[0]

            if cmd == "give":
                node = AST.give_milkshake(tokens)

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

                milkshake = MilkShake(
                    owner=node.args["owner"],
                    size=node.args["size"],
                )
                print(milkshake)

                people[node.args["owner"]] = milkshake

            else:
                # TODO: choose Exception
                raise Exception(f"Unknown command: {node.cmd}")

    def interpret(
        self,
        script: str,
    ) -> None:  # TODO: add exit code

        statement_list = script.splitlines()
        self._interpret(statement_list)
