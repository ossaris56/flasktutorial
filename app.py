from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/postdiscussion', methods=['POST', 'GET'])
def post_page():
   return render_template('post.html')

def post():
    if request.method == 'POST':
        with open('post.json', 'w') as f:
            json.dump(request.form, f)
            return redirect('/')
        return redirect('/post_page')

app.run(debug=True)
