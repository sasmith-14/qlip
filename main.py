from database import SessionLocal
from fastapi import FastAPI
from models import ShortenRequest
from fastapi.responses import RedirectResponse
import string
import random
from database import Base, engine
from models_db import URL
import qrcode
import re

app = FastAPI()

def is_ip_address(url):
    pattern = r"\d+\.\d+\.\d+\.\d+"
    return re.search(pattern, url) is not None

def generate_short_code():
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choice(characters) for i in range(5))
    return code


@app.get("/")
def home():
    return {"message": "qlip is running"}

@app.post("/shorten")
def shorten(request: ShortenRequest):
    if is_ip_address(request.url):
        return {"error": "IP address is not allowed"}
    code = generate_short_code()
    db = SessionLocal()
    new_url = URL(short_code = code, long_url = request.url)
    db.add(new_url)
    db.commit()
    db.close()

    short_url = f"http://localhost:8000/{code}"
    img = qrcode.make(short_url)
    img.save(f"qr_codes/{code}.png")

    return {"short_code": code}

@app.get("/admin/all-links")
def debug():
    db = SessionLocal()
    urls = db.query(URL).all()
    db.close()
    return urls

@app.get("/{code}")
def redirect_to_long_url(code: str):
    db = SessionLocal()
    result = db.query(URL).filter(URL.short_code == code).first()
    
    if result is None:
        db.close()
        return {"error": "Short code not found"}
    
    result.clicks += 1
    long_url = result.long_url
    db.commit()
    db.close()
    return RedirectResponse(long_url)