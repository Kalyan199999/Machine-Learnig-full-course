from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/success')
def success():
    score = int(request.args.get('score', 0))
    res = "passed" if score >= 60 else "failed"
    return render_template('result.html', result=res , marks=score)

if __name__ == "__main__":
    app.run(debug=True)