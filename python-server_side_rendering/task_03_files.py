from flask import Flask, render_template, request, jsonify
import json
import csv
import os

app = Flask(__name__)

def read_products_from_json():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return []

def read_products_from_csv():
    products = []
    try:
        with open('products.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Convert numeric fields to appropriate types
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id', type=int)
    
    if source not in ['json', 'csv']:
        return render_template('product_display.html', 
                            error="Invalid source. Please use 'json' or 'csv'.")
    
    # Read data based on source
    if source == 'json':
        products = read_products_from_json()
    else:  # csv
        products = read_products_from_csv()
    
    # Filter by ID if provided
    if product_id is not None:
        filtered_products = [p for p in products if p['id'] == product_id]
        if not filtered_products:
            return render_template('product_display.html',
                                error=f"No product found with ID {product_id}")
        products = filtered_products
    
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)