import pytest

from boringavatars import avatar


@pytest.mark.parametrize(
    "variant", ["beam", "marble", "pixel", "sunset", "bauhaus", "ring"]
)
def test_avatar(variant):
    avatar("foobar", variant=variant)
