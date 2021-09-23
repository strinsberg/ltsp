from ltsp_test import *
import random as rnd

builtin_tests = [
    PexTest(
        "Eval car on simple list",
        [pair("(car (quote (a b c)))", "a")],
    ),
    PexTest(
        "Eval car on nested list list",
        [pair("(car (quote ((a b (x) c) f)))", "(a b (x) c)")],
    ),
    PexTest(
        "Eval car on nested list list",
        [pair("(car (car (quote ((y) b x c))))", "y")],
    ),
]
