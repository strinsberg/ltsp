from clitest import *
import ltsp_test as lt
import test_reader as read
import test_eval as ev

test_suites = [
    lt.LtspSuite("Reading Symbols", read.symbol_tests),
    lt.LtspSuite("Reading Lists", read.list_tests),
    lt.LtspSuite("Reading Numbers", read.number_tests),
    lt.LtspSuite("Eval Builtin Functions", ev.builtin_tests),
]


# run tests
run_test_suites(test_suites)
