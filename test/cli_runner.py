from clitest import *
import ltsp_test as lt
import test_reader as read

test_suites = [
    lt.LtspSuite("Handles Symbols", read.symbol_tests),
    lt.LtspSuite("Handles Lists", read.list_tests)
]


# run tests
run_test_suites(test_suites)
