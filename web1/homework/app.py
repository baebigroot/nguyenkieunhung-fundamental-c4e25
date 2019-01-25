from flask import Flask, redirect

app = Flask(__name__)

@app.route("/about-me")
def aboutme():
    return """
        Name: Nguyen Kieu Nhung<br/>Age: 19<br/>Job: Student<br/>Song currently playing: Another day of sun - LaLaLand
    """

@app.route("/school")
def school():
    return  redirect("http://techkids.vn ")


if __name__ == "__main__":    
    app.run(debug=True)


