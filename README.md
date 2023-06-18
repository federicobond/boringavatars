
# Boring Avatars

boringavatars is a Python port of the <a href="https://www.npmjs.com/package/boring-avatars">boring-avatars</a> JS library.

![Build Status](https://github.com/federicobond/boringavatars/actions/workflows/python-package.yml/badge.svg?branch=main)
[![Supported Versions](https://img.shields.io/pypi/pyversions/boringavatars.svg)](https://pypi.python.org/pypi/boringavatars)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Install

```
pip install boringavatars
```

## Usage

```python
from boringavatars import avatar

# returns the string corresponding to the generated SVG
avatar(
    "Maria Mitchell",
    variant="marble",
    colors=["92A1C6", "146A7C", "F0AB3D", "C271B4", "C20D90"],
    title=False,
    size=40,
    square=True,
)
```

## License

MIT
