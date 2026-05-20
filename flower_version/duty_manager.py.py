# ============================================================================
# duty_manager.py
# אחריות: לוגיקה עסקית של ניהול תורנויות
# ============================================================================
from utils import *
from data import soldiers


def add_duty_to_soldier(soldier_id: int, duty_name: str, day: str) -> None:
    soldier = find_soldier_by_id(soldier_id)

    if soldier is None:
        raise ValueError("Soldier doesn't exist")

    if soldier_has_duty(soldier, duty_name):
        raise ValueError("Soldier already has this duty")

    if not is_valid_day(day):
        raise ValueError("Invalid day")

    duty = {
        'duty_name': duty_name,
        'day': day,
        'status': 'pending'
    }

    for s in soldiers:
        if s['id'] == soldier_id:
            s['duties'].append(duty)
            break

    return None


def update_duty_status(soldier_id: int, duty_name: str, new_status: str) -> None:
    if not is_valid_status(new_status):
        raise ValueError("Invalid new status")

    soldier = find_soldier_by_id(soldier_id)

    if soldier is None:
        raise KeyError("Soldier doesn't exist")

    if not soldier_has_duty(soldier, duty_name):
        raise ValueError("Soldier does not have this duty")

    for s in soldiers:
        if s['id'] == soldier_id:
            duties = get_soldier_duties(soldier_id)

            for d in duties:
                if d['duty_name'] == duty_name:
                    d['status'] = new_status

    return None


def get_soldier_duties(soldier_id: int) -> list:
    soldier = find_soldier_by_id(soldier_id)

    if soldier is None:
        raise ValueError("Soldier doesn't exist")

    return soldier['duties']