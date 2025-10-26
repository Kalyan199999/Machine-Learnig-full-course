from flask import Flask, render_template,request  

app = Flask( __name__ )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home' , methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login' , methods=['GET' , 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        print(f"Username: {username}, Password: {password}")
        return f"Username: {username}, Password: {password}"
        
    return render_template('login.html' )


if __name__ == '__main__':
    app.run(debug=True , port=5050)