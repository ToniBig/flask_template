from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user  # type: ignore
from werkzeug.security import generate_password_hash, check_password_hash

# Create blueprint
auth = Blueprint('auth', __name__)

# Setup Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # type: ignore

# In-memory user store for demonstration purposes
users: dict[str, 'User'] = {}

# User class to integrate with Flask-Login


class User(UserMixin):
    def __init__(self, id: int, username: str, password_hash: str):
        self.id = id
        self.username = username
        self.password_hash = password_hash

# Flask-Login user loader


@login_manager.user_loader  # type: ignore
def load_user(user_id: str):
    return users.get(user_id)

# Registration route


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users:
            flash('Username already exists.')
            return redirect(url_for('auth.register'))

        # Hash the password and store the user
        password_hash = generate_password_hash(password)  # type: ignore
        user = User(id=len(users) + 1, username=username,  # type: ignore
                    password_hash=password_hash)
        users[str(user.id)] = user
        flash('Registration successful! Please log in.')
        return redirect(url_for('auth.login'))

    return render_template('register.html')

# Login route


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Search for the user
        user = next((u for u in users.values()
                    if u.username == username), None)

        if user and check_password_hash(user.password_hash, password):  # type: ignore
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password.')

    return render_template('login.html')

# Logout route


@auth.route('/logout')
@login_required  # type: ignore
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('auth.login'))
