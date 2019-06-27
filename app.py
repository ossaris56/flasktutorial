from flask import Flask, render_template, request, jsonify, redirect, url_for
import uuid, json

app = Flask(__name__)

def read_json(json_file):
    with open(json_file, "r") as f:
        try:
            posts = json.load(f)
        except ValueError:
            posts = {}
        return posts

def write_json(json_file, data):
    with open(json_file, "w") as f:
        json.dump(data, f, indent=2, separators=(',', ':'), sort_keys=False)

@app.route("/")
def index():
    posts = read_json('posts.json')
    reversed_posts = {}
    for key in reversed(list(posts.keys())):
        reversed_posts[key] = posts[key]

    # getting time difference of posts
    return render_template('index.html', posts=reversed_posts)

@app.route('/postdiscussion')
def post_page():
    return render_template('post.html')

@app.route('/post', methods=['POST'])
def post():
    posts = read_json('posts.json')
    formdata = request.form.to_dict()
    formdata['comments'], formdata['points'], formdata['post_id'] = [], 0, uuid.uuid4().hex[:8]
    posts[formdata['post_id']] = formdata

    # write the post
    write_json('posts.json', posts)

    return redirect(url_for('index'))

@app.route('/comments/<string:post_id>/postcomment', methods=['POST'])
def postcomment(post_id):
    posts = read_json('posts.json')
    posts[post_id]['comments'].append(request.form['comment'])
    write_json('posts.json', posts)
    return redirect(url_for('comments', post_id=post_id))

@app.route('/comments/<string:post_id>', methods=['POST', 'GET'])
def comments(post_id):
    posts = read_json('posts.json')
    post_dict = posts[post_id]

    return render_template('comments.html', post_id=post_id, post_dict=post_dict)

@app.route('/upvote', methods=['POST'])
def upvote():
    data = request.get_json()
    posts = read_json('posts.json')
    posts[data['id']]['points'] += 1
    # post_dict = posts[data['id']]

    # increment the points counter
    # post_dict['points'] += 1
    write_json('posts.json', posts)
    # return jsonify(0)
    return jsonify(
        # id=post_dict['points']
        id=posts[data['id']]['points']
    )

@app.route('/downvote', methods=['POST'])
def downvote():
    data = request.get_json()
    posts = read_json('posts.json')
    # post_dict = posts[data['id']]['points'] -= 1

    posts[data['id']]['points'] -= 1

    # decrement the points counter
    # post_dict['points'] -= 1
    write_json('posts.json', posts)

    return jsonify(
        # id=post_dict['points']
        id=posts[data['id']]['points']
    )

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html'), 404

app.run(debug=True)
