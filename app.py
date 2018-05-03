import json
from flask import Flask, jsonify, render_template, request, Response

app = Flask(__name__)

with open('movies.json') as json_data:
    d = json.load(json_data)
    list_data = []
    for movies in d['data']:
	    list_data.append(movies)

@app.route('/', methods = ['GET'])
def template():
    return render_template("index.html")

@app.route('/data', methods = ['GET'])
def all_movie_list():
    return render_template("index.html", list = list_data)

@app.route('/data/<int:id>', methods = ['GET'])
def movie_by_year(id):
    single_data = []
    for movie_data in list_data:
        if(movie_data['release'] == id or movie_data['id'] == id):
            single_data.append(movie_data)
    return render_template("index.html", list = single_data)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
