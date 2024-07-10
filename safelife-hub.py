from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
safever = 1.0 # Please dont change this. This lets the client know how to communicate with this.
print(f"Running SafeLife Hub V{str(safever)}")
mainhub = True # Please change this to false. This is letting the server know that this is the main server. Other servers use this to update.
if not mainhub:
    latestver = requests.get('https://safelifehub.hamperhamps.space/ping')
    if int(latestver) != safever:
        print("YOU ARE USING AN OLD SERVER VERSION!!! PLEASE GO TO https://github.com/HAMPERHAMPS/safelife-hub/edit/main/safelife-hub.py AND DOWNLOAD THE LATEST SERVER VERSION FOR THE CLIENT TO WORK CORRECTLY!!!")
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
    return jsonify({'ver': safever} {'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True)
