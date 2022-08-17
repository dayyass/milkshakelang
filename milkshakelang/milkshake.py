from milkshakelang.utils import MilkShakeOverflowError

Size = {
    "demi": 3,
    "short": 8,
    "tall": 12,
    "grande": 16,
    "venti": 24,  # (20 ounces for hot drinks)
    "trenta": 30,
}


class MilkShake:
    """
    The only milkshakelang object to work with.
    """

    def __init__(
        self,
        owner: str,
        size: str,
    ):
        self.owner = owner
        self.size = size

        self._volume: int = Size[size]

        print(self._get_msg())

    def __repr__(self):
        return f"{self.owner}'s {self.size.capitalize()} MilkShake ({self._volume} ounces)\n"

    def _get_msg(self):
        return f"{self.owner} got {self.size.capitalize()} MilkShake ({self._volume} ounces)\n"

    def drink(
        self,
        ounces: int,  # TODO: validate positive number
    ) -> None:

        if self._volume == 0:
            msg = f"{self.owner}:\n- There is nothing to drink...\n- Need more milkshake!\n"

        elif ounces >= self._volume:
            msg = f"{self.owner}:\n- Drank {self._volume} ounces and finished my milkshake...\n- I want more!\n"
            self._volume = 0

        else:
            msg = f"{self.owner}:\n- Drank {ounces} ounces - so delicious!\n"
            self._volume -= ounces

        print(msg)

    def refill(
        self,
        ounces: int,  # TODO: validate positive number
    ) -> None:

        if self._volume + ounces < Size[self.size]:
            msg = f"{self.owner}:\n- Wow, {ounces} ounces of new milkshake!\n"
            self._volume += ounces

        elif self._volume + ounces == Size[self.size]:
            msg = f"{self.owner}:\n- Incredible, full cup of milkshake!\n"
            self._volume += ounces

        else:
            raise MilkShakeOverflowError("Milkshake was spilled on the floor!")

        print(msg)
