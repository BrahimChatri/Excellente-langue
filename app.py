from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inscription')
def inscription():
    return render_template('inscription.html')

@app.route('/etudiants')
def etudiants():
    return render_template('etudiants.html')

if __name__ == '__main__':
    app.run(debug=True)