# ============================================================================
# soldier_manager.py
# אחריות: לוגיקה עסקית של ניהול חיילים
# ============================================================================
import utils
from data import soldiers
from utils import is_valid_name


def add_soldier(soldier_id: int, name: str) -> None:
    if not is_valid_name(name):
        raise ValueError('name is not valid')
    for soldier in soldiers:
        if soldier["id"] == soldier_id:
            raise ValueError("id already in system")

    soldiers.append({"id": soldier_id, "name": name, 'duties' : []})



def remove_soldier(soldier_id: int) -> None:
    """
    מסירה חייל מהמערכת לפי id.

    סוג: לוגיקה עסקית (Business Logic)

    מקבלת:
        soldier_id (int): מספר אישי של החייל

    מחזירה:
        None - הפונקציה מסירה את החייל או זורקת exception

    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת

    למה הפונקציה קיימת:
    לוגיקה עסקית של הסרת חייל.
    מבצעת בדיקת קיום ומסירה מהנתונים.
    זורקת exception במקרה שהחייל לא קיים.
    """
    pass


def get_all_soldiers() -> list:
    return soldiers
