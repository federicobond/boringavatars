from .utils import hash_code, get_random_color, render

ELEMENTS = 64
SIZE = 80


def generate_colors(name, colors):
    num_from_name = hash_code(name)
    return [
        get_random_color(num_from_name % (i + 1), colors, len(colors))
        for i in range(ELEMENTS)
    ]


def pixel(name, *, colors, size, title, square):
    pixel_colors = generate_colors(name, colors)
    return render(
        "pixel.svg",
        {
            "name": name,
            "pixel_colors": pixel_colors,
            "SIZE": SIZE,
            "size": size,
            "title": title,
            "square": square,
        },
    )
