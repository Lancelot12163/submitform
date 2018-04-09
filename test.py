from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)
app.config.from_object('config.Config');

@app.route('/users/<id>')
def hello_users(id):
    return "users: " + id

	
@app.route('/query_use')
def query_user():
    id = request.args.get('id')
    return "query_user: id " + id

@app.route('/query_url')
def query_url():
    return 'query_url' + url_for('query_user')
	
if __name__ == '__main__':
	app.debug=True
	app.run('127.0.0.1', port = 5010)