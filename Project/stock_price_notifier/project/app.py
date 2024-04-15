from flask import Flask, request, render_template
import csv

app = Flask(__name__)

@app.route
def index():
    return render_template('main.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        contact = request.form['contact']
        with open('data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, address, contact])
        return 'Data submitted successfully!'

if __name__ == '__main__':
    app.run(debug=False)

