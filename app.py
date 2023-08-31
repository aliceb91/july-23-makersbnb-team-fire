import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.user_repository import UserRepository
from lib.booking import Booking
from lib.booking_repository import BookingRepository
import datetime

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/', methods=['GET'])
def get_all_spaces():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all()
    return render_template('homepage.html', spaces=spaces)

@app.route('/spaces/<id>', methods=['GET'])
def get_space_page(id):
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space = repository.find(id)
    return render_template("space_page.html", space=space)

@app.route('/booking_confirmed', methods=['GET'])
def booking_confirmed():
    return render_template("booking_confirmed.html")

@app.route('/spaces/<id>', methods=['POST'])
def make_space_booking(id):
    connection = get_flask_database_connection(app)
    space_repository = SpaceRepository(connection)
    space = space_repository.find(id)
    guest_id_string = request.form['guest_id']
    guest_id = int(guest_id_string)
    booking = Booking(None, space.user_id, guest_id, space.id, request.form['date'])
    booking_repository = BookingRepository(connection)
    booking_repository.add(booking)
    return redirect("/booking_confirmed")

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

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
