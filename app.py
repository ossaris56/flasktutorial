from flask import Flask, render_template, request, jsonify, redirect, json
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    with open('posts.json', "r") as f:
        posts = json.load(f)
    # getting time difference of posts
    return render_template('index.html', posts=posts)

@app.route('/postdiscussion', methods=['POST', 'GET'])
def post_page():
    return render_template('post.html')

@app.route('/post', methods=['POST'])
def post():
    with open('posts.json', "r") as f:
        posts = json.load(f)
    # add post to posts
    formdata = request.form.to_dict()
    formdata['date'] = datetime.now()
    formdata['comments'] = []
    if len(posts) < 1:
        formdata['post_id'] = 1
    else:
        formdata['post_id'] = posts[-1]['post_id'] + 1
    posts.append(formdata)

    # write the post
    with open('posts.json', "w") as f:
        json.dump(posts, f, indent=2, separators=(',', ':'))

    return redirect('/')

@app.route('/comments/<int:post_id>')
def comments(post_id):
    with open('posts.json', "r") as f:
        posts = json.load(f)
    for post in posts:
        if post_id == post['post_id']:
            post_dict = post
    return render_template('comments.html', post_id=post_id, post_dict=post_dict)

app.run(debug=True)
