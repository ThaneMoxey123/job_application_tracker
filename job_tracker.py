import csv
import os

applications = []

def show_menu():
    print("===== Job Application Tracker =====")
    print("1. Add new application")
    print("2. View all applications")
    print("3. Update application status")
    print("4. Quit")

def add_application():
    print("\n----- Add New Application -----")
    company = input("Company name: ")
    role = input("Job title / role: ")
    date = input("Date applied (e.g. 10/04/2026): ")
    
    application = {
        "company": company,
        "role": role,
        "date": date,
        "status": "Applied"
    }
    
    applications.append(application)
    print(f"\n✅ Application to {company} added successfully!")

def view_applications():
    print("\n----- All Applications -----")
    
    if len(applications) == 0:
        print("No applications yet. Start adding some!")
        return
    
    for i, app in enumerate(applications):
        print(f"\n[{i + 1}] Company:  {app['company']}")
        print(f"    Role:     {app['role']}")
        print(f"    Date:     {app['date']}")
        print(f"    Status:   {app['status']}")
    
    print(f"\nTotal applications: {len(applications)}")

def update_status():
    print("\n----- Update Application Status -----")
    
    if len(applications) == 0:
        print("No applications yet. Start adding some!")
        return
    
    view_applications()
    
    choice = input("\nEnter the number of the application to update: ")
    index = int(choice) - 1
    
    if index < 0 or index >= len(applications):
        print("Invalid number. Please try again.")
        return
    
    print("\nSelect new status:")
    print("1. Applied")
    print("2. Interview")
    print("3. Offer")
    print("4. Rejected")
    
    status_choice = input("\nChoose a status: ")
    
    if status_choice == "1":
        applications[index]["status"] = "Applied"
    elif status_choice == "2":
        applications[index]["status"] = "Interview"
    elif status_choice == "3":
        applications[index]["status"] = "Offer 🎉"
    elif status_choice == "4":
        applications[index]["status"] = "Rejected"
    else:
        print("Invalid choice.")
        return
    
    print(f"\n✅ Status updated to: {applications[index]['status']}")

def save_to_csv():
    with open("applications.csv", "w", newline="") as file:
        fieldnames = ["company", "role", "date", "status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(applications)
    print("💾 Applications saved!")

def load_from_csv():
    if not os.path.exists("applications.csv"):
        return
    with open("applications.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            applications.append(row)

def main():
    load_from_csv()
    while True:
        show_menu()
        choice = input("\nChoose an option: ")

        if choice == "1":
            add_application()
            save_to_csv()
        elif choice == "2":
            view_applications()
        elif choice == "3":
            update_status()
            save_to_csv()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")

main()


    