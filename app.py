from flask import Flask, request, jsonify
#from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def driversetup():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Selenium in headless mode
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("lang=en")
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--incognito")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
    return driver
    
app = Flask(__name__)
 
@app.route('/y')
def y():
  driver = driversetup()
  
  return  'Hello from Koyeb'
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