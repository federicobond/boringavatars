import hashlib
import math
import os.path

from jinja2 import Environment, FileSystemLoader, select_autoescape


def hash_code(name):
    return int.from_bytes(hashlib.sha1(name.encode("utf-8")).digest(), byteorder="big")


def get_digit(number, ntn):
    return math.floor((number // int(math.pow(10, ntn))) % 10)


def get_boolean(number, ntn):
    return not ((get_digit(number, ntn)) % 2)


def get_angle(x, y):
    return math.atan2(y, x) * 180 / math.pi


def get_unit(number, range, index=None):
    value = number % range

    if index and ((get_digit(number, index) % 2) == 0):
        return -value
    else:
        return value


def get_random_color(number, colors, range):
    return colors[(number) % range]


def get_contrast(hexcolor):
    # If a leading # is provided, remove it
    if hexcolor[0] == "#":
        hexcolor = hexcolor[1:]

    # Convert to RGB value
    r = int(hexcolor[0:2], 16)
    g = int(hexcolor[2:4], 16)
    b = int(hexcolor[4:6], 16)

    # Get YIQ ratio
    yiq = ((r * 299) + (g * 587) + (b * 114)) / 1000

    # Check contrast
    return "#000000" if yiq >= 128 else "#FFFFFF"


template_path = os.path.join(os.path.dirname(__file__), "templates")
env = Environment(
    loader=FileSystemLoader(template_path), autoescape=select_autoescape()
)


def render(template_name, context):
    return env.get_template(template_name).render(context)
