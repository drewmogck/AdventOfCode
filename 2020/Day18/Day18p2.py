# -*- coding: utf-8 -*-
"""
Advent of Code 2020
Day 18 part 2
Code borrowed from the solutions thread on Reddit
"""

import re

def EvaluateAddBeforeMul(equation):
    while ("+" in equation):
        priorty_eval = re.findall(r"\d+ [\+ \d+| \+ \d+]+", equation)
        for to_eval in priorty_eval:
            equation = equation.replace(to_eval, str(eval(to_eval)))
    return eval(equation)

def EvaluateSamePriority(equation):
    while ("+" in equation) or ("*" in equation):
        to_eval = re.findall(r"^(\d+ [\*\+] \d+)", equation)[0]
        equation = str(eval(to_eval)) + equation[len(to_eval):]
    return int(equation)

def Calculate(equation, eval_func):
    while equation.count("("):
        priorty_eval = re.findall(r"\(\d+ [\*\+] [\d+|\d+ \[\*\+\] \d+]+\)", equation)
        for to_eval in priorty_eval:
            equation = equation.replace(to_eval, str(eval_func(to_eval[1:-1])))

    return eval_func(equation)

if __name__ == "__main__":
    with open("Day18.txt") as f:
        equations = f.readlines()

    ans_same_priority = [Calculate(equation, EvaluateSamePriority)
                         for equation in equations]
    print("Part 1:", sum(ans_same_priority))

    ans_add_before_mul = [Calculate(equation, EvaluateAddBeforeMul)
                         for equation in equations]
    print("Part 2:", sum(ans_add_before_mul))