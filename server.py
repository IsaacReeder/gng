from flask import Flask, render_template, request, url_for, redirect, session
import random

app = Flask(__name__)                     
app.secret_key = 'ThisIsSecret'


@app.route('/')                                                                    
def index():
    
    if not 'guess' in session:
        session ['guess_number'] = random.randrange(0, 101)
    return render_template('gng.html')

@app.route('/guess', methods=['POST'])                                                                    
def guess():
    session["guess"] = int(request.form['guess'])
    print (session)
    return redirect('/')


@app.route('/play_again', methods=['POST'])                                                                    
def play_again():
    session['guess_number'] = random.randrange(0, 101)
    session['guess'] = None
    return redirect('/')
           
app.run(debug=True)