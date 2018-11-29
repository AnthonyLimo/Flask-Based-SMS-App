from flask import Flask, render_template, request, json
import africastalking

#authenticate with africastalking

#initialize SMS service

#create flask app

app = Flask(__name__)

#create routes to views

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/showSMSPage")
def showSendSMS():
    return render_template('sms.html')

#route SMS sending route 
#request sent via AJAX

@app.route("/signUp", methods=["POST"])
def signUp():
    #Reading values from the UI
    _sms_message = request.form[]
    _phone_number = request.form[]
    
    if _sms_message and _phone_number:
        return json.dumps({'html':'<span>All fields are good. Sending SMS</span>'})
    else:
        return json.dumps({'html':'<span>Please fill the required fields</span>'})

if __name__ == "__main__":
    app.run()