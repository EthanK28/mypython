

class MySet(list):
    def __init__(self, l):
        for e in l:
            self.append(e)
        MySet.eliminate_duplicate(self)

    def __str__(self):
        result = "MySet: {"
        for e in self:
            result = result + str(e) + " ,"
        result = result[0:len(result)-2] + "}"
        return result

    def __or__(self, other):
        s = []
        for e in self:
            for i in other:
                if(i not in s and e not in s):
                    s.append(i)
        return s
    def __and__(self, other):
        s = []
        for e in self:
            for i in other:
                if(e not in s and i not in s):
                    if(e == i):
                        s.append(i)


    @staticmethod
    def eliminate_duplicate(l):
        s = []
        for e in l:
            if e not in s:
                s.append(e)
        l[:] = []
        for e in s:
            l.append(e)