
# Boring Avatars

boringavatars is a Python port of the <a href="https://www.npmjs.com/package/boring-avatars">boring-avatars</a> JS library.

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
