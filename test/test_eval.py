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

special_form_tests = [
    # cond
    PexTest(
        "Simple only T conditional",
        [pair("(cond (T (quote a)))", "a")],
    ),
    PexTest(
        "Simple conditional, take first case",
        [pair("(cond ((eq? 1 1) (quote b)) (T (quote a)))", "b")],
    ),
    PexTest(
        "Simple conditional, take T case",
        [pair("(cond (F (quote b)) (T (quote a)))", "a")],
    ),
    PexTest(
        "Simple conditional using NIL as false, take T case",
        [pair("(cond (NIL (quote b)) (T (quote a)))", "a")],
    ),
    PexTest(
        "Conditional with a few cases, takes the third case as true",
        [pair("(cond ((eq? 2 NIL) NIL)"
                  + "(F 399)"
                  + "((eq? (car (quote (a))) (quote a)) 1234)"
                  + "(T (quote a)))",
              "1234")],
    ),

    # let
    PexTest(
        "Simple let with a single assignment",
        [pair("(let ((a 1)) a)", "1"),
         pair("a", "ERROR")],
    ),
    PexTest(
        "Simple let with two assignments",
        [pair("(let ((a 1) (b 3)) (cons a b))", "(1 . 3)"),
         pair("a", "ERROR"), pair("b", "ERROR")],
    ),
    PexTest(
        "Nested let that uses a binding from the first",
        [pair("(let ((a 1) (b 3)) (let ((c 7)) (cons a (cons b c))))", "(1 3 7)")]
    ),
    PexTest(
        "Nested let that shadows a binding from the first",
        [pair("(let ((a 1) (b 3)) (let ((a 7)) (cons a b)))", "(7 . 3)")]
    ),
    PexTest(
        "Let where bindings use previous bindings",
        [pair("(let ((a 1) (b (cons 2 a)) (c (cons 3 b))) c)", "(3 2 1)")]
    ),

    # lambda
    PexTest(
        "Simple lambda creation, returns a procedure",
        [pair("(lambda (a b) (cons a b))", "#((a b) (cons a b))")],
    ),
    PexTest(
        "Simple lambda creation and application",
        [pair("(define f (lambda (a b) (cons a b)))", "T"),
         pair("(f 1 2)", "(1 . 2)"),
         ],
    ),
    PexTest(
        "Simple lambda creation and application, with result saved",
        [pair("(define f (lambda (a b) (cons a b)))", "T"),
         pair("(define a (f 1 2))","T"),
         pair("a","(1 . 2)"),
         ],
    ),
    PexTest(
        "Lambda returns a lambda with a closure on its params, apply it",
        [pair("(define f (lambda (a b) (lambda (x) (cons x (cons a b)))))", "T"),
         pair("(define g (f 2 3))", "T"),
         pair("(g 1)", "(1 2 3)"),
         ],
    ),
    PexTest(
        "Apply a lambda directly",
        [pair("((lambda (a b) (cons a b)) 1 2)", "(1 . 2)")],
    ),
    PexTest(
        "Apply a lambda directly, with args that need evaluation",
        [pair("(define x 1)", "T"),
         pair("(define y 2)", "T"),
         pair("((lambda (a b) (cons a b)) x y)", "(1 . 2)")],
    ),

    # recursion
    # There seems to be no issue with the lambda being recursive, but there
    # is somethign that is not letting the second one run more than a few 
    # times. I have no idea why.
    # There could be some simple recursion tests if there were arithmetic
    # operations, so I need to add a couple of them.
    # Also, one removed iteration of the recursion used (quote ()) instead
    # of NIL and inside a recursive call there was an issue with quote
    # not being defined. This makes no sense since quote is builtin and should
    # be caught as the car of a list to be evaluated separately.
    #PexTest(
        #"Recursive lambda",
        #[pair("(define f (lambda (a) (cons 3 (f a))))", "T"),
         #pair("(f 3)", "(1 1 1 1 1 1 1 1)")],
    #),
    #PexTest(
        #"Recursive lambda",
        #[pair("(define f (lambda (a)"
                        #+ "(cond ((eq? a 888) T)"
                              #+ "(T (cons 1 (f (cdr a)))))))", "T"),
         #pair("(f (quote (9 8 7 6 5 4 3 2)))", "(1 1 1 1 1 1 1 1)")],
    #),

    # ISSUES this is a printing error
    # For some reason having a list with a NIL in the middle will not
    # print properly, whether it is a literal or created by the program.
    #PexTest(
    #    "Printing error with NIL literal in a list",
    #    [pair("(define a 123)", "T"),
    #     pair("(quote (cons a NIL))", "(cons a NIL)")]
    #),
]

symbol_tests = [
    PexTest(
        "Nil evaluates to nil",
        [pair("NIL")]
    ),
    PexTest(
        "T evaluates to T",
        [pair("T")]
    ),
    PexTest(
        "F evaluates to F",
        [pair("F")]
    ),
    PexTest(
        "ERROR evaluates to ERROR",
        [pair("ERROR")]
    ),
    PexTest(
        "Define a symbol",
        [pair("(define a T)", "T")]
    ),
    PexTest(
        "Define a symbol again and it will fail",
        [pair("(define a 888)", "T"),
         pair("(define a 123)", "ERROR"),
         pair("a", "888")]
    ),
    PexTest(
        "Define a symbol with a number as the symbol and it will fail",
         [pair("(define 123 T)", "ERROR")]
    ),
    PexTest(
        "Define a symbol with a list as the symbol and it will fail",
         [pair("(define (quote 123) T)", "ERROR")]
    ),
    PexTest(
        "Define a symbol, and then evaluate it",
        [pair("(define a T)", "T"),
         pair("a", "T")]
    ),
    PexTest(
        "Define a symbol with an function result, and check the result",
        [pair("(define a (cons (quote x) (quote y)))", "T"),
         pair("a", "(x . y)")]
    ),
    PexTest(
        "Define two symbols and then use them",
        [pair("(define a 123)", "T"),
         pair("(define b 456)", "T"),
         pair("(cons a b)", "(123 . 456)")]
    ),

]

"""
"""
