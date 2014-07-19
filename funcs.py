
level = 0

def fact(i):
    if i == 0:
        return 1
    return i * fact(i - 1)

def findit2(target, vl):
    global level
    level += 1
    mylevel = level
    print ">>> ", mylevel, ": ", target, ", ", vl
    i = 0
    while (i < len(vl)) :
        print mylevel, ": Try ", vl[i]
        if (vl[i] > target) :
            i += 1
        else :
            break

    if (i == len(vl)) :
        print mylevel, ": Did not find small enough value"
        return []
    elif (vl[i] == target) :
        print mylevel, ": FOUND it at element ", i
        return [vl[i]]
    else :
        print mylevel, ": ", vl[i], " < ", target, ", deeper"
        j = i + 1
        al = findit2(target - vl[i], vl[j:])
        if (al == []) :
            print mylevel, ": Did not find solution, move on"
            return findit2(target, vl[j:])
        else :
            print mylevel, ": Found it: ", al
            return [vl[i]] + al


