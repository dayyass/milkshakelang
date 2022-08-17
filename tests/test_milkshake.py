import unittest

from parameterized import parameterized

from src.milkshake import MilkShake, Size


class TestMilkShake(unittest.TestCase):
    @parameterized.expand([(size,) for size in Size])
    def test_drink(self, size):
        self.milkshake = MilkShake(owner="Igor", size=size)
        self.assertEqual(self.milkshake._volume, Size[size])

        self.milkshake.drink(ounces=16)
        self.assertEqual(self.milkshake._volume, max(0, Size[size] - 16))

        self.milkshake.drink(ounces=16)
        self.assertEqual(self.milkshake._volume, max(0, Size[size] - 16 - 16))

        self.milkshake.drink(ounces=15)
        self.assertEqual(self.milkshake._volume, 0)
