def validate_entry(title: str, content: str) -> str:
    if not title.strip():
        return "Başlık boş olamaz."
    if not content.strip():
        return "İçerik boş olamaz."
    if len(content) < 10:
        return "İçerik çok kısa."
    return ""
