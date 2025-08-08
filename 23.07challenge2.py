late_returns = {
  "Anu": 3,
  "Raj": 0,
  "Kavya": 5
}

fine_per_day = 2

for name,days_late in late_returns.items():
    fine = fine_per_day * days_late
    print(f"{name} has to pay ₹{fine}")

