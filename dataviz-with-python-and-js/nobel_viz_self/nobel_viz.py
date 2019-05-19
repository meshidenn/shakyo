from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

#winners = [
#    {'name': 'Albert Einstein', 'category': 'Physics'},
#    {'name': 'V.S. Naipaul', 'category': 'Literature'},
#    {'name': 'Dorothy Bodgkin', 'category': 'Chemistry'}
#]

#@app.route("/")
#def hello():
#    return "Hello World!"
#@app.route('/demolist')
#def demo_list():
#    return render_template('testj2.html',
#    heading="A little winners' list", winners=winners)

@app.route('/')
def root():
    return send_from_directory('.', 'templates/index.html')


if __name__ == "__main__":
    app.run(port=8000, debug=True)
