from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        contact = request.form['number']
        with open('data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, address, contact])
        return 'Data submitted successfully!'

if __name__ == '__main__':
    app.run(debug=False)


      