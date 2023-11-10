from flask import Flask, render_template
 
app = Flask(__name__, template_folder="templates")
import sys
import os

@app.route('/', methods=['GET','POST'])


def Menu_func():
    import os
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8001)