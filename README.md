#### Hexlet tests and linter status:
[![Actions Status](https://github.com/Onoiro/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Onoiro/python-project-50/actions)

![gendiff workflow](https://github.com/Onoiro/python-project-50/actions/workflows/gendiff-check.yml/badge.svg)

[![Maintainability](https://api.codeclimate.com/v1/badges/705776fbe38db666259d/maintainability)](https://codeclimate.com/github/Onoiro/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/705776fbe38db666259d/test_coverage)](https://codeclimate.com/github/Onoiro/python-project-50/test_coverage)

## Welcome to the "Detection of Differences"
This CLI utility allows you to compare two *.json or *.yaml files and show the difference.
Such system is used, for example, when outputting tests or when automatically tracking changes in configuration files.

Minimal system requirements:

    Linux or MacOS command line
    Python 3.8 and up installed
    Poetry 1.2.2 and up installed
    Pip 22.2.1 and up installed

To install Detection of Differences:

    git clone git@github.com:Onoiro/python-project-50.git
    poetry install
    make build
    make publish
    make package-install

To uninstall Detection of Differences:

    python3 -m pip uninstall hexlet-code

To run and use Detection of Differences:

    gendiff [-h] [-f FORMAT] filepath1 filepath2

        positional arguments:
        filepath1
        filepath2

        optional arguments:
        -h, --help            show this help message and exit
        -f FORMAT, --format FORMAT       set format of output

        format types:
        stylish (is used by default)
        plain
        json


#### How how to use help and compare two *.json files
[![asciicast](https://asciinema.org/a/qQZAaGhHVzzE5uvDKZ1TSmLIZ.svg)](https://asciinema.org/a/qQZAaGhHVzzE5uvDKZ1TSmLIZ)

#### How how to compare two *.yml files
[![asciicast](https://asciinema.org/a/jtOaVgxZ9jG6N50qsdZFJ2LAc.svg)](https://asciinema.org/a/jtOaVgxZ9jG6N50qsdZFJ2LAc)

#### How to compare two files with nested structures
[![asciicast](https://asciinema.org/a/JeLnWtVi1dXjhM22CnTJ2PUFA.svg)](https://asciinema.org/a/JeLnWtVi1dXjhM22CnTJ2PUFA)

#### How to compare two files using plain format
[![asciicast](https://asciinema.org/a/gtfc81MH8J6Y71ubpCY9sOWhl.svg)](https://asciinema.org/a/gtfc81MH8J6Y71ubpCY9sOWhl)

#### How to compare two files using json format
[![asciicast](https://asciinema.org/a/eevZlZcSA6gsHljEXHCe8Vrp6.svg)](https://asciinema.org/a/eevZlZcSA6gsHljEXHCe8Vrp6)
