
from collections import namedtuple

def getMarks(m, p, c, b):
    nmdTpl = namedtuple("Marks", "M P C B")
    tpl = nmdTpl(M=m, P=p, C=c, B=b)
    return tpl

marks = getMarks(96, 89, 79, 92)
print(marks)
print(f"Maths     :{marks.M}")
print(f"Physics   :{marks.P}")
print(f"Chemistry :{marks.C}")
print(f"Biology   :{marks.B}")

# immutable dictionary