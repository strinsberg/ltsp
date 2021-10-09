from ltsp_test import *
import random as rnd

symbol_tests = [
    PexTest(
        "Test reading a single 2 character symbol",
        [quoted("hi")],
    ),
    PexTest(
        "Test reading a single 6 character symbol",
        [quoted("hello!")],
    ),
    PexTest(
        "Test reading a single 8 character symbol",
        [quoted("wombat!?")],
    ),
    PexTest(
        "Test reading a single 8+ character symbol",
        [pair("(quote hello!worldthisissteve)", "hello!wo")],
    ),
    PexTest(
        "Test consecutive identical symbols in between others",
        [quoted("hi"), quoted("there"), quoted("hi"), quoted("hi"),
         quoted("there"), quoted("what"), quoted("hi"), quoted("what"),
         quoted("what")],
    ),

    # white space
    # newlines after the symbol will stop the repl stripping, so anything
    # after them will be read at the next prompt. Since the repl has no
    # readline support this means that it will not be possible to enter
    # manually, but could be sent by something else.
    PexTest(
        "Test reading a symbol surrounded by simple white space",
        [pair(" , (quote hello!)  ,,", "hello!")],
    ),
    PexTest(
        "Test reading a symbol surrounded by white space, tabs",
        [pair("(quote \t, hello!\t  ,)", "hello!")],
    ),
    PexTest(
        "Test reading a symbol surrounded by white space, newlines",
        [pair("(quote  , \n hello! \t ,,)", "hello!")],
    ),
    PexTest(
        "Test reading multiple symbols separated by a newline",
        [pair("(quote hello!)\n (quote World!)", "hello!"), ("", "World!")],
    ),

    # stopping chars
    PexTest(
        "Test reading a symbol ended by space",
        [pair("(quote hello! )", "hello!")],
    ),
    PexTest(
        "Test reading a symbol ended by newline",
        [pair("(quote hello!\n)", "hello!")],
    ),
    PexTest(
        "Test reading a symbol ended by tab",
        [pair("(quote hello!\t)", "hello!")],
    ),
    PexTest(
        "Test reading a symbol ended by ,",
        [pair("(quote hello!,)", "hello!")],
    ),

    # string
    PexTest(
        "Test reading a string",
        [pair('"Hello, World!"')],
    ),
    PexTest(
        "Test reading an empty string",
        [pair('""')],
    ),
    PexTest(
        "Test reading a string with escaped chars",
        [pair('"\\t\\"hello\\"\\nworld"')],
    ),
]

list_tests = [
    PexTest(
        "The empty list",
        [pair("()", "NIL")],
    ),
    PexTest(
        "Single level list",
        [quoted("(a b 123)")],
    ),
    PexTest(
        "List with consecutive identical symbols",
        [quoted("(a a a b a a b b b a c s)")],
    ),
    PexTest(
        "List with a list element",
        [quoted("(a (b) 123)")],
    ),
    PexTest(
        "Tree nested list",
        [quoted("(a (b (c) (d)) (e (f (g (h)))))")],
    ),
    PexTest(
        "Test reading a quoted list with strings",
        [quoted('("Hello, World!" 234 "I am Steven")')],
    ),
    PexTest(
        "Test reading list with strings",
        [pair('(list "Hello, World!" 234 "I am Steven")',
              '("Hello, World!" 234 "I am Steven")')],
    ),
]

number_tests = [
    PexTest(
        "Positive integer",
        [pair("123")],
    ),
    PexTest(
        "Positive integer, explicit sign",
        [pair("+123", "123")],
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
        [pair("123.56", "123.560")],
    ),
    PexTest(
        "Positive fixed point, 1 significant digits",
        [pair("123.5", "123.500")],
    ),
    PexTest(
        "Positive fixed point, explicit sign",
        [pair("+123.789", "123.789")],
    ),
    PexTest(
        "Negative fixed point",
        [pair("-123.432")],
    ),
]
