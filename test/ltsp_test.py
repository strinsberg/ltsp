import clitest as cli
import pexpect as pex
import sys


# Test and Suite classes #####################################################

class LtspSuite(cli.TestSuite):
    def __init__(self, name, tests):
        super().__init__(name, "./ltsp", tests)

    def execute(self):
        timed = "Timed Out: "
        eof = "EOF: "

        for i, test in enumerate(self.tests):
            repl = pex.spawn(self.command)
            passed = self.expect_prompt(repl, test, "Start: ", timed, eof)

            for j, action in enumerate(test.input):
                act = f"Action {j+1}: "
                if not passed:
                    break
                repl.sendline(action[0])
                # to clear the sent text from the buffer
                # this should never fail
                if not self.expect_action(action[0], repl, test, "", timed, eof):
                    test.expected = f"Send {j+1}: To find sent text in buffer"
                    passed = False
                    break
                if not self.expect_action(action[1], repl, test,
                                          f'Action {j+1}:', timed, eof):
                    passed = False
                    break
                passed = self.expect_prompt(repl, test, f'Prompt {j+1}',
                                            timed, eof)

            cli.display_test_results(test, passed, i+1, False)
            if not passed:
                self.failed.append((i+1, test))

    def expect_prompt(self, repl, test, act, timed, eof):
        prompt = "ltsp> "
        prompt_idx = repl.expect_exact([prompt.replace("\n", "\r\n"),
                                        pex.EOF, pex.TIMEOUT],
                                       timeout=test.prompt_timeout)
        test.expected = act + f'"{prompt}"'
        if prompt_idx == 1:
            test.actual = eof + f'"{repl.before.decode("ascii")}"'
            return False
        elif prompt_idx == 2:
            test.actual = timed + f'"{repl.before.decode("ascii")}"'
            return False
        return True

    def expect_action(self, action, repl, test, act, timed, eof):
        exp_idx = repl.expect_exact([action.replace("\n", "\r\n"),
                                     pex.EOF, pex.TIMEOUT],
                                    timeout=test.timeout)
        test.expected = act + f'"{action}"'
        if exp_idx == 1:
            test.actual = eof + f'"{repl.before.decode("ascii")}"'
            return False
        elif exp_idx == 2:
            test.actual = timed + f'"{repl.before.decode("ascii")}"'
            return False
        return True

class PexTest(cli.Test):
    def __init__(self, name, actions, timeout=0.2, prompt_timeout=0.2):
        super().__init__(name, actions, expected="")
        self.timeout = timeout
        self.prompt_timeout = prompt_timeout


# Helpers ####################################################################
def rnd_symbol():
    symbol = []
    length = rnd.randint(1, 10)
    for i in range(length):
        symbol.append(chr(rnd.randint(ord("a"), ord("z"))))
    return "".join(symbol)

def sym_pair():
    s = rnd_symbol()
    return pair(s, s[:6])

def rnd_syms(n):
    return [sym_pair() for _ in range(n)]

def out(text):
    return f'\n{text}\n'

def pair(inp, outp=None):
    if not outp:
        outp = inp
    return (inp, out(outp))

def quoted(text):
    return pair(f"(quote {text})", text)

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
