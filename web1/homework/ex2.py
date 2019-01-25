from flask import Flask, render_template

app = Flask(__name__)

database = {
    "Nhung": {
                "Name": "Nguyen Kieu Nhung",
                "Gender": "Male",
                "Age": "Younger than you",
                "Hobbies": "CLASSIFIED",
              },
    "Christ": {
                "Name": "Jesus Christ",
                "Gender": "Female",
                "Age": "Older than your grandma",
                "Hobbies": "Walk on water, swim on land",
                }
}

@app.route("/user/<username>")
def user(username):
    user1 = {}
    f = "sun"
    for i, j in database.items():
        if i.lower() == username:
            for k, l in j.items():
                user1[k] = l
            f = "moon"

    if f == "sun":
        return "User not found"
    else: 
        return render_template("user.html", user1=user1)

if __name__ == "__main__":
    app.run(debug=True)