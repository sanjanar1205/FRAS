from flask import Flask, redirect, request, render_template, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
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

@app.route('/add_admin', methods=['POST'])
def add_admin():
    new_user = Admin(id=1, username='sanjana', email='sanjana@example.com', password='password123')
    db.session.add(new_user)
    db.session.commit()
    return "Admin added!"

@app.route('/admin')
def admin():
    users = Admin.query.all()
    return render_template('admin_list.html', users=users)


# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
        
#         admin = Admin.query.filter_by(email=email).first()

#         if admin and admin.password == password:
#             return "Logged in successfully!"
#         else:
#             flash('Login Unsuccessful. Please check email and password', 'danger')
#             return redirect(url_for('login'))
    
#     return render_template('main.html')
