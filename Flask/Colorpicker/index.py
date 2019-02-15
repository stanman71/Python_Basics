from flask import Flask, render_template, send_from_directory

from colorpicker_local import colorpicker


app = Flask(__name__, template_folder='.')

colorpicker(app)



@app.route('/')
def root():
    return render_template('index.html')

# IMPORTANT
# ADD the PATH to spectrum.css and spectrum.js

@app.route('/get_media/<path:filename>', methods=['GET'])
def get_media(filename):
    return send_from_directory('C:/Users/stanman/Desktop/Unterlagen/GIT/Python_Training/Flask/Colorpicker/static/', filename)


app.run(debug=True, port=5000)

