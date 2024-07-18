from flask import Flask, render_template, request, jsonify
import json
import csv

app = Flask(__name__)

def read_json_file(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def read_csv_file(filepath):
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json_file('products.json')
    elif source == 'csv':
        data = read_csv_file('products.csv')
    else:
        return render_template('product_display.html', error='Wrong source')

    if product_id:
        product_id = int(product_id)
        data = [product for product in data if int(product['id']) == product_id]
        if not data:
            return render_template('product_display.html', error='Product not found')
    
    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True)