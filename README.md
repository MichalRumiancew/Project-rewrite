# Project rewrite

## Story

This kind of exercise is a classic: your task is to reimplement some basic
built-in functionalities of a language or its standard library for pedagogical
reasons without using built-in functionalities or the standard library itself.
Caveat: don’t use such code in your commercial projects!

## What are you going to learn?

You will practice the basics of the language while getting familiar with a few
simple algorithms.

## Tasks

1. Implement the `min(x, y)` function for two real numbers as inputs!
    - For any two real numbers the less is returned
    - No built-in functions are used

2. Implement the `max(values_list)` function for a list of numbers!
    - For any list of real numbers the greatest is returned
    - No built-in functions are used

3. Implement the `len(values_list)` function for a list of numbers or strings which returns the length of the list!
    - For any list the count of the elements is returned
    - No built-in functions are used

4. Implement the `multiply(x, y)` function for integer numbers as inputs! Do not use the `*`, `/`, and `//` operators and any built-in functions, but you may (and should) use `+`.
    - For any two integer inputs the returned value equals the result of `x * y`
    - Neither `*`, `/`, `//` nor any built-in functions are used

5. Implement the `pow(x, y)` function for real base numbers and positive integer exponents! Do not use the `**` operator and any built-in functions! Here you can use `*`.
    - For inputs from the specified domain the returned value equals the result of `x**y`
    - Neither `**` nor any built-in functions are used

6. [OPTIONAL] Implement the `divmod(x, y)` function for for two integer numbers as inputs! Do not use the `//` and the `%` operators and any built-in functions! It should return a tuple: the first value should be equal to the value of `x // y` and the second equal to the value of `x % y`! Do not use the `//` operator and any built-in functions!
    - For any two positive integer inputs the returned value equals `(x // y, x % y)`
    - For any two +/- integer inputs the returned value equals `(x // y, x % y)`
    - Neither `//` nor any built-in functions are used

## General requirements

- In general, do not use any built-in functions!

## Hints

- How to look for an greatest value in a list?
  Iterate through the list.
  Keep track of a greatest value by storing it in a variable.
  Compare the variable at every iteration with the current list element.
  If the variable is smaller than the current list element - replace it.
  At the end of the loop it will hold the answer.
- To get a length, you can iterate and count.
- Integer multiplication is basicly addition a given number of times.
- An integer power function is basicly multiplication a given number of times.
- How can you divide and calulate modulo _without_ actually dividing?
  Try to add up numbers until you reach the goal! We'll test only with
  not too large numbers (between `-100` and `100`).
  Also, reproducing integer division can be tricky; as you can read in the
  [documentation](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex),
  "The result is always rounded towards minus infinity:
  `1//2` is `0`, `(-1)//2` is `-1`, `1//(-2)` is `-1`, and `(-1)//(-2)` is `0`."

## Starting your project

To start your project click [this link](https://journey.code.cool/v2/project/solo/blueprint/project-rewrite/python).

## Background materials

- <i class="far fa-exclamation"></i> [Numbers](../pages/python/numbers.md)
- <i class="far fa-exclamation"></i> [Control structures](../pages/python/control-structures.md)
- <i class="far fa-exclamation"></i> [Functions](../pages/python/functions.md)
