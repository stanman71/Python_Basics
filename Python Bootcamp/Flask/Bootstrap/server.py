from flask import Flask, render_template
from flask_bootstrap import Bootstrap 

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html', site1="site1", site2="site2")

if __name__ == '__main__':
    app.run(debug=True)


