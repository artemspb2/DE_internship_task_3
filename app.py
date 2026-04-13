from flask import Flask, request
from math import gcd

app = Flask(__name__)

def lcm(x, y):
    return x * y // gcd(x, y)

@app.route('/artemspb2_gmail_com')
def calculate():
    try:
        x = request.args.get('x')
        y = request.args.get('y')

        # Проверяем что x и y переданы
        if x is None or y is None:
            return 'NaN'

        # Проверяем что это целые положительные числа
        if not x.isdigit() or not y.isdigit():
            return 'NaN'

        x = int(x)
        y = int(y)

        # Натуральные числа — больше нуля
        if x <= 0 or y <= 0:
            return 'NaN'

        return str(lcm(x, y))

    except Exception:
        return 'NaN'

if __name__ == '__main__':
    app.run()
