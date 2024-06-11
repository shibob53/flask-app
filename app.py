from flask import Flask, request, jsonify
from selenium import webdriver

app = Flask(__name__)

# Global dictionary to store user data
ld = {}

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

@app.route('/')
def home(): 
    driver = driversetup()
    return "Hello from Koyeb"

@app.route('/user', methods=["POST"])
def add_user():
    global ld
    data = request.get_json()
    s = data['s']
    d = data['d']
    ld[s] = d
    return 'User data added successfully'

@app.route('/gets', methods=["POST"])
def get_user():
    global ld
    data = request.get_json()
    s = data['s']
    if s in ld:
        return jsonify({s: ld[s]})
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/getd')
def get_all_users():
    global ld
    return jsonify(ld)

@app.route('/y')
def y_route():
    driver = driversetup()
    return 'Hello from Koyeb'
