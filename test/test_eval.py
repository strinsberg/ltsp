from ltsp_test import *
import random as rnd

builtin_tests = [
    # Car
    PexTest(
        "Eval car on simple list",
        [pair("(car (quote (a b c)))", "a")],
    ),
    PexTest(
        "Eval car on nested list",
        [pair("(car (quote ((a b (x) c) f)))", "(a b (x) c)")],
    ),
    PexTest(
        "Eval car on car of nested list",
        [pair("(car (car (quote ((y) b x c))))", "y")],
    ),

    # Cdr
    PexTest(
        "Eval cdr on simple list",
        [pair("(cdr (quote (a b c)))", "(b c)")],
    ),
    PexTest(
        "Eval cdr on nested list",
        [pair("(cdr (quote ((a b (x) c) f)))", "(f)")],
    ),
    PexTest(
        "Eval cdr on cdr of a list",
        [pair("(cdr (cdr (quote (y x a b c))))", "(a b c)")],
    ),
]
