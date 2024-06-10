from flask import Flask, request, jsonify

app = Flask(__name__)
ld={} 
@app.route('/user', methods=["POST"])
def user():
  global ld
  data = request.get_json()
  s=data['s']
  d=data['d']
  ld[s]=d
  
  #driver = driversetup()
  
  return  'Hello from Koyeb'
@app.route('/gets', methods=["POST"])
def gets():
   global ld
   data = request.get_json()
   s = data['s']
   return ld[s]
     
@app.route('/getd')
def getd():
  global ld
  return ld
@app.route('/')
def u(): 
  return "ndbdbdbndndb"