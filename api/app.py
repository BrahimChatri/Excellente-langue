from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder='../static', template_folder='../templates')

# Main routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inscription')
def inscription():
    return render_template('inscription.html')

@app.route('/etudiants')
def etudiants():
    return render_template('etudiants.html')

# Static file handler
@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)
