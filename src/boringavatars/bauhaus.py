from .utils import get_boolean, get_random_color, get_unit, render

ELEMENTS = 4
SIZE = 80


def generate_colors(name, colors):
    num_from_name = hash(name)

    return [
        {
            "color": get_random_color(num_from_name + i, colors, len(colors)),
            "translate_x": get_unit(num_from_name * (i + 1), SIZE / 2 - (i + 17), 1),
            "translate_y": get_unit(num_from_name * (i + 1), SIZE / 10 - (i + 17), 2),
            "rotate": get_unit(num_from_name * (i + 1), 360),
            "is_square": get_boolean(num_from_name, 2),
        }
        for i in range(ELEMENTS)
    ]


def bauhaus(name, colors):
    properties = generate_colors(name, colors)
    return render("bauhaus.svg", {"properties": properties, "SIZE": SIZE, "size": "80"})
