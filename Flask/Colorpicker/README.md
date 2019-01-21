
A Flask extension to add Spectrum jQuery color picker into the template, it makes adding and configuring multiple color pickers at a time much easier and less time consuming.

#### - From the source:
https://github.com/mrf345/flask_colorpicker.git


## Setup 

#### - Inside the Flask app:

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from colorpicker_local import colorpicker

app = Flask(__name__)
Bootstrap(app)
colorpicker(app)


#### - inside the jinja template

{% extends 'bootstrap/base.html'}

{% block scripts %}
  {{ super() }}
  {{ colorpicker.loader() }}
  {{ colorpicker.picker(ids=[".cp_01", ".cp_02"]) }}
{% endblock %}

{% block content %}
  <form class="verticalform">
    <input type="text" class="form-control cp_01" />
    <input type="text" class="form-control cp_02" />
  </form>
{% endblock %}

(cp_01 and cp_02 are example IDs of each field)


#### Settings:

Inside colorpicker_local:

def picker(self, ids=[".colorpicker"],         # list of ids of element to assign colorpicker to
            default_color='rgb(0,0,255,0.5)',  # default color to start with
            color_format='rgb',                # color format to use
            showAlpha='true',                  # enable or disable transparency
            showInput='false',                 # display or hide color picker
            showButtons='false',               # display or hide buttons
            allowEmpty='true'):                # allow empty input


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

IMPORTANT: 

- Change the links in colorpicker_local for your system 

- Add the route in flask:

  @app.route('/get_media/<path:filename>', methods=['GET'])
  def get_media(filename):
      return send_from_directory('FILEPATH', filename)

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
