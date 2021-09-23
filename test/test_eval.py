from ltsp_test import *
import random as rnd

builtin_tests = [
    PexTest(
        "Eval car on simple list",
        [pair("(car (a b c))", "a")],
    ),
]
