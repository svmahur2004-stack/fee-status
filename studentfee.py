import sys

# Default values (already given input)
default_name = "Soujanya"
default_branch = "CSE"
default_fee = "50000"
default_paid = "30000"
default_balance = "20000"

# If arguments are provided, use them
if len(sys.argv) == 6:
    name = sys.argv[1]
    branch = sys.argv[2]
    fee = sys.argv[3]
    paid = sys.argv[4]
    balance = sys.argv[5]
else:
    # Use already given input values
    name = default_name
    branch = default_branch
    fee = default_fee
    paid = default_paid
    balance = default_balance

print("------ FEE STATUS REPORT ------")
print("Student Name :", name)
print("Branch       :", branch)
print("Total Fee    :", fee)
print("Fee Paid     :", paid)
print("Balance      :", balance)

if balance == "0":
    print("Status       : All fees paid ✔")
else:
    print("Status       : Pending payment ")
