from hms.database import initialize
from hms.students import add_student, list_students, find_student, remove_student
from hms.rooms import room_status, available_rooms, summary

def show_students():
    rows=list_students()
    if not rows:
        print("No students registered.")
    else:
        print("\nID | Name | Phone | Room")
        for r in rows: print(" | ".join(map(str,r)))

def show_rooms(rows):
    print("\nRoom | Capacity | Occupied | Available")
    for r in rows: print(" | ".join(map(str,r)))

def main():
    initialize()
    while True:
        print("\n--- HOSTEL MANAGEMENT SYSTEM ---")
        print("1. Add student\n2. View students\n3. Search student")
        print("4. Vacate room (remove student)\n5. View room status")
        print("6. View available rooms\n7. Summary\n8. Exit")
        choice=input("Enter choice: ").strip()
        try:
            if choice=="1":
                sid=input("Student ID: ")
                name=input("Name: ")
                phone=input("Phone (10 digits): ")
                show_rooms(available_rooms())
                room=int(input("Room number: "))
                add_student(sid,name,phone,room)
                print("Student added successfully.")
            elif choice=="2": show_students()
            elif choice=="3":
                row=find_student(input("Student ID: "))
                print(" | ".join(map(str,row)) if row else "Student not found.")
            elif choice=="4":
                if remove_student(input("Student ID: ")): print("Student removed; room is available.")
                else: print("Student not found.")
            elif choice=="5": show_rooms(room_status())
            elif choice=="6": show_rooms(available_rooms())
            elif choice=="7":
                total,occupied,available=summary()
                print(f"Students: {total}\nOccupied spaces: {occupied}\nAvailable spaces: {available}")
            elif choice=="8":
                print("Goodbye."); break
            else: print("Invalid choice.")
        except (ValueError, Exception) as e:
            print("Error:",e)

if __name__=="__main__":
    main()
