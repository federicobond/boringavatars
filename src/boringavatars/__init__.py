from .bauhaus import bauhaus
from .beam import beam
from .marble import marble
from .pixel import pixel
from .ring import ring
from .sunset import sunset

__version__ = "1.0.0"

__all__ = ["avatar"]

DEFAULT_COLORS = ["FFAD08", "EDD75A", "73B06F", "0C8F8F", "405059"]

VARIANTS = {
    "beam": beam,
    "marble": marble,
    "pixel": pixel,
    "sunset": sunset,
    "bauhaus": bauhaus,
    "ring": ring,
}


def avatar(
    name: str,
    *,
    colors: list[str] = DEFAULT_COLORS,
    variant: str = "marble",
    title: bool = False,
    size: int = 40,
    square: bool = False,
) -> str:
    """Generate an avatar SVG string with the given parameters."""
    if variant not in VARIANTS:
        raise ValueError(f"unrecognized variant: {variant}")

    fn = VARIANTS[variant]
    colors = [c.lstrip("#") for c in colors]
    return fn(name, colors=colors, size=size, title=title, square=square)
