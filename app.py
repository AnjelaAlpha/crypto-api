from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/crypto')
def crypto():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    r = requests.get(url, timeout=10)
    d = r.json()
    b = d['bpi']

    return jsonify({
        'USD': b['USD']['rate'],
        'EUR': b['EUR']['rate'],
        'GBP': b['GBP']['rate']
    })

if __name__ == '__main__':
    app.run(debug=True)  
