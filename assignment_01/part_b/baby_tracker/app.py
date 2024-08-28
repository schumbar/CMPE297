import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from data_storage import save_event, get_events

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    return redirect(url_for('dashboard'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # This is a placeholder login. In a real application, you would validate credentials.
        session['user'] = email
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/event/<event_type>', methods=['GET', 'POST'])
def event(event_type):
    if 'user' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        event_data = request.form.to_dict()
        event_data['event_type'] = event_type
        save_event(session['user'], event_data)
        flash('Event recorded successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('event_form.html', event_type=event_type)

@app.route('/history')
def history():
    if 'user' not in session:
        return redirect(url_for('login'))
    events = get_events(session['user'])
    return render_template('history.html', events=events)

if __name__ == '__main__':
    app.run(debug=True)