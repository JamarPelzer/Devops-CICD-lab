## Math API logic Layer 
print("Hello from DevOps CI/CD Lab")

def add(x, y):
  return x + y

def subtract (x, y):
  return x - y 

def multiply(x, y):
  return x * y 

def divide (x, y):
  if y == 0:
    raise ValueError("Cannot divide by zero")
  return x / y

def exponent(x, y):
  return x ** y 

def modulo(x, y):
  return x % y
