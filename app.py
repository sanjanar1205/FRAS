from flask import Flask, render_template, request, redirect, flash, url_for
import subprocess
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for flashing messages
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///info.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Admin('{self.username}', '{self.email}')"
    
with app.app_context():
    db.create_all()


@app.route('/add_admin', methods=['GET','POST'])
def add_admin():
    new_user = Admin(id=1, username='sanjana', email='sanjana@example.com', password='password123')
    db.session.add(new_user)
    db.session.commit()
    return "Admin added!"

@app.route('/show_admins')
def show_admins():
    admins = Admin.query.all()
    return render_template('show_admins.html', admins=admins)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        admin = Admin.query.filter_by(email=email).first()

        if admin and admin.password == password:
            return "Logged in successfully!"
        else:
            # flash('Login Unsuccessful. Please check email and password', 'danger')
            return redirect(url_for('login'))
    
    return render_template('main.html')
 
@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/info')
# def info():
#     subprocess.Popen(['python', 'database.py'])
#     return render_template('admin_list.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/employee')
def employee():
    # Start the employee Tkinter application
    subprocess.Popen(['python', 'employee.py'])
    return render_template('main.html')

@app.route('/photo')
def photo():
    # Start the employee Tkinter application
    # subprocess.Popen(['python', 'train.py'])
    return render_template('main.html')

@app.route('/attendance')
def attendance():
    # Start the employee Tkinter application
    subprocess.Popen(['python', 'attendance.py'])
    return render_template('main.html')

@app.route('/train')
def train():
    # Start the employee Tkinter application
    subprocess.Popen(['python', 'train.py'])
    return render_template('main.html')

@app.route('/detect1')
def detect1():
    # Start the employee Tkinter application
    subprocess.Popen(['python', 'face_recognise.py'])
    return render_template('index.html')

@app.route('/detect2')
def detect2():
    # Start the employee Tkinter application
    subprocess.Popen(['python', 'face_recognise.py'])
    return render_template('main.html')

@app.route('/exit')
def exit():
    # Start the employee Tkinter application
    # subprocess.Popen(['python', 'train.py'])
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)
