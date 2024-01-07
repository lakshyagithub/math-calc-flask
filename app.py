from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def api_contactor():
    if request.method == 'POST':
        simplify = request.form["operation1"]
        equation = request.form["equation1"]
        api_url = 'https://newton.now.sh/api/v2/' + simplify + '/' + equation

        response = requests.get(api_url)
        data = response.json()

        return render_template('index.html', expression1=equation, ans1=data['result'])

    # If it's a GET request or any other method, render the template with default values
    return render_template('index.html', expression1="", ans1="")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9002)
