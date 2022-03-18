from flask import Flask
from flask_cors import CORS
import json


app = Flask('app')
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route('/')
def hello_world():
  return 'Hello, world!'

@app.route('/favicon.ico')
def favicon():
  return app.send_static_file('favicon.ico')



@app.route('/lasit')
def lasit():
  with open('dati/chats.txt', 'r', encoding = "utf-8") as f:
    chats = f.read()

  return chats

@app.route('/sutit/<vards>/<zina>')
def sutit(vards, zina):
  # "/sutit/Anna/Labrit visiem:"
  rinda = {
    "zina": zina,
    "vards": vards
  }
  with open('dati/chats.json', 'r', encoding = "utf-8") as r:
    vecie = r.read()
    rindas = json.loads(vecie)

  rindas.append(rinda)
  print(rinda)
  
  

  with open('dati/chats.json', 'w', encoding = "utf-8") as f:
    f.write(json.dumps(rindas, indent = 2, ensure_ascii = False ))
  return "Ok!"

@app.route('/sutit')
def sutit2():
  # "/sutit/Anna/Labrit visiem:"
    
  return True
app.run(host='0.0.0.0.', post = 8080)