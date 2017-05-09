from flask import Flask
app = Flask(__name__)


from subprocess import Popen

@app.route('/')
def hello_world():
        return 'command is online.\n\n'


@app.route('/re')
def reboot_pi():
    p = Popen(['/bin/sleep 5 && /usr/bin/sudo /sbin/reboot 0'], shell=True);

    return 'rebooting in 5..4..3..2..1..'


@app.route('/off')
def reboot_pi():
    p = Popen(['/bin/sleep 5 && /usr/bin/sudo /sbin/shutdown 0'], shell=True);

    return 'shutting down in 5..4..3..2..1..'
