from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

PDF_DIR = BASE_DIR / "pdfs"

VECTOR_STORE = BASE_DIR / "vector_store"

PDF_DIR.mkdir(exist_ok=True)

VECTOR_STORE.mkdir(exist_ok=True)