from flask import Flask, request, jsonify, render_template
import database as db

app = Flask(__name__)

@app.route('/')
def index():
    treats = db.retrieve_treats()
    stock = db.get_stock()
    requests = db.fetch_requests()
    return render_template('index.html', treats=treats, stock=stock, requests=requests)

@app.route('/treats', methods=['GET', 'POST'])
def treats():
    if request.method == 'GET':
        return jsonify({"treats": db.retrieve_treats()}), 200
    elif request.method == 'POST':
        data = request.json
        db.create_treat(data['treat_name'], data['availability'])
        return jsonify({"message": "Treat added successfully"}), 201

@app.route('/treats/<int:treat_id>', methods=['DELETE'])
def delete_treat(treat_id):
    db.remove_treat(treat_id)
    return jsonify({"message": "Treat removed"}), 200

@app.route('/stock', methods=['GET', 'POST'])
def stock():
    if request.method == 'GET':
        return jsonify({"stock": db.get_stock()}), 200
    elif request.method == 'POST':
        data = request.json
        db.add_stock_item(data['item_name'], data['amount'])
        return jsonify({"message": "Stock item added"}), 201

@app.route('/stock/<int:item_id>', methods=['PUT', 'DELETE'])
def manage_stock(item_id):
    if request.method == 'PUT':
        data = request.json
        db.modify_stock(item_id, data['new_amount'])
        return jsonify({"message": "Stock updated"}), 200
    elif request.method == 'DELETE':
        db.remove_stock_item(item_id)
        return jsonify({"message": "Stock item removed"}), 200

@app.route('/requests', methods=['GET', 'POST'])
def customer_requests():
    if request.method == 'GET':
        return jsonify({"requests": db.fetch_requests()}), 200
    elif request.method == 'POST':
        data = request.json
        db.log_request(data['treat_name'], data['requester'], data.get('dietary_restrictions'))
        return jsonify({"message": "Request logged"}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
