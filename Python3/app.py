from flask import Flask
# import Jinja2



app=Flask(__name__)

@app.route("/")
def index():
    return "<html><H1>This is Best Learning Mr Hari</H1></html>"

@app.route("/index")
def index1():
    return "<html><H2>Welcome To the Flask Course Mr. Peddireddy Hari Vardhan Reddy</H2></html>"


@app.route("/main")
def index2():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)

# return "Peddireddy"

