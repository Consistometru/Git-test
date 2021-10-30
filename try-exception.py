print("salut")
from operator import pow, truediv, mul, add, sub, floordiv, mod
w = 0
operators = {
  '+': add,
  '-': sub,
  '*': mul,
  '/': truediv,
  '^': pow,
  '//': floordiv,
  '%': mod
}

def calculate(s):
    if s.isdigit():
        return float(s)
    for c in operators.keys():
        left, operator, right = s.partition(c)
        if operator in operators:
            return operators[operator](calculate(left), calculate(right))
if w:
     file = open("history.txt", "w")
input1 = input("continuati? da / nu: ")
while input1 == "da":
    calc = input("Type calculation:\n")
    print("Answer: " + str(calculate(calc)))
    if w:
         file.write(calc + " Answer: " + str(calculate(calc)))
    input1 = input("continuati? da / nu: ")
if w:
     file.close()