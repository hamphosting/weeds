from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
safever = 1.0
print(f"Running SafeLife Hub V{str(safever)}")
app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET', 'POST'])
def proxy():
    try:
        url = request.args.get('url')
    
        if url:
            response = requests.get(url)
            return jsonify({
                'status_code': response.status_code,
                'content': response.text
            })

    except:
        return jsonify({
            'status_code': 1,
            'content': f"""<p style="color: red;">NYOOOOOoOooOOOo that site doesnt exist.</p> <p>RUNNING SAFELIFE-HUB V{str(safever)}"""
        })

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify(str(safever))

if __name__ == '__main__':
    app.run(debug=True)
