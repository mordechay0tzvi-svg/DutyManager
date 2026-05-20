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
    print("============================")
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
    try:
        name = input("name: ")
        soldier_id = int(input("id: "))

        add_soldier(soldier_id, name)

        print("====== Soldier added ======")

    except ValueError as e:
        print(f"Error: {e}")


def handle_remove_soldier() -> None:
    try:
        soldier_id = int(input("id: "))

        remove_soldier(soldier_id)

        print("====== Soldier removed ======")

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


def handle_view_soldiers() -> None:
    try:
        print(get_all_soldiers())
        print("======= End of list =======")

    except Exception as e:
        print(f"Error: {e}")


def handle_add_duty() -> None:
    try:
        soldier_id = int(input("id: "))
        duty_name = input("duty name: ")
        day = input("day: ")

        add_duty_to_soldier(soldier_id, duty_name, day)

        print("====== Duty added ======")

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


def handle_update_duty_status() -> None:
    try:
        soldier_id = int(input("id: "))
        duty = input("duty: ")
        status = input("status: ")

        update_duty_status(soldier_id, duty, status)

        print("======= Duty updated =======")

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


def handle_view_soldier_duties() -> None:
    try:
        soldier_id = int(input("id: "))

        print(get_soldier_duties(soldier_id))

        print("==================")

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


def main() -> None:
    while True:
        try:
            show_menu()

            choice = get_user_choice()

            if choice == "1":
                handle_add_soldier()

            elif choice == "2":
                handle_remove_soldier()

            elif choice == "3":
                handle_view_soldiers()

            elif choice == "4":
                handle_add_duty()

            elif choice == "5":
                handle_update_duty_status()

            elif choice == "6":
                handle_view_soldier_duties()

            elif choice == "7":
                print("Goodbye!")
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print(f"Unexpected error: {e}")


main()