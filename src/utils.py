import json
from typing import Dict, List


def load_transactions(file_path: str) -> List[Dict]:
    """Загружает транзакции из JSON-файла"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return []
