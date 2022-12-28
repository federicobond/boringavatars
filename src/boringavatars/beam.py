from .utils import (
    hash_code,
    get_boolean,
    get_contrast,
    get_random_color,
    get_unit,
    render,
)

SIZE = 36


def generate_data(name, colors):
    num_from_name = hash_code(name)
    wrapper_color = get_random_color(num_from_name, colors, len(colors))
    pre_translate_x = get_unit(num_from_name, 10, 1)
    wrapper_translate_x = (
        pre_translate_x + SIZE / 9 if pre_translate_x < 5 else pre_translate_x
    )
    pre_translate_y = get_unit(num_from_name, 10, 2)
    wrapper_translate_y = (
        pre_translate_y + SIZE / 9 if pre_translate_y < 5 else pre_translate_y
    )

    return {
        "wrapper_color": wrapper_color,
        "face_color": get_contrast(wrapper_color),
        "background_color": get_random_color(num_from_name + 13, colors, len(colors)),
        "wrapper_translate_x": wrapper_translate_x,
        "wrapper_translate_y": wrapper_translate_y,
        "wrapper_rotate": get_unit(num_from_name, 360),
        "wrapper_scale": 1 + get_unit(num_from_name, SIZE / 12) / 10,
        "is_mouth_open": get_boolean(num_from_name, 2),
        "is_circle": get_boolean(num_from_name, 1),
        "eye_spread": get_unit(num_from_name, 5),
        "mouth_spread": get_unit(num_from_name, 3),
        "face_rotate": get_unit(num_from_name, 10, 3),
        "face_translate_x": wrapper_translate_x / 2
        if wrapper_translate_x > SIZE / 6
        else get_unit(num_from_name, 8, 1),
        "face_translate_y": wrapper_translate_y / 2
        if wrapper_translate_y > SIZE / 6
        else get_unit(num_from_name, 7, 2),
    }


def beam(name, *, colors, size, title, square):
    context = generate_data(name, colors)
    context["name"] = name
    context["SIZE"] = SIZE
    context["size"] = size
    context["title"] = title
    context["square"] = square
    return render("beam.svg", context)
