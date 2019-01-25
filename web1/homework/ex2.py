from flask import Flask, render_template

app = Flask(__name__)

database = {
    "Nhung": {
                "name": "Nguyen Kieu Nhung",
                "gender": "Male",
                "age": "10",
                "hobbies": "classified",
              },
    "Christ": {
                "name": "Jesus Christ",
                "gender": "Female",
                "age": "2019",
                "hobbies": "walk on water, swim on land",
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