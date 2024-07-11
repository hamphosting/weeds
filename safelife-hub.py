from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json
safever = 1.2 # Please dont change this. This lets the client know how to communicate with this.
print(f"Running SafeLife Hub V{str(safever)}")
mainhub = True # Please change this to false. This is letting the server know that this is the main server. Other servers use this to update.
#if not mainhub:
#    latestver = requests.get('https://safelifehub.hamperhamps.space/version')
#    if str(latestver) != safever:
#        print("YOU ARE USING AN OLD SERVER VERSION!!! PLEASE GO TO https://github.com/HAMPERHAMPS/safelife-hub/edit/main/safelife-hub.py AND DOWNLOAD THE LATEST SERVER VERSION FOR THE CLIENT TO WORK CORRECTLY!!!")
app = Flask(__name__)
banned = """108.51.114.54 174.219.255.241"""
online = True
CORS(app)
@app.route('/', methods=['GET', 'POST'])
def proxy():
    client_ip = request.remote_addr
    if not online:
        return jsonify({
            'status_code': 30023,
            'content': f"""<p style="color: red;">This server is not online. Try a different one. </p> <p>RUNNING SAFELIFE-HUB V{str(safever)} </p> <p style="color: red;">Your current ip: {str(client_ip)}</p>"""
        }) 
    if str(client_ip) in banned:
        return jsonify({
            'status_code': 30023,
            'content': f"""<p style="color: red;">Your IP is banned. </p> <p>RUNNING SAFELIFE-HUB V{str(safever)} </p> <p style="color: red;">Your current ip: {str(client_ip)}</p>"""
        }) 
    try:
        url = request.args.get('url')
        webhook_url = 'https://discordapp.com/api/webhooks/1260679944309051434/KfTn6WyuMH1ZEDy5FgvL9YA4AiitqG4o-fFJ2SuUfjY7Ty3BkeX4V-PPtGBgzwF-wKuW'
        payload = {
            
            'content': client_ip + " | " + url
        }
        json_payload = json.dumps(payload)


        if url:
            response = requests.get(url)
            return jsonify({
                'status_code': response.status_code,
                'content': response.text
            })

    except Exception as e:
        return jsonify({
            'status_code': 1,
            'content': f"""<p style="color: red;">NYOOOOOoOooOOOo somethings wrong!!! Error: {e}</p> <p>RUNNING SAFELIFE-HUB V{str(safever)} </p> <p style="color: red;">Your current ip: {str(client_ip)}</p>"""
        })

@app.route('/ping', methods=['GET'])
def ping():
    satsts = "ok"
    if online:
        return jsonify({'status': 'ok'})
    
@app.route('/version', methods=['GET'])
def version():
    return jsonify({'ver': safever})

if __name__ == '__main__':
    app.run(debug=True)
