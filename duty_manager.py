# ============================================================================
# duty_manager.py
# אחריות: לוגיקה עסקית של ניהול תורנויות
# ============================================================================
from utils import *


def add_duty_to_soldier(soldier_id: int, duty_name: str, day: str) -> None:
    soldier = find_soldier_by_id(soldier_id)
    if soldier_has_duty(soldier, duty_name):
        raise ValueError("Soldier already has this duty pending")
    if find_soldier_by_id(soldier_id) is None:
        raise ValueError("Soldier doesn't exist")
    if not is_valid_day(day):
        raise ValueError("Invalid day")
    duty = {'duty_name': duty_name, 'day': day, 'status': 'pending'}
    for soldier in soldiers:
        if soldier['id'] == soldier_id:
            soldier['duties'].append(duty)
            break
    return None


def update_duty_status(soldier_id: int, duty_name: str, new_status: str) -> None:
    """
    מעדכנת את הסטטוס של תורנות.

    סוג: לוגיקה עסקית (Business Logic)

    מקבלת:
        soldier_id (int): מספר אישי של החייל
        duty_name (str): שם התורנות
        new_status (str): סטטוס חדש (pending/completed/missed)

    מחזירה:
        None - הפונקציה מעדכנת את הסטטוס או זורקת exception

    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
        KeyError: אם תורנות עם שם זה לא נמצאה לחייל
        ValueError: אם new_status לא חוקי (לא pending/completed/missed)

    למה הפונקציה קיימת:
    לוגיקה עסקית של עדכון סטטוס.
    מבצעת בדיקות ומעדכנת את הסטטוס.
    זורקת exceptions במקרה של שגיאה במקום להחזיר False.
    """
    pass


def get_soldier_duties(soldier_id: int) -> list:

    """
    מחזירה את רשימת התורנויות של חייל.

    סוג: גישה לנתונים (Data Access)

    מקבלת:
        soldier_id (int): מספר אישי של החייל

    מחזירה:
        list: רשימת תורנויות (מילונים)
              רשימה ריקה אם אין תורנויות

    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת

    למה הפונקציה קיימת:
    גישה מבוקרת לתורנויות של חייל.
    מפרידה בין הנתונים לבין הגישה אליהם.
    זורקת exception אם החייל לא קיים (במקום להחזיר רשימה ריקה).
    """
    pass