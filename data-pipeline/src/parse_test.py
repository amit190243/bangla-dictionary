
import json
from pathlib import Path


SOURCE_FILE = Path("data/output/test_words.json")


def parse_json_list(value):
    """Parse a JSON array stored as text, handling empty values safely."""
    if not value:
        return []

    try:
        result = json.loads(value)
    except (json.JSONDecodeError, TypeError):
        return []

    if not isinstance(result, list):
        return []

    return [
        item.strip()
        for item in result
        if isinstance(item, str) and item.strip()
    ]


def main():
    records = json.loads(SOURCE_FILE.read_text(encoding="utf-8"))

    for record in records:
        definitions = parse_json_list(record.get("definition"))
        examples = parse_json_list(record.get("exmpl"))
        antonyms = parse_json_list(record.get("antonym"))

        print(f"\nWord: {record['word']}")
        print(f"Bangla: {record.get('trans', '')}")
        print(f"Definitions: {len(definitions)}")
        print(f"Examples: {len(examples)}")
        print(f"Antonyms: {len(antonyms)}")


if __name__ == "__main__":
    main()
