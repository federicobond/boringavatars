from .utils import get_random_color, render

ELEMENTS = 64
SIZE = 80


def generate_colors(name, colors):
    num_from_name = hash(name)
    return [get_random_color(num_from_name + i, colors, len(colors)) for i in range(ELEMENTS)]


def pixel(name, colors):
    pixel_colors = generate_colors(name, colors)
    return render("pixel.svg", {"pixel_colors": pixel_colors, "SIZE": SIZE, "size": "80"})
