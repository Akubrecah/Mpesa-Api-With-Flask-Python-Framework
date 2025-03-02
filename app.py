# filepath: /c:/xampp/htdocs/daraja_flask/app.py
from flask import Flask, render_template, request, jsonify
from access_token import get_access_token, lipa_na_mpesa_online

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pay', methods=['POST'])
def pay():
    phone_number = request.form['phone_number']
    amount = request.form['amount']
    
    token = get_access_token()
    response = lipa_na_mpesa_online(token)
    
    # Check if 'ResponseCode' is in the response
    if 'ResponseCode' in response and response['ResponseCode'] == '0':
        message = "Check Your Phone and Enter PIN to complete transaction"
    else:
        message = "Canceled by the user"
    
    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(debug=True)