Size = {
    "demi": 3,
    "short": 8,
    "tall": 12,
    "grande": 16,
    "venti": 24,  # (20 ounces for hot drinks)
    "trenta": 31,
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

    def __repr__(self):
        return (
            f"{self.owner}'s {self.size.capitalize()} MilkShake ({self._volume} ounces)"
        )

    def drink(
        self,
        ounces: int,
    ) -> None:

        if self._volume == 0:
            print(
                f"{self.owner}:\n- There is nothing to drink...\n- Need more milkshake!\n"
            )
            return

        elif ounces >= self._volume:
            print(
                f"{self.owner}:\n- Drank {self._volume} ounces and finished my milkshake...\n- I want more!\n"
            )
            self._volume = 0
            return

        else:
            print(f"{self.owner}:\n- Drank {ounces} ounces - so delicious!\n")
            self._volume -= ounces
            return
