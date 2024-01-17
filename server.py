from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')



@app.route('/blog/<int:post_id>')
def blog_id(post_id=None):
    return render_template('blog.html', id=post_id)

@app.route('/blog')
def blog():
    return render_template('blog.html')