import sqlite3


def get_result(sql):
    with sqlite3.connect("netflix.db") as con:
        con.row_factory = sqlite3.Row
        result = []
        for item in con.execute(sql).fetchall():
            s = dict(item)
            result.append(s)

        return result


def search(name1, name2):
    sql = '''
    SELECT "cast"
    FROM netflix n 
    '''
    t = []
    result = get_result(sql)
    for item in result:
        if name1 in item.get("cast") and name2 in item.get("cast"):
            t.append(item.get("cast"))

    if len(t) >= 2:
        print(t)


def search_by(type, date, genre):
    sql = f'''
    SELECT *
    FROM netflix n
    WHERE "type" = '{type}' and release_year = {date} and listed_in LIKE '%{genre}%'
    '''
    print(get_result(sql))


if __name__ == '__main__':
    search("Rose McIver", "Ben Lamb")
    search_by(type="Movie", date=2009, genre="Action")
