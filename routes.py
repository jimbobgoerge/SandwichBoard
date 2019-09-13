from flask import *
import html
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def view_list():
  user_file = ""
  with open("sandwich_info.json", "r") as item:
      user_file = item.read().rstrip("\n\r")
      print(type(user_file))
  return render_template("index.html", user_file=user_file)

if __name__ == "__main__":
  app.run()
