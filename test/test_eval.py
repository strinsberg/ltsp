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
    PexTest(
        "eval car on symbol",
        [pair("(car a)", "NIL")],
    ),
    PexTest(
        "eval cdr on empty list",
        [pair("(car (quote ()))", "NIL")],
    ),

    # Cdr
    PexTest(
        "eval cdr on simple list",
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
    PexTest(
        "eval cdr on symbol",
        [pair("(cdr a)", "NIL")],
    ),
    PexTest(
        "eval cdr on empty list",
        [pair("(cdr (quote ()))", "NIL")],
    ),

    # Cons
    PexTest(
        "eval cons on a symbol and list",
        [pair("(cons a (quote (b c)))", "(a b c)")],
    ),
    PexTest(
        "eval cons on a list and list",
        [pair("(cons (quote (a)) (quote (b c)))", "((a) b c)")],
    ),
    PexTest(
        "eval cons on two symbols",
        [pair("(cons a b)", "(a . b)")],
    ),
    PexTest(
        "eval cons symbol onto cons list",
        [pair("(cons a (cons b (quote (c d))))", "(a b c d)")],
    ),
    PexTest(
        "eval cons symbol onto dotted pair two symbols",
        [pair("(cons a (cons b c))", "(a b c)")],
    ),
    PexTest(
        "eval cons on a symbol onto NIL",
        [pair("(cons a NIL)", "(a)")],
    ),
    PexTest(
        "eval cons on a symbol onto empty list",
        [pair("(cons a (quote ()))", "(a)")],
    ),
    PexTest(
        "eval cons on a symbol onto unquoted empty list",
        [pair("(cons a ())", "(a)")],
    ),

]
