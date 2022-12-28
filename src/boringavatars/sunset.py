import hashlib

from .utils import hash_code, get_random_color, render

ELEMENTS = 4
SIZE = 80


def generate_colors(name, colors):
    num_from_name = hash_code(name)
    return [
        get_random_color(num_from_name + i, colors, len(colors))
        for i in range(ELEMENTS)
    ]


def sunset(name, *, colors, size, title, square):
    sunset_colors = generate_colors(name, colors)
    name = hashlib.sha1(name.encode("utf-8")).hexdigest()
    return render(
        "sunset.svg",
        {
            "name": name,
            "sunset_colors": sunset_colors,
            "SIZE": SIZE,
            "size": size,
            "title": title,
            "square": square,
        },
    )
