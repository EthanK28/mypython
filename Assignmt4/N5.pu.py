def myinitial(str):
    def f(x):
        return x[0]
    str = str.split()
    afterMap = map(f, str)
    result = ''.join(afterMap)
    print type(result)
    return result.upper()

print myinitial("as soon as possible")