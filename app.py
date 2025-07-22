from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_items():
    conn = sqlite3.connect('restaurant.db')
    c = conn.cursor()
    c.execute("SELECT id, name, price FROM items")
    items = c.fetchall()
    conn.close()
    return items

@app.route('/')
def index():
    items = get_items()
    return render_template('place_order.html', items=items)

@app.route('/show_bill', methods=['POST'])
def show_bill():
    table_no = request.form.get("table_no")
    ordered = []
    total = 0

    conn = sqlite3.connect('restaurant.db')
    c = conn.cursor()

    for key, value in request.form.items():
        if key == "table_no":
            continue
        qty = int(value)
        if qty > 0:
            c.execute("SELECT name, price FROM items WHERE id = ?", (key,))
            name, price = c.fetchone()
            subtotal = price * qty
            ordered.append({'name': name, 'price': price, 'qty': qty, 'subtotal': subtotal})
            total += subtotal

    conn.close()
    return render_template('show_bill.html', table_no=table_no, ordered=ordered, total=total)

if __name__ == '__main__':
    app.run(debug=True)

