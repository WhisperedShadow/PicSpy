# PicSpy 🔍

**PicSpy** is a reverse image search tool powered by **Google Lens API (via SerpAPI)** and **Cloudinary** for image storage. Upload an image, and PicSpy will find similar results across the web.

## 🚀 Features
- 🔎 **Google Lens Integration** – Search images using SerpAPI's Google Lens.
- ☁️ **Cloudinary Storage** – Securely store and manage uploaded images.
- ⚡ **Fast & Simple UI** – Easy-to-use interface for quick image searches.

## 🛠️ Technologies Used
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python)
- **APIs:**
  - [SerpAPI Google Lens API](https://serpapi.com/)
  - [Cloudinary API](https://cloudinary.com/)

## 🔧 Setup & Installation

### Prerequisites
- **Python 3** installed
- **SerpAPI Key** (Sign up on SerpAPI for a key)
- **Cloudinary Account** (Get API credentials)

### Installation Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/WhisperedShadow/PicSpy.git
   cd PicSpy
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
    venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file and add:
   ```env
   SERPAPI_KEY=your_serpapi_key
   CLOUDINARY_CLOUD_NAME=your_cloud_name
   CLOUDINARY_API_KEY=your_api_key
   CLOUDINARY_API_SECRET=your_api_secret
   ```
5. Start the Flask server:
   ```bash
   python app.py
   ```
6. Open `http://localhost:5000` in your browser.

## 📸 How It Works
1. **Upload an image** → Stored in **Cloudinary**.
2. **Send request to Google Lens API** via SerpAPI.
3. **Receive search results** & display similar images and sources.

## 🏗️ Future Enhancements
- ✅ Improve UI with animations & better UX.
- ✅ Add user authentication.
- ✅ Support multiple image formats.
- ✅ Mobile-friendly design.

## 💡 Contributing
Pull requests are welcome! Open an issue if you find any bugs or have feature requests.

## ✨ Acknowledgments
- **[SerpAPI](https://serpapi.com/)** for Google Lens API
- **[Cloudinary](https://cloudinary.com/)** for image hosting

---
🚀 **PicSpy – Find Anything by Image!**