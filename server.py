from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name +'.html')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('thankyou')
    else:
        return "something went wrong"
    
def write_to_csv(data):
    with open('database.csv', newline="", mode="a") as database:
        fieldnames = ["email", "subject", "message"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.DictWriter(database, fieldnames=fieldnames)
        
        csv_writer.writerow({'email':email, 'subject':subject, 'message':message})
