import numpy as np
from math import gcd

def genQuadraticSimple(xmax=10):
    # Only generate problems with real, rational roots.
    # ~ O(xmax**4) unique questions possible.

    # roots are x = -ksi/beta, x = -chi/alpha.
    alpha,beta,chi,ksi = np.random.randint(-xmax,xmax,4)

    # format: ax^2 + bx + c = 0
    a = alpha * beta
    b = alpha * ksi + beta * chi
    c = chi * ksi

    if a == 0 and b == 0:
        return genQuadraticSimple(xmax)

    outStrings = [] # each string in this list should be a new line on soln sheet.

    # Generate worked solution
    # 1. Write the problem
    outStrings.append(quadStr(a,b,c))   

    # 2. Simplify, if possible
    d = gcd(a,gcd(b,c))
    if d != 1:
        a//=d
        b//=d
        c//=d
        outStrings.append(quadStr(a,b,c) + " [Simplify]")
    
    d = gcd(chi,alpha)
    if d != 1:
        alpha //= d
        chi //= d
    d = gcd (ksi,beta)
    if d != 1:
        ksi //= d
        beta //= d

    # 3. Factorise
    if (alpha !=0 and beta != 0):

        s0 = "%ix"%alpha
        if chi != 0: 
            s0 = "(%s + %i)"%(s0,chi)
        s1 = "%ix"%beta
        if ksi != 0: 
            s1 = "(%s + %i)"%(s1,ksi)

        if ksi == 0: s = eqnClean (s1+s0)+" = 0"
        else: s = eqnClean (s0+s1)+" = 0"
        outStrings.append(s + " [Factorise]")

    # 4. Write the answer(s)    
    if chi == 0 and alpha != 0: outStrings.append("x = 0")
    elif not (chi == 0 or alpha == 0): 
        if chi*alpha > 0 : sgn = "-"
        else: sgn = ""
        outStrings.append(eqnClean ("x = %s%i/%i"%(sgn,abs(chi),abs(alpha))))
    if ksi == 0 and beta != 0: outStrings.append("x = 0")
    elif not (ksi == 0 or beta == 0): 
        if ksi*beta > 0 : sgn = "-"
        else: sgn = ""
        outStrings.append(eqnClean ("x = %s%i/%i"%(sgn,abs(ksi),abs(beta))))

    return outStrings

def quadStr(a,b,c):
    s = ""
    if a!=0: s+= "%ix^2"%a
    if b!=0: s+= " + %ix"%b
    if c!=0: s+= " + %i"%c
    return eqnClean(s) + " = 0"

def eqnClean(s):
    # Attempt to remove silly notation. Specifically:
    #   ++, --, +-, -+, x/1, 1x
    # Not quite general enough for arbitrary cases (yet?).
    # Does not cleanup zeroes e.g. +0x^2 etc. (yet?)
    # TODO: This is a bit hacky atm, make it not so.
    # TODO: If generalised, move to utils.py (or equivalent)

    s0 = s.strip()
    if s == "": return s
    s = list(s0)

    if s[0] == "+": # e.g. +4x --> 4x
        s[0] = ""
    if s[0] == "-":
        # move - beside next non-space char (e.g. - 4x --> -4x)
        i=1
        while s[i] in " ":
            s[i] = ""
            i+=1
            break
    i = 0
    while i < len(s)-1:
        
        j = i + 1

        if s[i] == " " and s[i+1] == " ":
            s[i] = ""

        elif s[i] == "/" and s[i+1] == "1":
            # e.g. we have x/1
            s[i] = ""
            s[j] = ""

        elif s[i] == "1" and not s[i+1] in " =*/+-0123456789)(":
            # e.g. we have 1x
            if i==0 or  (i > 0 and s[i-1] not in "123456789"):
                s[i] = ""

        elif s[i] == "+":
            while j < len(s):
                if s[j] == " " or s[j] == "":
                    j+=1
                    continue
                if s[j] == "-":
                    s[i] = "-"
                    s[j] = ""
                    i -= 1
                    break
                if s[j] == "+":
                    s[j] = ""
                    break
                break

        elif s[i] == "-":
            while j < len(s):
                if s[j] == " " or s[j] == "":
                    j+=1
                    continue
                if s[j] == "-":
                    s[i] = ""
                    s[j] = "+"
                    break
                if s[j] == "+":
                    s[i] = ""
                    s[j] = "-"
                    break
                break
            else: break
        i+=1
    s = "".join(s).strip()
    if s0 == s: return s
    return eqnClean(s) # rerun until no changes made