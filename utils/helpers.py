import re

def count_words(text: str) -> int:
    return len(re.findall(r'\w+', text))

def format_tags(tags):
    return ', '.join(tags) if tags else '-'
