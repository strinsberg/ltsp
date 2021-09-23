from ltsp_test import *
import random as rnd

symbol_tests = [
    PexTest(
        "Test reading a single 2 character symbol",
        [pair("hi")],
    ),
    PexTest(
        "Test reading a single 6 character symbol",
        [pair("hello!")],
    ),
    PexTest(
        "Test reading a single 8 character symbol",
        [pair("wombat!?")],
    ),
    PexTest(
        "Test reading a single 8+ character symbol",
        [("hello!worldthisissteve", "hello!wo")],
    ),
    PexTest(
        "Test consecutive identical symbols in between others",
        [pair("hi"), pair("there"), pair("hi"), pair("hi"), pair("there"),
         pair("what"), pair("hi"), pair("what"), pair("what")],
    ),

    # white space
    # newlines after the symbol will stop the repl stripping, so anything
    # after them will be read at the next prompt. Since the repl has no
    # readline support this means that it will not be possible to enter
    # manually, but could be sent by something else.
    PexTest(
        "Test reading a symbol surrounded by simple white space",
        [(" , hello!  ,,", "hello!")],
    ),
    PexTest(
        "Test reading a symbol surrounded by white space, tabs",
        [(" \t, hello!\t  ,", "hello!")],
    ),
    PexTest(
        "Test reading a symbol surrounded by white space, newlines",
        [(" , \n hello! \t ,,", "hello!")],
    ),
    PexTest(
        "Test reading multiple symbols separated by a newline",
        [("hello!\n World!", "hello!"), ("", "World!")],
    ),

    # stopping chars
    PexTest(
        "Test reading a symbol ended by space",
        [("hello! ", "hello!")],
    ),
    PexTest(
        "Test reading a symbol ended by newline",
        [("hello!\n", "hello!")],
    ),
    PexTest(
        "Test reading a symbol ended by tab",
        [("hello!\t", "hello!")],
    ),
    PexTest(
        "Test reading a symbol ended by ,",
        [("hello!,", "hello!")],
    ),
    PexTest(
        "Test reading a symbol ended by (",
        [("hello!(", "hello!")],
    ),
    PexTest(
        "Test reading a symbol ended by )",
        [("hello!)", "hello!")],
    ),
]

list_tests = [
    PexTest(
        "The empty list",
        [("()", "NIL")],
    ),
    PexTest(
        "Single level list",
        [pair("(a b 123)")],
    ),
    PexTest(
        "List with consecutive identical symbols",
        [pair("(a a a b a a b b b a c s)")],
    ),
    PexTest(
        "List with a list element",
        [pair("(a (b) 123)")],
    ),
    PexTest(
        "Tree nested list",
        [pair("(a (b (c) (d)) (e (f (g (h)))))")],
    ),
]

number_tests = [
    PexTest(
        "Positive integer",
        [pair("123")],
    ),
    PexTest(
        "Positive integer, explicit sign",
        [("+123", "123")],
    ),
    PexTest(
        "Negative integer",
        [pair("-123")],
    ),
    PexTest(
        "Positive fixed point",
        [pair("123.567")],
    ),
    PexTest(
        "Positive fixed point, 2 significant digits",
        [("123.56", "123.560")],
    ),
    PexTest(
        "Positive fixed point, 1 significant digits",
        [("123.5", "123.500")],
    ),
    PexTest(
        "Positive fixed point, explicit sign",
        [("+123.789", "123.789")],
    ),
    PexTest(
        "Negative fixed point",
        [pair("-123.432")],
    ),
]
