# Piece Length

Calculate ideal piece length for .torrent files.

Piece Length(`piecelength`) is a simple package that sole purpose is to calculate
the ideal piece length for the Bittorrent protocol based on the total size of
the torrent contents.  Results are returned in integer form, and will always
be a perfect power of 2.

## Install

The `piecelength` package can be installed from git:

```sh
git clone https://github.com/alexpdev/piecelength.git
cd piecelength
pip install .
```

It is also available on PyPi:

```sh
pip install piecelength
```

## Usage

To use the package as library:

```python
from piecelength import piece_length

size = 100000000 # some integer value
result = piece_length(size)
```

It can also be used from the command line:

```sh
piecelength 3456677434645
```

## License

Licensed with BSD 3 see the LICENSE file for more details.
