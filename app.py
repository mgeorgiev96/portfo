from flask import Flask, render_template,url_for,request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def index1():
    return render_template('index.html')

@app.route('/<string:page_name>')
def index(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt','a') as database:
        email,subject,message = data['email'],data['subject'],data['message']
        file = database.write(f'\n{email},{subject},{message}')
def write_to_csv(data):
    with open('database.csv','a') as database2:
        email,subject,message = data['email'],data['subject'],data['message']
        csv_writer = csv.writer(database2,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
          data = request.form.to_dict()
          write_to_csv(data)
          return redirect('index.html')
        except:
          return 'Did not save to database'
    else:
        return 'something went wrong'

