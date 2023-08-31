import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.user_repository import UserRepository
# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/', methods=['GET'])
def get_all_spaces():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all()
    return render_template('homepage.html', spaces=spaces)

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')


@app.route('/users/<id>', methods=['GET'])
def get_single_user_by_id(id):
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    user = repository.find(id)
    return render_template('user.html', user=user)


@app.route('/spaces/<id>', methods=['GET'])
def get_single_space_by_id(id):
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space = repository.find(id)
    return render_template('user.html', space=user)


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
