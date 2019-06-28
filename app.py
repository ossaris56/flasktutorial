from flask import Flask, render_template, request, jsonify, redirect, url_for
import uuid, json

app = Flask(__name__)

# reads json file and appends empty dictionary if json file is empty
def read_json(json_file):
    with open(json_file, "r") as f:
        try:
            posts = json.load(f)
        except ValueError:
            posts = {}
        return posts

# writes into the json file 
def write_json(json_file, data):
    with open(json_file, "w") as f:
        json.dump(data, f, indent=2, separators=(',', ':'), sort_keys=False)

@app.route("/")
def index():
    # TODO: load json and reverse posts

    return render_template()

@app.route('/postdiscussion')
def post_page():
    return render_template()

@app.route('/post', methods=['POST'])
def post():
    # TODO: load json, change form data into dict and populate comments, points and post_id
    # TODO: set post_id as key and formdata dict as value
    # TODO: write posts into json

    return redirect()

@app.route('/comments/<string:post_id>', methods=['POST', 'GET'])
def comments(post_id):
    # TODO: load json, get data of post from the post id
    
    # return post data to template
    return render_template()

@app.route('/comments/<string:post_id>/postcomment', methods=['POST'])
def postcomment(post_id):
    # TODO: load json, append comment into the comments list of the post
    # TODO: write posts into json
    # TODO: redirect while returning post id

    return redirect()

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
