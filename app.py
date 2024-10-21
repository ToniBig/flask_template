from flask import Flask, render_template
from blueprints.auth import auth, login_manager

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Initialize Flask-Login
login_manager.init_app(app)  # type: ignore

# Register Blueprints
app.register_blueprint(auth, url_prefix='/auth')

# Simple homepage route


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
