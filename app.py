# ==========================================
# EVENT MANAGEMENT SYSTEM (Python Project)
# ==========================================

import datetime

# ---------- Dummy Database ----------

users_db = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}

membership_db = {}


# ---------- Helper Functions ----------

def generate_membership_id():
    return "M" + str(len(membership_db) + 1).zfill(3)


def calculate_end_date(months):
    today = datetime.date.today()
    return today + datetime.timedelta(days=30 * months)


# ---------- Maintenance Module (Admin Only) ----------

def maintenance_menu():
    print("\n--- Maintenance Menu (Admin Only) ---")
    print("1. View System Info")
    print("2. Back")

    choice = input("Enter choice: ")

    if choice == "1":
        print("System Running Successfully")
    else:
        return


# ---------- Add Membership ----------

def add_membership():
    print("\n--- Add Membership ---")

    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")

    if not name or not email or not phone:
        print("All fields are mandatory!")
        return

    print("\nSelect Duration:")
    print("1. 6 months (Default)")
    print("2. 1 year")
    print("3. 2 years")

    choice = input("Enter choice: ") or "1"

    duration_map = {
        "1": (6, "6 months"),
        "2": (12, "1 year"),
        "3": (24, "2 years")
    }

    months, duration_text = duration_map.get(choice, (6, "6 months"))

    mem_id = generate_membership_id()
    start_date = datetime.date.today()
    end_date = calculate_end_date(months)

    membership_db[mem_id] = {
        "name": name,
        "email": email,
        "phone": phone,
        "duration": duration_text,
        "start": start_date,
        "end": end_date,
        "status": "Active"
    }

    print(f"Membership Created! ID = {mem_id}")


# ---------- Update Membership ----------

def update_membership():
    print("\n--- Update Membership ---")

    mem_id = input("Enter Membership ID: ")

    if mem_id not in membership_db:
        print("Membership not found!")
        return

    data = membership_db[mem_id]

    print("\nMember Details:")

    import datetime

    users_db = {
        "admin": {"password": "admin123", "role": "admin"},
        "user": {"password": "user123", "role": "user"}
    }




    def generate_membership_id():
        return "M" + str(len(membership_db) + 1).zfill(3)


    def calculate_end_date(months):
        today = datetime.date.today()
        return today + datetime.timedelta(days=30 * months)


    def maintenance_menu():
        print("\nAdmin stuff")
        print("1. Info")
        print("2. Back")
        choice = input("Pick: ")
        if choice == "1":
            print("All good.")
        else:
            return


    def add_membership():
        print("\nAdd new member")
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        if not name or not email or not phone:
            print("Fill everything!")
            return
        print("\nHow long?")
        print("1. 6 months (default)")
        print("2. 1 year")
        print("3. 2 years")
# ---------- Transactions Module ----------

def transactions():
    print("\n--- Transactions ---")
    print("1. Add Membership")
    print("2. Update Membership")
    print("3. Back")

    choice = input("Enter choice: ")

    if choice == "1":
        add_membership()
    elif choice == "2":
        update_membership()
    else:
        return


# ---------- Admin Dashboard ----------

def admin_dashboard():
    while True:
        print("\n===== ADMIN DASHBOARD =====")
        print("1. Maintenance")
        print("2. Reports")
        print("3. Transactions")
        print("4. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            maintenance_menu()
        elif choice == "2":
            reports()
        elif choice == "3":
            transactions()
        elif choice == "4":
            break
        else:
            print("Invalid choice")


# ---------- User Dashboard ----------

def user_dashboard():
    while True:
        print("\n===== USER DASHBOARD =====")
        print("1. Reports")
        print("2. Transactions")
        print("3. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            reports()
        elif choice == "2":
            transactions()
        elif choice == "3":
            break
        else:
            print("Invalid choice")


# ---------- Login System ----------

def login():
    print("\n===== LOGIN =====")

    username = input("Username: ")
    password = input("Password: ")

    if username in users_db and users_db[username]["password"] == password:
        role = users_db[username]["role"]

        print("Login Successful!")

        if role == "admin":
            admin_dashboard()
        else:
            user_dashboard()
    else:
        print("Invalid credentials")


# ---------- Main Program ----------

while True:
    login()

    again = input("\nLogin again? (y/n): ").lower()
    if again != "y":
        print("Exiting system...")
        break
