[![Build Status](https://travis-ci.com/andyfoston/coding_kata.svg?branch=master)](https://travis-ci.com/andyfoston/coding_kata)

# Coding Kata

A script that runs basic arithmetic functions from the command line

## Prerequisites

There are no prerequisites for running this program, however for linting,
building or running in a container, there are some requirements:

  * Docker - Can be used to run the script inside    a container.
  * Make - used as a wrapper for building, linting, testing and running in
    docker
  * Pylint - Required for linting the script

## Running

The script runs calculations from options provided on the command line. To show the available options, run the script with a '-h' flag:
```
$ ./basic_arithmetric -h
usage: basic_arithmetic.py [-h] (-a | -s | -m | -d) operand operand

Performs basic arithmetic on two provided numbers

positional arguments:
  operand         The operands that the arithmetic operation will be applied
                  to

optional arguments:
  -h, --help      show this help message and exit
  -a, --add       Adds the two operands together
  -s, --subtract  Subtracts the second operand from the first
  -m, --multiply  Multiplies the two operands together
  -d, --divide    Divides the first operand by the second operand
```

The formula and result are then printed on the command line.

### Example:

```
$ ./basic_arithmetic.py --add 4 6
4.0 + 6.0 = 10.0
```

## Build

To build a tar.gz package, run the following command:

```
$ make build
```

The file will be written to `./dist/CodingKata-0.1dev.tar.gz`

## Clean

To clean the package artifact, run the following command:

```
$ make clean
```

Alternatively, to also remove coverage files and pyc files, run the following

```
$ make clean-all
```

## Test

The test the script, run one of the following:

```
$ make test # Runs the test suite
$ make lint # Lints the main script
$ make test-coverage # Runs the tests and prints a coverage report
```

## Run in docker

Use the following to build a docker container and run the script in a container with provided the arguments:

```
make docker-run ARGS="--add 4 5"
```
