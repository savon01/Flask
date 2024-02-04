from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def predict_age():
    if request.method == 'POST':
        name = request.form['name']
        age = get_age(name)
        if age != None:
            return render_template('result.html', name=name, age=age)
        return render_template('result_none.html')
    return render_template('index.html')


def get_age(name):
    url = f"https://api.agify.io/?name={name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        age = data.get('age')
        return age
    else:
        print("Произошла ошибка при получении возраста:", response.status_code)
        return None


if __name__ == '__main__':
    app.run()
