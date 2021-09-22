import ltsp_test as lt
import random as rnd

def rnd_symbol():
    symbol = []
    length = rnd.randint(1, 10)
    for i in range(length):
        symbol.append(chr(rnd.randint(ord("a"), ord("z"))))
    return "".join(symbol)

def sym_pair():
    s = rnd_symbol()
    return (s, s[:6])

def rnd_syms(n):
    return [sym_pair() for _ in range(n)]

def pair(text):
    return (text, text)

def rnd_lisp_list():
    length = rnd.randint(1, 20)
    send = []
    expect = []
    for i in range(length):
        pair = sym_pair()
        send.append(pair[0])
        expect.append(pair[1])
    a = "(" + " ".join(send) + ")"
    b = "(" + " ".join(expect) + ")"
    return (a, b)

def rnd_lists(n):
    return [rnd_lisp_list() for _ in range(n)]

symbol_tests = [
    lt.PexTest(
        "Test reading a single 2 character symbol",
        [pair("hi")],
    ),
    lt.PexTest(
        "Test reading a single 6 character symbol",
        [pair("hello!")],
    ),
    lt.PexTest(
        "Test reading a single 6+ character symbol",
        [("hello!worldthisissteve", "hello!")],
    ),
    lt.PexTest(
        "Test consecutive identical symbols in between others",
        [pair("hi"), pair("there"), pair("hi"), pair("hi"), pair("there"),
         pair("what"), pair("hi"), pair("what"), pair("what")],
    ),
]

list_tests = [
    lt.PexTest(
        "Test list with nothing",
        [pair("(a a a b a a b b b a c s)")],
    ),
    lt.PexTest(
        "Test list with consecutive identical symbols",
        [pair("(a a a b a a b b b a c s)")],
    ),

]
