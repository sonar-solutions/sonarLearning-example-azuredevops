def is_not_empty(value):
    if not value:
        return False
    else:
        return True

def main():
    # Input
    name = input("Enter your name: ")

    # Check if name is empty
    if is_not_empty(name):
        print("Hello, {}!".format(name))
    else:
        print("Name is empty.")

if __name__ == "__main__":
    main()

def fun(a):
  i = 10
  return i + a       # Noncompliant
  i += 1             # this is never executed


def fun(b):
  i = 10
  return i + b       # Noncompliant
  i += 1             # this is never executed

def fun(c):
  i = 10
  return i + c       # Noncompliant
  i += 1             # this is never executed

def fun(d):
  i = 10
  return i + d      # Noncompliant
  i += 1             # this is never executed


def fun3(c3):
  i = 10
  return i + c3       # Noncompliant
  i += 1             # this is never executed

def fun2(d2):
  i = 10
  return i + d2      # Noncompliant
  i += 1             # this is never executed

def main():
    # Input
    name = input("Enter your name: ")

    # Check if name is empty
    if is_not_empty(name):
        print("Hello, {}!".format(name))
    else:
        print("Name is empty.")