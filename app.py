from flask import Flask, render_template, request, json
import africastalking

#authenticate with africastalking
username = "sandbox"
api_key = "f6c6e1d0686fddddb375d47c8bcda0dc80713f214ce26b912567ab156ae7feee"
africastalking.initialize(username,api_key)

#initialize SMS service

sms = africastalking.SMS

#create flask app

app = Flask(__name__)

#create routes to views

@app.route("/")
def main():
    _sms_message = request.form["smsMessage"]
    _phone_number = request.form["phoneNumber"]

    response = sms.send(_sms_message, [str(_phone_number)])
    #print(response)
    return render_template('index.html')

@app.route("/showSMSPage")
def showSendSMS():
    return render_template('sms.html')

#route SMS sending route 
#request sent via AJAX

@app.route("/sendSMS", methods=["POST"])
def sendSMS():
    #Reading values from the UI
    if request.method == "POST":
        _sms_message = request.form["smsMessage"]
        _phone_number = request.form["phoneNumber"]

        response = sms.send(_sms_message, [str(_phone_number)])
        print(response)
    
        if _sms_message and _phone_number:
            return json.dumps({'html':'<span>All fields are good. Sending SMS</span>'})
        else:
            return json.dumps({'html':'<span>Please fill the required fields</span>'})

if __name__ == "__main__":
    app.run(debug=True)