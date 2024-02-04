from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/check_user_status', methods=['GET'])
def check_user_status():
    phone_number = request.args.get('phone_number')
    if not phone_number:
        return jsonify({'error': 'Phone number is required'}), 400

    url = "https://app.mynagad.com:20002/api/user/check-user-status-for-log-in"

    headers = {
        "X-KM-User-AspId": "100012345612345",
        "X-KM-User-Agent": "ANDROID/1152",
        "X-KM-DEVICE-FGP": "19DC58E052A91F5B2EB59399AABB2B898CA68CFE780878C0DB69EAAB0553C3C6",
        "X-KM-Accept-language": "bn",
        "X-KM-AppCode": "01",
    }

    params = {"msisdn": phone_number}

    response = requests.get(url, headers=headers, params=params)
    
    return response.text

if __name__ == '__main__':
    app.run(debug=True)
