import json
import os

DATA_FILE = "contacts.json"

def load_contacts():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_contacts(contacts):
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=2)
def add_contact(name, phone, email):
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"Contact '{name}' added!")
def main():
    while True:
        choice = input("Choose: add/list/exit: ").strip().lower()
        if choice == "add":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            add_contact(name, phone, email)
        elif choice == "list":
            contacts = load_contacts()
            for i, c in enumerate(contacts, 1):
                print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")
        elif choice == "exit":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
