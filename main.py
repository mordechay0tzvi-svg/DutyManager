# ============================================================================
# main.py
# אחריות: תפריט ראשי, קלט מהמשתמש, ניתוב לפונקציות
# ============================================================================
from utils import *
from soldier_manager import *
from duty_manager import *


def show_menu() -> None:
    """
    מציגה את התפריט הראשי למשתמש.

    מקבלת: כלום
    מחזירה: כלום (מדפיסה לקונסול)

    למה הפונקציה קיימת:
    הפרדה בין הצגת התפריט לבין הלוגיקה העסקית.
    אם נרצה לשנות את התצוגה, נשנה רק כאן.
    """
    pass


def get_user_choice() -> str:
    return input()


def handle_add_soldier() -> None:
    name = get_user_choice()
    id = int(get_user_choice())
    add_soldier(id, name)


def handle_remove_soldier() -> None:
    id = int(input())
    remove_soldier(id)


def handle_view_soldiers() -> None:
    print(get_all_soldiers())


def handle_add_duty() -> None:
    id = int(get_user_choice())
    duty_name = get_user_choice()
    day = get_user_choice()
    add_duty_to_soldier(id, duty_name,  day)


def handle_update_duty_status() -> None:
    id = int(get_user_choice())
    duty = get_user_choice()
    status = get_user_choice()
    update_duty_status(id, duty, status)


def handle_view_soldier_duties() -> None:
    """
    מטפלת בתהליך הצגת תורנויות של חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    pass


def main() -> None:
    """
    הפונקציה הראשית של התוכנית.
    מריצה לולאה ראשית שמציגה תפריט, מקבלת בחירה ומפעילה פעולה.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    נקודת הכניסה לתוכנית. מנהלת את הזרימה הראשית.
    """
    pass



