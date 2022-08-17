import unittest

from parameterized import parameterized

from milkshakelang.milkshake import MilkShake, Size
from milkshakelang.utils import MilkShakeOverflowError


class TestMilkShake(unittest.TestCase):
    @parameterized.expand([(size,) for size in Size])
    def test(self, size):
        self.milkshake = MilkShake(owner="Igor", size=size)
        self.assertEqual(self.milkshake._volume, Size[size])

        self.milkshake.drink(ounces=16)
        self.assertEqual(self.milkshake._volume, max(0, Size[size] - 16))

        self.milkshake.drink(ounces=16)
        self.assertEqual(self.milkshake._volume, max(0, Size[size] - 32))

        self.milkshake.drink(ounces=16)
        self.assertEqual(self.milkshake._volume, 0)

        if size in {"demi", "short"}:
            with self.assertRaises(MilkShakeOverflowError):
                self.milkshake.refill(ounces=12)
            return

        self.milkshake.refill(ounces=12)
        self.assertEqual(self.milkshake._volume, 12)

        if size in {"tall", "grande"}:
            with self.assertRaises(MilkShakeOverflowError):
                self.milkshake.refill(ounces=12)
            return

        self.milkshake.refill(ounces=12)
        self.assertEqual(self.milkshake._volume, 24)

        with self.assertRaises(MilkShakeOverflowError):
            self.milkshake.refill(ounces=12)
