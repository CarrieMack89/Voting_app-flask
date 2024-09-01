from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

dates = ["05-10-2024", "07-09-2024", "21-12-2024", "05-01-2025"]  # add your dates here
votes = {date: 0 for date in dates}


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected_date = request.form.get("date")
        if selected_date:
            votes[selected_date] += 1
            return redirect(url_for("results"))

    return render_template("index.html", dates=dates)


@app.route("/results")
def results():
    most_voted = max(votes, key=votes.get)
    return render_template("results.html",
                           votes=votes, most_voted=most_voted)


if __name__ == "__main__":
    app.run(host="0.0.0.0.", port=5000, debug=True)
