# ============================================================================
# utils.py
# אחריות: פונקציות עזר שחוזרות על עצמן
# ============================================================================

def find_soldier_by_id(soldier_id: int) -> dict | None:
    """
    מחפשת חייל לפי id ומחזירה אותו.

    סוג: פונקציית עזר (Helper Function)

    מקבלת:
        soldier_id (int): מספר אישי של החייל

    מחזירה:
        dict | None: מילון של החייל אם נמצא, None אם לא נמצא

    זורקת: כלום - מחזירה None במקרה שלא נמצא

    למה הפונקציה קיימת:
    פונקציה זו משמשת הרבה מקומות במערכת (DRY).
    במקום לחזור על לולאת חיפוש בכל פונקציה,
    יש פונקציה אחת שעושה את זה.
    מחזירה None במקום לזרוק exception - מאפשרת גמישות.
    """
    pass


def find_duty_by_name(duties: list, duty_name: str) -> dict | None:
    """
    מחפשת תורנות לפי שם ברשימת תורנויות.

    סוג: פונקציית עזר (Helper Function)

    מקבלת:
        duties (list): רשימת תורנויות
        duty_name (str): שם התורנות לחיפוש

    מחזירה:
        dict | None: מילון של התורנות אם נמצאה, None אם לא נמצאה

    זורקת: כלום - מחזירה None במקרה שלא נמצא

    למה הפונקציה קיימת:
    פונקציה זו משמשת במספר מקומות (הוספת תורנות, עדכון סטטוס).
    הפרדה של לוגיקת החיפוש למקום אחד.
    מחזירה None במקום לזרוק exception - מאפשרת גמישות.
    """
    pass


def is_valid_status(status: str) -> bool:
    return status in ['pending','completed','missed']


def is_valid_name(name: str) -> bool:
    if name:
        return True
    return False


def soldier_has_duty(soldier: dict, duty_name: str) -> bool:
    for duty in soldier['duties']:
        if duty['name'] == duty_name and duty['status'] == 'pending':
            return True
    return False


def is_valid_day(day: str) -> bool:
    return day in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday']
