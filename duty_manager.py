# ============================================================================
# duty_manager.py
# אחריות: לוגיקה עסקית של ניהול תורנויות
# ============================================================================
from utils import *


def add_duty_to_soldier(soldier_id: int, duty_name: str, day: str) -> None:
    soldier = find_soldier_by_id(soldier_id)
    if soldier_has_duty(soldier, duty_name):
        raise ValueError("Soldier already has this duty")
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
    if not is_valid_status(new_status):
        raise ValueError("Invalid new status")
    soldier = find_soldier_by_id(soldier_id)
    if soldier is None:
        raise KeyError("Soldier doesn't exist")
    if not soldier_has_duty(soldier, duty_name):
        raise ValueError("Soldier already has this duty pending")
    for soldier in soldiers:
        if soldier['id'] == soldier_id:
            soldier['duties'][duty_name] = new_status
    return None


def get_soldier_duties(soldier_id: int) -> list:
    soldier = find_soldier_by_id(soldier_id)
    if soldier is None:
        raise ValueError("Soldier doesn't exist")
    return soldier['duties']
