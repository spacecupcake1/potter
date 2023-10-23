from flask import Flask, render_template, request

app = Flask(__name__)

# Book prices and discounts
BOOK_PRICE = 8
DISCOUNTS = {
    2: 0.05,
    3: 0.1,
    4: 0.2,
    5: 0.25
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    quantities = [request.form.get(f'book{i}', 0) for i in range(1, 6)]

    total_price = 0
    for qty in quantities:
        if qty:
            total_price += int(qty) * BOOK_PRICE

    max_discount = 0
    for num_books, discount in DISCOUNTS.items():
        unique_books = len([qty for qty in quantities if qty and int(qty) > 0])
        if unique_books >= num_books and discount > max_discount:
            max_discount = discount

    discounted_price = total_price * (1 - max_discount)

    return render_template('index.html', result=f"The total price is {total_price} EUR. After discounts, it's {discounted_price:.2f} EUR.")

if __name__ == '__main__':
    app.run(debug=True)
