"""Module providing csv."""
import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    """Function render index"""
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    """Function render html page."""
    return render_template(page_name +'.html')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    """Function submit contact form."""
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou')
        except RuntimeWarning:
            return 'did not save to database'
    else:
        return "something went wrong, try again later"
    
def write_to_csv(data):
    """Function write data to csv file."""
    with open('database.csv', newline="", mode="a", encoding="utf-8") as database:
        fieldnames = ["email", "subject", "message"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.DictWriter(database, fieldnames=fieldnames)
        
        csv_writer.writerow({'email':email, 'subject':subject, 'message':message})
