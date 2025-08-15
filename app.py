from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(200), nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    total_price = db.Column(db.Float, nullable=False)

@app.route("/")
def home():
    products = Product.query.all()
    return render_template("index.html", products=products)

@app.route("/add_to_cart/<int:product_id>")
def add_to_cart(product_id):
    cart = session.get("cart", [])
    cart.append(product_id)
    session["cart"] = cart
    return redirect(url_for("home"))

@app.route("/cart")
def cart():
    cart = session.get("cart", [])
    products = Product.query.filter(Product.id.in_(cart)).all()
    total = sum([p.price for p in products])
    return render_template("cart.html", products=products, total=total)

@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    cart = session.get("cart", [])
    if not cart:
        return redirect(url_for("home"))

    products = Product.query.filter(Product.id.in_(cart)).all()
    total = sum([p.price for p in products])

    if request.method == "POST":
        name = request.form["name"]
        address = request.form["address"]
        phone = request.form["phone"]

        new_order = Order(name=name, address=address, phone=phone, total_price=total)
        db.session.add(new_order)
        db.session.commit()

        session["cart"] = []  # Clear cart
        return redirect(url_for("thank_you", order_id=new_order.id))

    return render_template("checkout.html", total=total)

@app.route("/thank_you/<int:order_id>")
def thank_you(order_id):
    order = Order.query.get_or_404(order_id)
    return render_template("thank_you.html", order=order)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
