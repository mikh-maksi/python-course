a = input("a = ")
a = float(a)

b = input("b = ")
b = float(b)

c = input("c = ")
c = float(c)

D = (b**2 - 4*a*c) ** (0.5)
x1 = (-b + D) / (2 * a)
x2 = (-b - D) / (2 * a)

print(f"x1 = {x1}; x2 = {x2}")
