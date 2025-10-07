a = None
b = None
c = None
def mais(a, b, c ):
    if a is not None and b is not None and c is not None:
        return a + b + c 
    if a is not None and c is not None and b is None:
        return a + c
    if a is not None and b is not None and c is None:
        return a + b
    if a is None and b is not None and c is not None:
        return b + c
    if a is None and b is None and c is None:
        return 0

print(mais(4, 8 , 3))