from flask import Flask, render_template, request, jsonify, redirect, json

app = Flask(__name__)

@app.route("/")
def index():
    # reading the posts
    with open('posts.json', "r") as f:
        posts = json.load(f)
    print(posts)
    return render_template('index.html')

@app.route('/postdiscussion', methods=['POST', 'GET'])
def post_page():
    return render_template('post.html')

@app.route('/post', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        # reading the posts
        with open('posts.json', "r") as f:
            posts = json.load(f)
        # add post to posts
        formdata = request.form.to_dict()
        formdata['comments'] = []
        posts.append(formdata)
        # write the post
        with open('posts.json', "w") as f:
            json.dump(posts, f, sort_keys = True, indent=2, separators=(',', ':'))

        return redirect('/')
    else: # GET http method
        return render_template('post.html')

app.run(debug=True)
