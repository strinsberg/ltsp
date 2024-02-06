# LTSP

A lisp interpreter for the lieutenant-64 virtual machine written in lt64-ams.

**NOTE** As this runs on a "toy" VM it should be obvious that it is not for real world use. Also, if you find it interesting be warned that there are some bugs, and I never did implement any garbage collection for the fixed memory of the VM, so a program can easily run out of memory.

# Purpose

I wanted to make a list interpreter that has to deal with a more low level
language as a target. Now that I have a virtual machine of my own I can use
it for this task. It is not really efficient to have an interpreter that runs
on a VM, but none of this is intended to be used for serious projects. There
are plenty of great lisp/scheme implementations for that already. The goal
here is to learn more about lisp implementation details and have some fun
with my virtual machine.

