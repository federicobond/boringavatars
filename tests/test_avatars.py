import random
import unittest

from boringavatars import avatar
from snapshottest import TestCase


class AvatarTests(TestCase):
    def setUp(self):
        random.seed(13)  # used for consistent mask ids

    def test_avatar_beam(self):
        out = avatar("foobar", variant="beam")
        self.assertMatchSnapshot(out)

    def test_avatar_marble(self):
        out = avatar("foobar", variant="marble")
        self.assertMatchSnapshot(out)

    def test_avatar_pixel(self):
        out = avatar("foobar", variant="pixel")
        self.assertMatchSnapshot(out)

    def test_avatar_sunset(self):
        out = avatar("foobar", variant="sunset")
        self.assertMatchSnapshot(out)

    def test_avatar_bauhaus(self):
        out = avatar("foobar", variant="bauhaus")
        self.assertMatchSnapshot(out)

    def test_avatar_ring(self):
        out = avatar("foobar", variant="ring")
        self.assertMatchSnapshot(out)


if __name__ == "__main__":
    unittest.main()
