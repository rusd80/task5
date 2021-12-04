from flask import Flask, json, request
from json import load

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get_query():
    query = json.loads(request.get_data())
    with open('countries.json') as file:
        countries = load(file)
    with open('languages.json') as file:
        languages = load(file)
    if len(query) == 2:
        result = "Country: {0}, capital: {1}, currency: {2}, languages(native): "\
            .format(countries[query]["name"], countries[query]["capital"], countries[query]["currency"],)
        native = []
        for lang in countries[query]["languages"]:
            native.append("{0}({1})".format(languages[lang]["name"], languages[lang]["native"]))
        result += ", ".join(native)
    else:
        result = "data incorrect"
    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
