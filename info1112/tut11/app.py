#code for establishing web server


from flask import Flask, render_template
app = Flaks(__name__)
#In shell type argument 'export FLASK_APP=app.py'
#Run server with command 'python3 -m flask run --host=0 -- port=5678(this is the uni port)'

visitors = []

@app.route('/home')
def hello():
    return "This is the home page"

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/visit/<name>')
def visit(name):
    output = "Hello, %s! " % name
    output += "These people have visited: %s" % "\n".join(visitors)
    visitors.append(name)
    return output

@app.route('/visitors')
def visits():
    return "These people have visited: %s" % ("\n".join(visitors))
