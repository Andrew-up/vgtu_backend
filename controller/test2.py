from controller import app
import json  # json library imported

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def test():
    person_data = '{  "person":  { "name":  "Kenn",  "sex":  "male",  "age":  28}}'
    dict_obj = json.loads(person_data)
    print(dict_obj)


if __name__ == '__main__':
    test()

    pass
