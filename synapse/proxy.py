from flask import Flask, request, jsonify
import threading

app = Flask(__name__)

# A dictionary to store the callback data and cookies for each state
callback_data = {}
callback_event = threading.Event()

@app.route('/callback/<session_id>')
def callback(session_id):
    code = request.args.get('code')
    state = request.args.get('state')
    # store entire querystring in variable
    # query_string = request.query_string.decode('utf-8')
    # store loginToken query param
    login_token = request.args.get('loginToken')

    # Store the callback data and cookies
    callback_data[session_id] = {
        'token': login_token
    }
    callback_event.set()  # Signal that data is available

    return "Login success. You can close this window.", 200

@app.route('/poll/<session_id>')
def poll(session_id):
    # Long polling mechanism
    def wait_for_callback(session_id):
        while session_id not in callback_data:
            callback_event.wait(timeout=10)  # Wait with a timeout to allow for checking if data is available
        return callback_data.pop(session_id)

    data = wait_for_callback(session_id)
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=8008)
