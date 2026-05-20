# ============================================================================
# main.py
# אחריות: תפריט ראשי, קלט מהמשתמש, ניתוב לפונקציות
# ============================================================================
from utils import *
from soldier_manager import *
from duty_manager import *


def show_menu() -> None:
    print("============================")
    print("Welcome to Duty Manager")
    print("===========================")
    print("Choose an option:")
    print("1. Add soldier")
    print("2. Remove soldier")
    print("3. See list of soldiers")
    print("4. Add duty to soldier")
    print("5. Update status of duty")
    print("6. See soldier duties")
    print("7. Exit")


def get_user_choice() -> str:
    return input()


def handle_add_soldier() -> None:
    name = input("name:")
    id = int(input("id:"))
    add_soldier(id, name)


def handle_remove_soldier() -> None:
    id = int(input("id:"))
    remove_soldier(id)


def handle_view_soldiers() -> None:
    print(get_all_soldiers())


def handle_add_duty() -> None:
    id = int(input("id:"))
    duty_name = input("duty name:")
    day = input("day")
    add_duty_to_soldier(id, duty_name,  day)


def handle_update_duty_status() -> None:
    id = int(input("id:"))
    duty = input("duty:")
    status = input("status:")
    update_duty_status(id, duty, status)


def handle_view_soldier_duties() -> None:
    id = int(input("id:"))
    print(get_soldier_duties(id))


def main() -> None:
    while True:
        show_menu()
        choice = get_user_choice()
        if choice == "1":
            handle_add_soldier()
            continue
        if choice == "2":
            handle_remove_soldier()
            continue
        if choice == "3":
            handle_view_soldiers()
            continue
        if choice == "4":
            handle_add_duty()
            continue
        if choice == "5":
            handle_update_duty_status()
            continue
        if choice == "6":
            handle_view_soldier_duties()
            continue
        if choice == "7":
            break



main()
