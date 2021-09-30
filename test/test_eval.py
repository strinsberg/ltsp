from ltsp_test import *


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
    PexTest(
        "Recursive lambda",
        [pair("(define f (lambda (a)"
                        + "(cond ((eq? a NIL) NIL)"
                              + "(T (cons 1 (f (cdr a)))))))", "T"),
         pair("(f (quote (9 8 7 6 5 4 3 2)))", "(1 1 1 1 1 1 1 1)")],
    ),

    # This was a printing error
    # NIL was not being printed properly in lists
    PexTest(
        "Printing error with NIL literal in a list",
        [pair("(define a 123)", "T"),
         pair("(quote (cons a NIL))", "(cons a NIL)")]
    ),
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
