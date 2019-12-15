from flask import Flask
from faker import Faker
import requests

app = Flask('app')


@app.route('/')
def generator():
    return '<br />'.join(f"User name: {Faker().name()}, Email: {Faker().email()}" for i in range(100))


@app.route('/height_weight')
def height_weight():
    with open('hw.csv') as file:
        height = 0
        weight = 0
        count = 0
        for line in file.readlines():
            modern_line = line.strip().split(', ')
            if len(modern_line) == 3 and modern_line[1][0].isdigit() and modern_line[2][0].isdigit():
                height += float(modern_line[1])
                weight += float(modern_line[2])
                count += 1
    return f'Average height: {height / count}; Average weight: {weight / count}'


@app.route('/space')
def space():
    api_request = requests.get('http://api.open-notify.org/astros.json')
    names = '<br />'.join(f'Astronaut {i + 1}: {api_request.json()["people"][i]["name"]}' for i in range(api_request.json()['number']))
    return f'Humans amount in space: {api_request.json()["number"]} <br />{names}'


if __name__ == '__main__':
    app.run()

# Add string for pull request