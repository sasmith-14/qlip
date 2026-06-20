# 🔗 Qlip

**A backend URL shortener with QR code generation and basic phishing-link detection — built with Python and FastAPI.**

Qlip goes beyond a typical tutorial URL shortener. It persists data in a real SQLite database, tracks click analytics per link, auto-generates a scannable QR code for every shortened URL, and includes a basic safety layer that flags suspicious links (such as raw IP-based URLs) before shortening them.

---

## ✨ Features

- 🔗 **Shorten any URL** into a clean, shareable short link
- 🗄️ **Persistent storage** using SQLite + SQLAlchemy (data survives restarts)
- 📊 **Click tracking** — every visit to a short link increments its click count
- 📷 **Automatic QR code generation** for every shortened link
- 🛡️ **Basic phishing red-flag detection** — flags raw IP-based URLs before shortening
- ⚡ **Auto-generated interactive API docs** via FastAPI's built-in Swagger UI

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Web Framework | FastAPI |
| Data Validation | Pydantic |
| Database | SQLite |
| ORM | SQLAlchemy |
| QR Generation | `qrcode` |
| Server | Uvicorn |

---

## 📂 Project Structure

```
qlip/
├── main.py          # API routes
├── models.py        # Pydantic request/response schemas
├── models_db.py      # SQLAlchemy database table definitions
├── database.py       # Database connection & session setup
├── qr_codes/          # Generated QR code images
└── requirements.txt
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/qlip.git
cd qlip

# Install dependencies
pip3 install -r requirements.txt
```

### Running the app

```bash
python3 -m uvicorn main:app --reload
```

The API will be running at `http://localhost:8000`

Interactive API docs available at `http://localhost:8000/docs`

---

## 📖 API Reference

### Shorten a URL
```
POST /shorten
```
**Request body:**
```json
{
  "url": "https://example.com/some/very/long/path"
}
```
**Response:**
```json
{
  "short_code": "N2xiS"
}
```
Also generates a QR code saved to `qr_codes/N2xiS.png`, pointing to the short link.

---

### Redirect to original URL
```
GET /{code}
```
Redirects to the original long URL and increments the click counter for that link.

---

### View all links (internal/dev use)
```
GET /admin/all-links
```
Returns all stored URLs with their click counts.

---

## 🛡️ Safety Layer

Before shortening a URL, Qlip checks for basic phishing red flags — currently:

- **Raw IP-based URLs** (e.g. `http://192.168.1.1/login`) are flagged and rejected, since legitimate services rarely link directly via IP address.

> Note: This is a lightweight, pattern-based check — not a comprehensive phishing detection system. It serves as a first layer of protection, not a replacement for dedicated security tools.

---

## 🗺️ Roadmap

- [ ] Custom short codes
- [ ] Link expiry (time-based or click-based)
- [ ] User accounts & authentication
- [ ] Click analytics dashboard (time/location/device breakdown)
- [ ] Rate limiting
- [ ] Dockerized deployment

---

## 📄 License

MIT
