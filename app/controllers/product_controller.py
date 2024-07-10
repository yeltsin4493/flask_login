from flask import request, jsonify
from flask_jwt_extended import jwt_required
from ..models.product import Product
from ..extensions import db

@jwt_required()
def create_product():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')

    new_product = Product(name=name, price=price, description=description)
    db.session.add(new_product)
    db.session.commit()

    return jsonify({"msg": "Product created successfully", "product": new_product.to_dict()}), 201

@jwt_required()
def get_products():
    products = Product.query.all()
    products_list = [product.to_dict() for product in products]
    return jsonify(products_list), 200

@jwt_required()
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify(product.to_dict()), 200

@jwt_required()
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.get_json()

    product.name = data.get('name', product.name)
    product.price = data.get('price', product.price)
    product.description = data.get('description', product.description)

    db.session.commit()
    return jsonify({"msg": "Product updated successfully", "product": product.to_dict()}), 200

@jwt_required()
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"msg": "Product deleted successfully"}), 200
