from flask import Flask, request, render_template
import html
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def view_list():
  return render_template("index.html")

if __name__ == "__main__":
  app.run()
