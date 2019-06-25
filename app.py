from flask import Flask, render_template, request, jsonify, redirect, json
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    # reading the posts
    with open('posts.json', "r") as f:
        posts = json.load(f)
    # getting time difference of posts
    now = datetime.now()
    time = []
    '''
    for post in posts:
        time.append(datetime.strptime(post['date'], 'insert time format') - now)
    '''
    return render_template('index.html', posts=posts, time=time)

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
        formdata['id'] = 1
    else:
        formdata['id'] = posts[-1]['id'] + 1
    posts.append(formdata)
    # write the post
    with open('posts.json', "w") as f:
        json.dump(posts, f, indent=2, separators=(',', ':'))

    return redirect('/')


app.run(debug=True)
