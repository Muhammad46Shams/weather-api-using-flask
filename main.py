from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/v1/<station>/<date>')
def about(station, date):
    temprature = str(23)
    return {
		'station': station,
		'date' : date,
		'temprature': temprature
	}

if __name__ == 'main':
	app.run(debug=True)