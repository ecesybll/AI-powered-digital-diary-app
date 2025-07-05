import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'config', 'diary.db')

# Google Gemini API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', 'AIzaSyBrGV8J2tl2RZ3iTY2kZs7UqgHa2LdlNwQ')
GEMINI_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent'

# Uygulama ayarları
def get_config():
    return {
        'DB_PATH': DB_PATH,
        'GEMINI_API_KEY': GEMINI_API_KEY,
        'GEMINI_API_URL': GEMINI_API_URL
    }
