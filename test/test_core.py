from ltsp_test import *

arithmetic_tests = [
    # add
    PexTest(
        "Add two integers",
        [pair("(add 123467 98765)", "222232")],
    ),
    PexTest(
        "Add multiple integers",
        [pair("(add 1 2 3 4 5)", "15")],
    ),
    PexTest(
        "Add two integers, negative",
        [pair("(add -123467 -98765)", "-222232")],
    ),
    PexTest(
        "Add two fixed point",
        [pair("(add 123.467 987.65)", "1111.117")],
    ),
    PexTest(
        "Add two fixed point, negative",
        [pair("(add -123.467 -987.65)", "-1111.117")],
    ),
    PexTest(
        "Add multiple integers and fixed",
        [pair("(add 1 2 3.1 4 5)", "15.100")],
    ),
    PexTest(
        "Add when there is a non number in the list, integers",
        [pair("(add 123467 98765 (quote a))", "ERROR")],
    ),
    PexTest(
        "Add when there is a non number in the list, fixed",
        [pair("(add -123.46 98.765 (quote a))", "ERROR")],
    ),

]