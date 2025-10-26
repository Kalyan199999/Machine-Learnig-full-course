from flask import Flask, render_template

app = Flask( __name__ )

# Routes
@app.route('/')
def welcome():
    return "welcome o home page!pavan is amazing"

@app.route('/about')
def about():
    return "<h1>This is about page</h1>"

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/<name>')
def dynamic_function(name):
    return f"<h1>My name is {name} </h1><br />Thank u!"


if __name__ == '__main__':
    app.run(debug=True,port=5050)

