from flask import Flask, request, render_template
import cloudinary
import cloudinary.uploader
from serpapi import GoogleSearch
import os

app = Flask(__name__)

os.getenv('CLOUD')
cloudinary.config(
    cloud_name=os.getenv('CLOUD_NAME'),
    api_key=os.getenv('CLOUD_API'),
    api_secret=os.getenv('CLOUD_SECRET')
)

SERPAPI_KEY = os.getenv('SERPAPI_KEY')

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "image" not in request.files:
        return "No image uploaded", 400

    file = request.files["image"]
    
    result = cloudinary.uploader.upload(file)
    image_url = result["secure_url"]

    params = {
        "engine": "google_lens",
        "url": image_url,
        "api_key": SERPAPI_KEY
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    visual_matches = results.get("visual_matches", [])
    search_results = [{"title": match["title"], "link": match["link"]} for match in visual_matches]

    return render_template("index.html", image_url=image_url, search_results=search_results)

if __name__ == "__main__":
    app.run(debug=True)
