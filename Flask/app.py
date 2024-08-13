from flask import Flask, render_template

app = Flask(__name__) # create an instance of the Flask class



@app.route('/about')
def about():
    return "This is the About page"

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__': # run the application
    app.run(debug=True) # run the app on http:// localhost:5000/ by default 
