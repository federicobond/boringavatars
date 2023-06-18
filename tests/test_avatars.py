import unittest

from boringavatars import avatar


class AvatarTests(unittest.TestCase):
    def test_avatar_beam(self):
        avatar("foobar", variant="beam")

    def test_avatar_marble(self):
        avatar("foobar", variant="marble")

    def test_avatar_pixel(self):
        avatar("foobar", variant="pixel")

    def test_avatar_sunset(self):
        avatar("foobar", variant="sunset")

    def test_avatar_bauhaus(self):
        avatar("foobar", variant="bauhaus")

    def test_avatar_ring(self):
        avatar("foobar", variant="ring")


if __name__ == "__main__":
    unittest.main()
