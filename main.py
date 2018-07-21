# -------------------------------------------------#
# Title: main.py
# Dev: Scott Luse
# Date: 07/21/2018
# Epoch time generator
# -------------------------------------------------#

import os
import time

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Please send /epoch/ request."

@app.route('/epoch/')
def time_epoch():
    epoch_time = str(int(time.time()))
    return (epoch_time)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

