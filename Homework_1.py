from flask import Flask
from faker import Faker

app = Flask('app')


@app.route('/')
def generator():
    return '<br />'.join(f"User name: {Faker().name()}, Email: {Faker().email()}" for i in range(100))


@app.route('/')
def height_weight():
    return


if __name__ == '__main__':
    app.run()