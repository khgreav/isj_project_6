#!/usr/bin/env python3

import itertools

def first_nonrepeating(item):
    """Function that returns the first nonrepeating character in a string."""
    if not type(item) == str:
        return None
    spec = [' ', '\n', '\r', '\e', '\f', '\s', '\t', '\v']
    if item in spec:
        return None
    strdict = {}
    for c in item:
        if c in strdict.keys():
            strdict[c] += 1
        else:
            strdict.update({c: 1})
    for k, v in strdict.items():
        if v == 1:
            return k
    return None


def combine4(numlist, res):
    """Function that produces unique mathematic formulas
    from numbers in numlist that equal to number res."""
    if not type(numlist) == list:
        raise TypeError("First argument is not a list.")

    if not len(numlist) == 4:
        raise Exception("List of numbers does not have 4 members.")

    for num in numlist:
        if not type(num) == int:
            raise TypeError("List contains non-numerical characters.")
        if num < 1:
            return []
    if not type(res) == int:
        raise TypeError("Second argument is not an integer.")

    nums = list(itertools.permutations(numlist, 4))
    ops = list(itertools.product('+-*/', repeat=3))

    formulas = []  # list containing formulas comprised of numbers and operations
    for num in nums:
        for op in ops:
            formulas.append(str(num[0])+op[0]+str(num[1])+op[1]+str(num[2])+op[2]+str(num[3]))

    bformulas = []  # list containing formulas with brackets
    for f in formulas:  # a-b-c-d
        for i in range(10):
            if i == 0:  # (a+b)+c+d
                bformulas.append("("+f[:3]+")"+f[3:])
            elif i == 1:  # a+(b+c)+d
                bformulas.append(f[:2]+"("+f[2:5]+")"+f[5:])
            elif i == 2:  # a+b+(c+d)
                bformulas.append(f[:4]+"("+f[4:]+")")
            elif i == 3:  # (a+b)+(c+d)
                bformulas.append("("+f[:3]+")"+f[3:4]+"("+f[4:]+")")
            elif i == 4:  # (a+b+c)+d
                bformulas.append("("+f[:5]+")"+f[5:])
            elif i == 5:  # ((a+b)+c)+d
                bformulas.append("(("+f[:3]+")"+f[3:5]+")"+f[5:])
            elif i == 6:  # (a+(b+c))+d
                bformulas.append("("+f[:2]+"("+f[2:5]+"))"+f[5:])
            elif i == 7:  # a+(b+c+d)
                bformulas.append(f[:2]+"("+f[2:]+")")
            elif i == 8:  # a+((b+c)+d)
                bformulas.append(f[:2]+"(("+f[2:5]+")"+f[5:]+")")
            elif i == 9:  # a+(b+(c+d))
                bformulas.append(f[:2]+"("+f[2:4]+"("+f[4:7]+"))")

    results = []  # list containing formulas that are equal to the specified result
    for bformula in bformulas:
        try:
           result = eval(bformula)
        except ZeroDivisionError:  # divison by zero
            continue
        if result == res:
            results.append(bformula)

    return sorted(set(results))
