# qlip
**Qlip** is a backend URL shortener built with Python and FastAPI that goes beyond the basics — it persists links in a real SQLite database, tracks click counts, generates a scannable QR code for every shortened link, and flags suspicious URLs (like raw IP-based links) before shortening them as a basic phishing-safety layer.
