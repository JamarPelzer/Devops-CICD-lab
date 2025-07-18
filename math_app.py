from flask import Flask, request, jsonify

app = Flask(__name__)

print("Hello from DevOps CI/CD Lab")
# math Functions
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

# Routes
@app.route("/")
def home():
      return '''
    <h2>Welcome to the Math API</h2>
    <p>Use routes like /add?x=5&y=3</p>
    <ul>
      <li>/add?x=5&y=3</li>
      <li>/subtract?x=5&y=3</li>
      <li>/multiply?x=5&y=3</li>
      <li>/divide?x=5&y=3</li>
      <li>/exponent?x=5&y=3</li>
      <li>/modulo?x=5&y=3</li>
    </ul>
    '''
@app.route('/add')
def add_route():
    x = float(request.args.get('x'))
    y = float(request.args.get('y'))
    return jsonify(result=add(x, y))

@app.route('/subtract')
def subtract_route():
    x = float(request.args.get('x'))
    y = float(request.args.get('y'))
    return jsonify(result=subtract(x, y))

@app.route('/multiply')
def multiply_route():
    x = float(request.args.get('x'))
    y = float(request.args.get('y'))
    return jsonify(result=multiply(x, y))

@app.route('/divide')
def divide_route():
    x = float(request.args.get('x'))
    y = float(request.args.get('y'))
    return jsonify(result=divide(x, y))

@app.route('/exponent')
def exponent_route():
    x = float(request.args.get('x'))
    y = float(request.args.get('y'))
    return jsonify(result=exponent(x, y))

@app.route('/modulo')
def modulo_route():
    x = float(request.args.get('x'))
    y = float(request.args.get('y'))
    return jsonify(result=modulo(x, y))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
