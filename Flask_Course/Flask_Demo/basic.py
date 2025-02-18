from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1> Hello World Peddiredy </h1>"

@app.route('/html')
def info():
    return "<h1> Added New Page </h1>"

@app.route('/app/<name>')
def main(name):
    return "My name is {}".format(name)

if __name__=='__main__':
    app.run(debug=True)
