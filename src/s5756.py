class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, x, y):
        return x + y

calculator = Calculator()
result = calculator.add(5, 10)
print("Result:", result)

# Bug: Calling a non-callable value
calculator = 42
result = calculator.add(5, 10)
print("Result:", result)

#adding comment to trigger commit


name = name

import tempfile

filename = tempfile.mktemp() # Noncompliant
tmp_file = open(filename, "w+")



def fpn(a):
  j = 10
  return i + a       # Noncompliant
  j += 1             # this is never executed
