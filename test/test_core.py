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

    # sub
    PexTest(
        "Subtract two integers",
        [pair("(sub 123467 98765)", "24702")],
    ),
    PexTest(
        "Subtract multiple integers",
        [pair("(sub 1 2 3 4 5)", "-13")],
    ),
    PexTest(
        "Subtract two integers, negative",
        [pair("(sub -123467 -98765)", "-24702")],
    ),
    PexTest(
        "Subtract two fixed point",
        [pair("(sub 123.467 987.65)", "-864.183")],
    ),
    PexTest(
        "Subtract two fixed point, negative",
        [pair("(sub -123.467 -987.65)", "864.183")],
    ),
    PexTest(
        "Subtract multiple integers and fixed",
        [pair("(sub 1 2 3.1 4 5)", "-13.100")],
    ),
    PexTest(
        "Subtract when there is a non number in the list, integers",
        [pair("(sub 123467 98765 (quote a))", "ERROR")],
    ),
    PexTest(
        "Subtract when there is a non number in the list, fixed",
        [pair("(sub -123.46 98.765 (quote a))", "ERROR")],
    ),

    # mult
    PexTest(
        "Multiply two integers",
        [pair("(mult 123 987)", "121401")],
    ),
    PexTest(
        "Multiply multiple integers",
        [pair("(mult 1 2 3 4 5)", "120")],
    ),
    PexTest(
        "Multiply two integers, one negative",
        [pair("(mult -123 987)", "-121401")],
    ),
    PexTest(
        "Multiply two integers, both negative",
        [pair("(mult -123 -987)", "121401")],
    ),
    PexTest(
        "Multiply two fixed point",
        [pair("(mult 123.467 987.65)", "121942.182")],
    ),
    PexTest(
        "Multiply two fixed point, one negative",
        [pair("(mult 123.467 -987.65)", "-121942.182")],
    ),
    PexTest(
        "Multiply two fixed point, both negative",
        [pair("(mult -123.467 -987.65)", "121942.182")],
    ),
    PexTest(
        "Multiply multiple integers and fixed",
        [pair("(mult 1 2 3.12 4 5)", "124.800")],
    ),
    PexTest(
        "Multiply when there is a non number in the list, integers",
        [pair("(mult 123467 98765 (quote a))", "ERROR")],
    ),
    PexTest(
        "Multiply when there is a non number in the list, fixed",
        [pair("(mult -123.46 98.765 (quote a))", "ERROR")],
    ),
]
