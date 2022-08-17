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

    def __repr__(self):
        return (
            f"{self.owner}'s {self.size.capitalize()} MilkShake ({self._volume} ounces)"
        )
