import requests
import json
import random
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

def generate_rand_namespace_id():
    return ''.join(random.choices('0123456789abcdef', k=16))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return pay_for_blob()
    return render_template('index.html')

@app.route('/pay-for-blob', methods=['POST'])
def pay_for_blob():

    node_ip = request.form['node_ip']
    node_port = request.form['node_port']
    namespace_id = generate_rand_namespace_id()
    data = 'aabbccddeeff'

    payload = {
        'namespace_id': namespace_id,
        'data': data,
        'gas_limit': 80000,
        'fee': 2000
    }

    response = requests.post(f"http://{node_ip}:{node_port}/submit_pfb", json=payload)

    if response.status_code == 200:
        try:
            result = response.json()
        except ValueError as e:
            result = {"error": f"Error parsing JSON response: {str(e)}"}
    else:
        result = {"error": f"Error: {response.status_code} - {response.text}"}

    return render_template('index.html', result=result, namespace_id=namespace_id)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
