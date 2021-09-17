ASM_FILE= ltsp.lta
CFILE= ltsp.c
PROGRAM=ltsp
DEBUG=ltsp-debug

LTASM= lt64-asm-0.0.3.jar
ASM_FLAGS= -c $(CFILE)

RELEASE_FLAGS= -o $(PROGRAM) -O3
DEBUG_FLAGS= -o $(DEBUG) -D DEBUG


.PHONY: release
release:
	java -jar $(LTASM) $(ASM_FILE) $(ASM_FLAGS)
	gcc $(CFILE) $(RELEASE_FLAGS)

.PHONY: debug
debug:
	java -jar $(LTASM) $(ASM_FILE) $(ASM_FLAGS)
	gcc $(CFILE) $(DEBUG_FLAGS)

.PHONY: clean
clean:
	rm -rf $(PROGRAM) $(DEBUG) $(CFILE)
