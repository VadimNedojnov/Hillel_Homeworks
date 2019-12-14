from flask import Flask
from faker import Faker

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


if __name__ == '__main__':
    app.run()
