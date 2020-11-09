# Ved Archi Library
Simple REST API wrapper for https://ved.archi/

## Installation

```bash
$ git clone https://github.com/blazewashere/vedarchi-py
$ cd vedarchi-py
$ python3 setup.py install
```

## Usage

```py
    from archi import Archi

    archi = Archi()

    print(archi.lists())
    print(archi.lists("LYOCTRgrJPzDfter"))
    print(archi.donations())
```

## Other Langs

C++ -> [Ved Archi](https://github.com/blazewashere/vedarchi)

## Requirements

Requires [Requests](https://pypi.org/project/requests/)

`setup.py` should install the requirements automatically, if it does not then run:

```bash
$ pip3 install requests
```

## License

[MIT](https://github.com/BlazeWasHere/vedarchi-py/blob/main/LICENSE)