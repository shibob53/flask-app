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
   data = 
   s = data['s']
   return ld[s]
     
@pp.route('/getd')
def getd():
  global ld
  return ld