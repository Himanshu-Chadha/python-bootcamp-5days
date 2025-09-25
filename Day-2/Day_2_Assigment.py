# ---------------------------------------
# Assignment 1: Roadmap Provider Project
# ---------------------------------------

print("=== Roadmap Provider Project ===")

exp = input("Are you a Fresher or Experienced? ").strip().lower()

if exp == "fresher" :
    print("Choose your path: \n1. Web Dev \n2. App Dev \n3. DS, ML, AI")
    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "1":

        print("Learn HTML, CSS, JS, Python Django")
    elif choice == "2":
        print("Learn Java + DSA + Build Projects")
    elif choice == "3":
        print("Learn Python, Maths, R")
    else:
        print("Invalid choice")

elif exp == "experienced":
    print("Choose your path: \n1. Data Analytics \n2. Cloud Computing \n3. Front-end")
    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "1":
        print("Learn Python, Excel, PowerBI")
    elif choice == "2":
        print("Learn DevOps and Python for Automation")
    elif choice == "3":
        print("Learn Python and Django for Backend")
    else:
        print("Invalid choice")
else:
    print("Invalid input! Please enter Fresher or Experienced.")


# ---------------------------------------
# Assignment 2: Certificate Eligibility
# ---------------------------------------

print("\n=== Certificate Eligibility ===")

day_status = input("Did you attend All Day or was there a Day Gap? ").strip().lower()

if day_status == "all day":
    print("Choose your activity: \n1. Assignment \n2. LIVE Class \n3. Camera On")
    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "1":
        print("Eligible for certificate")
    elif choice == "2":
        print("Eligible for certificate")
    elif choice == "3":
        print("Not eligible for certificate")
    else:
        print("Invalid choice")

elif day_status == "day gap":
    print("Not eligible for certificate ")

else:
    print("Invalid input! Please enter 'All Day' or 'Day Gap'.")
