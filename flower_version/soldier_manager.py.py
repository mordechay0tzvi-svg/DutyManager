# ============================================================================
# soldier_manager.py
# אחריות: לוגיקה עסקית של ניהול חיילים
# ============================================================================
from utils import *
from data import soldiers


def add_soldier(soldier_id: int, name: str) -> None:
    if not is_valid_name(name):
        raise ValueError('name is not valid')

    for soldier in soldiers:
        if soldier["id"] == soldier_id:
            raise ValueError("id already in system")

    soldiers.append({
        "id": soldier_id,
        "name": name,
        'duties': []
    })


def remove_soldier(soldier_id: int) -> None:
    soldier = find_soldier_by_id(soldier_id)

    if soldier is None:
        raise KeyError("soldier not found")

    for s in soldiers:
        if s['id'] == soldier_id:
            soldiers.remove(s)
            break

    return None


def get_all_soldiers() -> list:
    return soldiers