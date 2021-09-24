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

    # Atom?
    PexTest(
        "A quoted symbol is an atom",
        [pair("(atom? (quote a))", "T")],
    ),
    PexTest(
        "An integer is an atom",
        [pair("(atom? 1237)", "T")],
    ),
    PexTest(
        "A fixed point number is an atom",
        [pair("(atom? 12.37)", "T")],
    ),
    PexTest(
        "Nil is an atom",
        [pair("(atom? NIL)", "T")],
    ),
    PexTest(
        "A dotted pair is NOT an atom",
        [pair("(atom? (cons a b))", "F")],
    ),
    PexTest(
        "A list is not an atom",
        [pair("(atom? (cons a (quote b c)))", "F")],
    ),

    # Eq? Only works on symbols and ints, not lists.
    PexTest(
        "Check if two symbols are eq? T",
        [pair("(eq? (quote a) (quote a))", "T")],
    ),
    PexTest(
        "Check if two symbols are eq? F",
        [pair("(eq? (quote a) (quote b))", "F")],
    ),
    PexTest(
        "Check if a symbol eq? a number F",
        [pair("(eq? (quote a) 1234)", "F")],
    ),
    PexTest(
        "Check if a symbol eq? a list, F",
        [pair("(eq? (quote a) (quote (a)))", "F")],
    ),
    PexTest(
        "Check if a list eq? a list, F",
        [pair("(eq? (quote (a)) (quote (a)))", "F")],
    ),
    PexTest(
        "Check if two ints are eq? T",
        [pair("(eq? 1234 1234)", "T")],
    ),
    PexTest(
        "Check if two negative ints are eq? T",
        [pair("(eq? -1234 -1234)", "T")],
    ),
    PexTest(
        "Check if two ints are eq? F",
        [pair("(eq? 1234 6432)", "F")],
    ),
    PexTest(
        "Check if two fixed point are eq? T",
        [pair("(eq? 12.34 12.340)", "T")],
    ),
    PexTest(
        "Check if two negative fixed point are eq? T",
        [pair("(eq? -12.34 -12.340)", "T")],
    ),
    PexTest(
        "Check if two fixed point are eq? F",
        [pair("(eq? 12.34 1.234)", "F")],
    ),
    PexTest(
        "Check if an int and a fixed are eq? T",
        [pair("(eq? 1234 1234.000)", "T")],
    ),
    PexTest(
        "Check if a fixed and an int are eq? T",
        [pair("(eq? 1234.000 1234)", "T")],
    ),
    # this test is used because these two numbers have the same internal
    # representation with fixed point scaling
    PexTest(
        "Check if an int and a fixed are eq? F",
        [pair("(eq? 1234 1.234)", "F")],
    ),
    PexTest(
        "Check if a fixed and an int are eq? F",
        [pair("(eq? 1.234 1234)", "F")],
    ),
]
