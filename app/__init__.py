from flask import Flask, render_template
from .config import Configuration
from .shipping_form import ShippingForm

app = Flask(__name__)
app.config.from_object(Configuration)



@app.route("/")
def index():
    return render_template("base.html")


@app.route("/new_package", methods=["GET", "POST"])
def new_package():
    form = ShippingForm()
    return render_template("shipping_request.html", form=form)
