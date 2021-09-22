ASM_FILE= ltsp.lta
TEST_RUNNER= test/runner.lta
CFILE= ltsp.c
TEST_CFILE= test.c
PROGRAM=ltsp
DEBUG=ltsp-debug
TEST=ltsp-test

LTASM= lt64-asm-0.0.3-4.jar
ASM_FLAGS= -c $(CFILE)
ASM_TEST_FLAGS= -c $(TEST_CFILE)

RELEASE_FLAGS= -o $(PROGRAM) -O3
DEBUG_FLAGS= -o $(DEBUG) -D DEBUG
TEST_FLAGS= -o $(TEST)
DEBUG_TEST_FLAGS= $(TEST_FLAGS) -D DEBUG


.PHONY: release
release: clean
	java -jar $(LTASM) $(ASM_FILE) $(ASM_FLAGS)
	gcc $(CFILE) $(RELEASE_FLAGS)

.PHONY: debug
debug: clean
	java -jar $(LTASM) $(ASM_FILE) $(ASM_FLAGS)
	gcc $(CFILE) $(DEBUG_FLAGS)

.PHONY: tests
tests: release
	python3 test/cli_runner.py

.PHONY: lta-tests
lta-tests: clean
	java -jar $(LTASM) $(TEST_RUNNER) $(ASM_TEST_FLAGS)
	gcc $(TEST_CFILE) $(TEST_FLAGS)
	./$(TEST)

.PHONY: clean
clean:
	rm -rf $(PROGRAM) $(DEBUG) $(TEST) $(CFILE) $(TEST_CFILE) *.c
