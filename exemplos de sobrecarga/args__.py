class Example:
    def add(self, *args):
        return sum(args)
# * Define a tupla
# Termo args como uma convenção (poderia ser qualquer nome)

obj = Example()

print(obj.add(10, 20))        # 2 valores → 30
print(obj.add(5, 10, 15))     # 3 valores → 30
print(obj.add(1, 2, 3, 4, 5)) # 5 valores → 15