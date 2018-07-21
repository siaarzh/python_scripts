import csv
import io
import cherrypy
from flask import Blueprint
from paste.translogger import TransLogger

main = Blueprint('main', __name__)
import json
from flask import Flask, request


@main.route("/<int:user_id>/ratings", methods=["POST"])
def add_ratings(user_id):
	# get the ratings from the Flask POST request object
	# ratings_list = request.form.keys()[0].strip().split("\n")
	f = request.files['data']
	stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
	csv_input = csv.reader(stream)
	ratings_list = []
	for row in csv_input:
		ratings_list.append(row)
	#ratings_list = list(request.form.keys())[0].strip().split("\n")  # Python 3 fix
	#ratings_list = list(map(lambda x: x.split(","), ratings_list))
	# create a list with the format required by the negine (user_id, movie_id, rating)
	ratings = list(map(lambda x: (user_id, int(x[0]), float(x[1])), ratings_list))
	print(ratings)
	# add them to the model using then engine API
	# recommendation_engine.add_ratings(ratings)

	return json.dumps(ratings)


def create_app():

	app = Flask(__name__)
	app.register_blueprint(main)
	return app


def run_server(app):
	# Enable WSGI access logging via Paste
	app_logged = TransLogger(app)

	# Mount the WSGI callable object (app) on the root directory
	cherrypy.tree.graft(app_logged, '/')

	# Set the configuration of the web server
	cherrypy.config.update({
		'engine.autoreload.on': True,
		'log.screen': True,
		'server.socket_port': 5000,
		'server.socket_host': '127.0.0.1'
	})

	# Start the CherryPy WSGI web server
	cherrypy.engine.start()
	cherrypy.engine.block()


if __name__ == "__main__":
	app = create_app()
	# start web server
	run_server(app)