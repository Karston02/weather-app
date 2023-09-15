from flask import Flask, render_template, request
from weather import main as get_weather

app = Flask(__name__)


@app.route('/' , methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'GET':
        city_name = request.args.get('city_name')
        state_name = request.args.get('state_name')
        country_name = request.args.get('country_name')
        if city_name and state_name and country_name:
            data = get_weather(city_name, state_name, country_name)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)