# Smart Complaint Management System

complaints = []
complaint_id = 1

def register_complaint():
    global complaint_id

    name = input("Enter your name: ")
    category = input("Enter complaint category: ")
    description = input("Enter complaint description: ")

    complaint = {
        "ID": complaint_id,
        "Name": name,
        "Category": category,
        "Description": description,
        "Status": "Pending"
    }

    complaints.append(complaint)

    print("\nComplaint Registered Successfully!")
    print("Complaint ID:", complaint_id)

    complaint_id += 1


def view_complaints():
    if len(complaints) == 0:
        print("\nNo complaints found.")
        return

    print("\n===== ALL COMPLAINTS =====")

    for complaint in complaints:
        print("\nComplaint ID:", complaint["ID"])
        print("Name:", complaint["Name"])
        print("Category:", complaint["Category"])
        print("Description:", complaint["Description"])
        print("Status:", complaint["Status"])


def update_status():
    if len(complaints) == 0:
        print("\nNo complaints available.")
        return

    cid = int(input("Enter Complaint ID: "))

    for complaint in complaints:
        if complaint["ID"] == cid:
            print("Current Status:", complaint["Status"])
            new_status = input("Enter New Status (Pending/In Progress/Resolved): ")
            complaint["Status"] = new_status
            print("Status Updated Successfully!")
            return

    print("Complaint ID not found.")


def search_complaint():
    cid = int(input("Enter Complaint ID to Search: "))

    for complaint in complaints:
        if complaint["ID"] == cid:
            print("\nComplaint Found")
            print("ID:", complaint["ID"])
            print("Name:", complaint["Name"])
            print("Category:", complaint["Category"])
            print("Description:", complaint["Description"])
            print("Status:", complaint["Status"])
            return

    print("Complaint not found.")


while True:
    print("\n========== SMART COMPLAINT MANAGEMENT SYSTEM ==========")
    print("1. Register Complaint")
    print("2. View Complaints")
    print("3. Update Complaint Status")
    print("4. Search Complaint")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_complaint()

    elif choice == "2":
        view_complaints()

    elif choice == "3":
        update_status()

    elif choice == "4":
        search_complaint()

    elif choice == "5":
        print("Thank you for using the system.")
        break

    else:
        print("Invalid Choice. Please try again.")




        