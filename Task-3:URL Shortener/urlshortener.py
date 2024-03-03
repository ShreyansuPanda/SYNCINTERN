import json
from flask import Flask, render_template, redirect, request
import pyshorteners
import webview

app = Flask(__name__)
shortened_urls = {}

def shorten_url(long_url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(long_url)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        long_url = request.form['long_url']
        short_url = shorten_url(long_url)
        shortened_urls[short_url] = long_url
        with open("urls.json", "w") as f:
            json.dump(shortened_urls, f)
        return f"Shortened URL: {short_url}"
    return render_template("INDEX.html")

@app.route("/<short_url>")
def redirect_url(short_url):
    long_url = shortened_urls.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "URL not found", 404

if __name__ == "__main__":
    with open("urls.json", "r") as f:
        shortened_urls = json.load(f)
    app.run(debug=True)
    
