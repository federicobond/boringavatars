from .utils import get_random_color, hash_code, random_id, render

SIZE = 90
COLORS = 5


def generate_colors(name, colors):
    num_from_name = hash_code(name)
    colors_shuffle = [
        get_random_color(num_from_name + i, colors, len(colors)) for i in range(COLORS)
    ]
    return [
        colors_shuffle[0],
        colors_shuffle[1],
        colors_shuffle[1],
        colors_shuffle[2],
        colors_shuffle[2],
        colors_shuffle[3],
        colors_shuffle[3],
        colors_shuffle[0],
        colors_shuffle[4],
    ]


def ring(name, *, colors, size, title, square):
    ring_colors = generate_colors(name, colors)
    return render(
        "ring.svg",
        {
            "name": name,
            "mask_id": random_id(),
            "ring_colors": ring_colors,
            "SIZE": SIZE,
            "size": size,
            "title": title,
            "square": square,
        },
    )
