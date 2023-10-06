from flask import Flask, render_template
import requests
from requests.structures import CaseInsensitiveDict
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, FloatField, BooleanField, RadioField, SubmitField)
from wtforms.validators import InputRequired, Length
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__, instance_relative_config=False)
app.config['SECRET_KEY'] = "your secret key"

class ContactForm(FlaskForm):
    price = FloatField("Price", validators=[InputRequired()],render_kw={"placeholder": "1"})
    submit = SubmitField("Submit")

def get_turkishlira():
    url = "your API endpoint"
    resp = requests.get(url)
    if resp.status_code == 200:
        cur = resp.json()
        val = cur['data']['TRY']
        print(val)
        return val
    else:
        notfound = "This website is not currently functioning due to the exceeded limit in API."
        print(notfound)
        return notfound

def get_britishpound():
    url = "your API endpoint"
    resp = requests.get(url)
    if resp.status_code == 200:
        cur = resp.json()
        val = cur['data']['GBP']
        print(val)
        return val
    else:
        notfound = "This website is not currently functioning due to the exceeded limit in API."
        print(notfound)
        return notfound

def get_euro():
    url = "your API endpoint"
    resp = requests.get(url)
    if resp.status_code == 200:
        cur = resp.json()
        val = cur['data']['EUR']
        print(val)
        return val
    else:
        notfound = "your API endpoint"
        print(notfound)
        return notfound

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/turkishlira", methods=['GET', 'POST'])
def get_tl():
    form = ContactForm() 
    currency = get_turkishlira()
    if form.validate_on_submit():
        price = form.price.data
        print("Price:", price)
        res = float(price) * float(currency)
        return render_template("turkishlira.html", tl = res, form=form)
    return render_template("turkishlira.html", tl = currency, form=form)

@app.route("/britishpound", methods=['GET', 'POST'])
def get_gbp():
    form1 = ContactForm()
    currency = get_britishpound()
    if form1.validate_on_submit():
        price = form1.price.data
        print("Price:", price)
        res = float(price) * float(currency)
        return render_template("britishpound.html", gbp = res, form=form1)
    return render_template("britishpound.html", gbp = currency, form=form1)

@app.route("/euro", methods=['GET', 'POST'])
def get_eur():
    form2 = ContactForm()
    currency = get_euro()
    if form2.validate_on_submit():
        price = form2.price.data
        print("Price:", price)
        res = float(price) * float(currency)
        return render_template("euro.html", eur = res, form=form2)
    return render_template("euro.html", eur = currency, form=form2)

if __name__ == "__main__":
  app.run(debug=True)
