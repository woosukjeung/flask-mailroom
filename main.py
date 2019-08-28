import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donor, Donation

app = Flask(__name__)
# app.secret_key = b'\x98E\xb3\xb4O\xd9\xd8\xf7\xe1C\x89\xef\x89\xc2G\xd6\xa9W\x84\xc2hCP\xfb'
app.secret_key = os.environ.get('SECRET_KEY').encode()


@app.route('/')
def home():
    return redirect(url_for('all'))


@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)


@app.route('/create/', methods=['GET', 'POST'])
def create():
    # if request.method

    if request.method == 'POST':
        entry = Donor(name=request.form['name'])
        entry.save()
        Donation(donor=entry, value=request.form['amount']).save()
        return redirect(url_for('home'))
    else:
        return render_template('create.jinja2')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
