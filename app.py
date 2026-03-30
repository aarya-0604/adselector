from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__, static_folder='static')

ads = ["ad1.jpg", "ad2.jpg", "ad3.jpg", "ad4.jpg"]

ad_stats = {
    ad: {"clicks": 0, "shown": 0}
    for ad in ads
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_ad")
def get_ad():
    ad = random.choice(ads)
    ad_stats[ad]["shown"] += 1
    return jsonify({"ad": ad})

@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.json
    ad = data["ad"]
    clicked = data["clicked"]

    if clicked:
        ad_stats[ad]["clicks"] += 1

    return jsonify(ad_stats)

if __name__ == "__main__":
    app.run(debug=True)