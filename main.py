from flask import Flask
import json
from utils import get_result

app = Flask(__name__)


@app.get("/movie/<title>")
def get_by_title(ttitle: str):
    sql = f'''
    SELECT *
    FROM netflix n
    WHERE n.title = {title} and n.date_added = (SELECT max(date_added)
    FROM netflix name
    WHERE n.title = {title})
    '''
    result = []
    for item in get_result(sql):
        s = {
            "title": item.get("title"),
            "country": item.get("country"),
            "release_year": item.get("release_ear"),
            "listed_in": item.get("genre"),
            "description": item.get("description"),
        }
        result.append(s)
    return app.response_class(response=json.dumps(result),
                              status=200,
                              mimetype="application/json")


@app.get("/movie/<year1>/to/<year2>")
def get_by_date(year1: str, year2: str):
    sql = f'''
    SELECT *
    FROM netflix n
    WHERE release_year >= {year1} and release_year <={year2}
    LIMIT 100
    '''
    result = []
    for item in get_result(sql):
        s = {
            "title": item.get("title"),
            "release_year": item.get("release_ear"),
        }
        result.append(s)
    return app.response_class(response=json.dumps(result),
                              status=200,
                              mimetype="application/json")


@app.get("/rating/<value>")
def get_by_rating(value: str):
    sql = f'''
    SELECT *
    FROM netflix n
    '''

    if value == 'children':
        sql += f'''WHERE rating = 'G' '''
    elif value == 'family':
        sql += f'''WHERE rating LIKE '%G' '''
    elif value == 'adult':
        sql += f'''WHERE rating = 'R' or rating = 'NC-17' '''
    else:
        return app.response_class(response=json.dumps({}),
                                  status=204,
                                  mimetype="application/json")

    result = []
    for item in get_result(sql):
        s = {
            "title": item.get("title"),
            "release_year": item.get("release_ear"),
            "description": item.get("description"),
        }
        result.append(s)
    return app.response_class(response=json.dumps(result),
                              status=200,
                              mimetype="application/json")

@app.get("/genre/<genre>")
def get_by_genre(genre: str):
    sql = f'''
    SELECT *
    FROM netflix n
    WHERE listed_in = {genre}
    LIMIT 10
    '''
    result = []
    for item in get_result(sql):
        s = {
            "title": item.get("title"),
            "description": item.get("description"),
        }
        result.append(s)
    return app.response_class(response=json.dumps(result),
                              status=200,
                              mimetype="application/json")


if __name__ == '__main__':
    app.run(host="localhost", port=8080)

