"""Модуль для обработки списков словарей (фильтрация, сортировка)."""

from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Фильтрует список словарей по значению ключа 'state'."""
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Сортирует список словарей по дате (ключ 'date')."""

    def parse_date(item: Dict[str, Any]) -> datetime:
        return datetime.fromisoformat(item["date"])

    return sorted(data, key=parse_date, reverse=reverse)
