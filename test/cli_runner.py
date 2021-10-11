from clitest import *
import ltsp_test as lt
import test_reader as read
import test_eval as ev
import test_core as core

test_suites = [
    lt.LtspSuite("Reading Symbols", read.symbol_tests),
    lt.LtspSuite("Reading Lists", read.list_tests),
    lt.LtspSuite("Reading Numbers", read.number_tests),
    lt.LtspSuite("Reading Strings", read.string_tests),
    lt.LtspSuite("Eval Symbols", ev.symbol_tests),
    lt.LtspSuite("Eval Special Forms", ev.special_form_tests),
    lt.LtspSuite("Elementary Functions", core.elementary_tests),
    lt.LtspSuite("Core Artithmetic", core.arithmetic_tests),
    lt.LtspSuite("Map Filter Reduce", core.functional_tests),
    lt.LtspSuite("Eval Apply List", core.eval_tests),
    lt.LtspSuite("Core Relational and Boolean", core.rel_bool_tests),
    lt.LtspSuite("Printing", core.printing_tests),
    lt.LtspSuite("String Operations", core.string_tests),
    lt.LtspSuite("List Operations", core.list_tests),
]


# run tests
run_test_suites(test_suites)
