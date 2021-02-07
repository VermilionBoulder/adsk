from flask import Flask
app = Flask(__name__)

participants = [
    1, 2, 3, 4
]

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/sample')
def api_sample():
    return json.dumps(participants)

@app.route('/index')
def html_sample():
    return render_template('index.html', participants=participants)
