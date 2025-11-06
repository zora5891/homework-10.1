"""Модуль для обработки списков словарей (фильтрация, сортировка)."""

from typing import List, Dict, Any, Optional


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:

    """Фильтрует список словарей по значению ключа 'state'."""
    return [item for item in data if item.get("state") == state]



