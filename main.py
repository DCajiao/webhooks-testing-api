from flask import Flask, request
import os
import logging

if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(level=logging.INFO, filename='logs/data.txt', filemode='a', format='%(asctime)s - %(message)s', encoding='utf-8')

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def post():
    data = request.json
    logging.info(data)
    return 'Data saved'


@app.route('/get', methods=['GET'])
def get_logs():
    with open('logs/data.txt', 'r') as file:
        data = file.read()
    return data


if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.makedirs('logs')
    app.run(debug=True, port=5000)
