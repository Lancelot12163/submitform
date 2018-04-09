from flask import Flask, render_template
app = Flask(__name__)

@app.route('/proj/')
def projects():
    return '<h2>The projec page<h2>'

@app.route('/')
def index():
    return 'Index Page'

@app.route('/user/<string:us>')
def user(us):
    # show the user profile for that user
    return 'User %s' % us

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/new/')
def hello():
    return render_template('new.html')
	
if __name__ == '__main__':
	app.run(debug = True)