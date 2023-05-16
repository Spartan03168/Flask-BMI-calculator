from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/", methods = ["GET", "POST"])
def BMI_calculator():
    bmi = 0
    if request.method == "POST":
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        bmi = weight / (height ** 2)

    return render_template("index.html", bmi = bmi)

app.run(debug= True)