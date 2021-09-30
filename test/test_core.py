from ltsp_test import *

elementary_tests = [
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
        [pair("(car (quote a))", "NIL")],
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
        [pair("(cdr (quote a))", "NIL")],
    ),
    PexTest(
        "eval cdr on empty list",
        [pair("(cdr (quote ()))", "NIL")],
    ),

    # Cons
    PexTest(
        "eval cons on a symbol and list",
        [pair("(cons (quote a) (quote (b c)))", "(a b c)")],
    ),
    PexTest(
        "eval cons on a list and list",
        [pair("(cons (quote (a)) (quote (b c)))", "((a) b c)")],
    ),
    PexTest(
        "eval cons on two symbols",
        [pair("(cons (quote a) (quote b))", "(a . b)")],
    ),
    PexTest(
        "eval cons symbol onto cons list",
        [pair("(cons (quote a) (cons (quote b) (quote (c d))))", "(a b c d)")],
    ),
    PexTest(
        "eval cons symbol onto dotted pair two symbols",
        [pair("(cons(quote a)(cons (quote b)(quote  c)))", "(a b c)")],
    ),
    PexTest(
        "eval cons on a symbol onto NIL",
        [pair("(cons (quote a) NIL)", "(a)")],
    ),
    PexTest(
        "eval cons on a symbol onto empty list",
        [pair("(cons (quote a) (quote ()))", "(a)")],
    ),
    PexTest(
        "eval cons on a symbol onto unquoted empty list",
        [pair("(cons (quote a) ())", "(a)")],
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
        [pair("(atom? (cons (quote a) (quote b)))", "F")],
    ),
    PexTest(
        "A list is not an atom",
        [pair("(atom? (cons (quote a) (quote (b c))))", "F")],
    ),

    # Eq? Only works on symbols and ints, not lists.
    PexTest(
        "Check if two symbols are eq? T",
        [pair("(eq? (quote a) (quote a))", "T")],
    ),
    PexTest(
        "Check if two long symbols are eq? T",
        [pair("(eq? (quote abcdefgh) (quote abcdefgh))", "T")],
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

    # div
    PexTest(
        "Divide two integers",
        [pair("(div 300000 300)", "1000")],
    ),
    PexTest(
        "Divide multiple integers",
        [pair("(div 16 2 2 2 2)", "1")],
    ),
    PexTest(
        "Divide two integers, one negative",
        [pair("(div -300000 300)", "-1000")],
    ),
    PexTest(
        "Divide two integers, both negative",
        [pair("(div -300000 -300)", "1000")],
    ),
    PexTest(
        "Divide two integers, with truncated remainder",
        [pair("(div 15 4)", "3")],
    ),
    PexTest(
        "Divide two fixed point",
        [pair("(div 15.0 4.0)", "3.750")],
    ),
    PexTest(
        "Divide two fixed point, one negative",
        [pair("(div 16.793 -3.123)", "-5.377")],
    ),
    PexTest(
        "Divide two fixed point, both negative",
        [pair("(div -16.793 -3.123)", "5.377")],
    ),
    PexTest(
        "Divide multiple integers and fixed",
        [pair("(div 16 2.1 2 2)", "1.904")],
    ),
    PexTest(
        "Divide when there is a non number in the list, integers",
        [pair("(div 123467 98765 (quote a))", "ERROR")],
    ),
    PexTest(
        "Divide when there is a non number in the list, fixed",
        [pair("(div -123.46 98.765 (quote a))", "ERROR")],
    ),
]

functional_tests = [
    # map
    PexTest(
        "Map a builtin subroutine over a list",
        [pair("(map atom? (quote (1 2 3 (4) 5 6)))",
              "(T T T F T T)")]
    ),
    PexTest(
        "Map a lambda over a list",
        [pair("(map (lambda (a) (add a 1)) (quote (1 2 3 4 5 6)))",
              "(2 3 4 5 6 7)")]
    ),
    PexTest(
        "Map a defined lambda over a list",
        [pair("(define sub1 (lambda (a) (sub a 1)))", "T"),
         pair("(map sub1 (quote (1 2 3 4 5 6)))",
              "(0 1 2 3 4 5)")]
    ),

    # filter
    PexTest(
        "Filter a list with a builtin subroutine",
        [pair("(filter atom? (quote (1 2 (3) 4 (5 6))))",
              "(1 2 4)")]
    ),
    PexTest(
        "Filter a list with a builtin subroutine, no matches",
        [pair("(filter atom? (quote ((3) (5 6))))",
              "NIL")]
    ),
    PexTest(
        "Filter a list with a builtin subroutine, empty list",
        [pair("(filter atom? (quote ()))",
              "NIL")]
    ),
    PexTest(
        "Filter a list with a lambda",
        [pair("(filter (lambda (a) (eq? a 4)) (quote (1 2 3 4 5 6)))",
              "(4)")]
    ),
    PexTest(
        "Filter a list with a defined lambda",
        [pair("(define is2 (lambda (a) (eq? a 2)))", "T"),
         pair("(filter is2 (quote (1 2 3 4 2 6)))",
              "(2 2)")]
    ),
]
