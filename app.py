from flask import Flask
<<<<<<< HEAD
import windows
=======
import linux
>>>>>>> 3cd0c1551de9bf702c38adf8c1eb7a456d9411dd

app = Flask(__name__)

@app.route("/")
def hello():
    return "updated Flask sample application on azure hghapp service updated verrsion-4"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 0))
    app.run(debug=True,host='0.0.0.0',port=port)
