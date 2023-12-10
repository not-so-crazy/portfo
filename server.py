
from token import NEWLINE
from flask import Flask, render_template, request, redirect
import flask
import json
import csv

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def home_02(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n Email: {email} \n Subject: {subject} \n Message: {message} \n')
        
def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        if email:
            if subject:
                if message:
                    csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    csv_writer.writerow([email, subject, message])
                else:
                    redirect('page_not_found.html')
            else:
                redirect('page_not_found.html')
        else:
            redirect('page_not_found.html')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method =='POST':
        data = request.form.to_dict()
        print(data)
        if data:
            if write_to_csv(data):
                write_to_csv(data)
                # with open('database.txt', 'w') as convert_file:
                # appender = convert_file.write(json.dumps(data))
                # convert_file.write(str(appender))
                return redirect('thankyou.html')
            else:
                return redirect('page_not_found.html')
        else:
            return redirect('page_not_found')
    else:
        return 'it seems it has some type of error'

# Deinstall the envirement first
# cd..
# python3 -m venv web_server
# . web_server/Scripts/activate.bat
# . web_server/Scripts/activate
# pip3 install flask
# flask --app server run --debug

