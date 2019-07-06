from flask import Flask
from flask import render_template
from flask import request
import json

app = Flask(__name__)

list_of_datas = ['dota']

@app.route("/")
def hello():
    return "Hello world!"

@app.route('/api/add', methods=['POST'])
def post_json_data():
    income_data = request.get_data()
#    print("TYPE of data: " + str(type(income_data)))
#    print(request.is_json)
#    print(income_data)
    json_string = json.loads(income_data)
#    print(json_string)
    list_of_datas.append(json_string)
    string_of_datas = '; '.join(str(i) for i in list_of_datas)
    return render_template( 'genlist.html', name='api', list=string_of_datas)


@app.route('/api/<name>', methods=['GET'])
def get_json_data(name=None):
    string_of_datas = '; '.join(str(i) for i in list_of_datas)
    return render_template( 'genlist.html', name=name, list=string_of_datas)

if __name__ == "__name__":
    app.run()

