from flask import Flask, request
import os
import logging

if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(level=logging.INFO, filename='logs/data.txt', filemode='a', format='%(asctime)s - %(message)s', encoding='utf-8')

app = Flask(__name__)

@app.route('/post', defaults={'subpath': ''}, methods=['POST'])
@app.route('/post/<path:subpath>', methods=['POST'])
def post(subpath):
    data = request.json
    logging.info(f"Received data for {subpath}: {data}")
    return 'Data saved', 200


@app.route('/get', methods=['GET'])
def get_logs():
    with open('logs/data.txt', 'r') as file:
        data = file.read()
    return data, 200

@app.route('/delete', methods=['DELETE'])
def delete_logs():
    with open('logs/data.txt', 'w') as file:
        file.write('')
    return 'Logs deleted', 200

if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.makedirs('logs')
    app.run(host="0.0.0.0", debug=True, port=5000)
