from flask import Flask, render_template, redirect, url_for, request,jsonify;


app = Flask(__name__)
signal_status = {'state': 'stopped'}  # Possible: 'stopped', 'starting', 'started'
class ComndServer:
    commnd = "stop"


@app.route('/')
def index():
    return render_template('index.html', state=signal_status['state'])

@app.route('/app/start')
def start():
    ComndServer.commnd = "start"
    signal_status['state'] = 'starting'
    # return redirect(url_for('index'))
    return jsonify({'status': signal_status['state']})

@app.route('/app/refresh')
def refresh():
    return jsonify({'Content-Type': 'application/json', 'status': signal_status['state']})

@app.route('/board/getCom')
def getCom():
    return ComndServer.commnd


@app.route('/board/updateState')
def start_done():
    status = request.args.get('state', 'unknown')
    print(status)
    signal_status['state'] = status
    return "OK"



@app.route('/app/stop')
def stop():
    ComndServer.commnd = "stop"
    signal_status['state'] = 'stopping'
    # return redirect(url_for('index'))
    return jsonify({'status': signal_status['state']})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
