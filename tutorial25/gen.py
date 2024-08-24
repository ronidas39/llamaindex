import json
import random
from faker import Faker

# Initialize the Faker library
fake = Faker()

# Function to generate a random employee profile
def generate_employee_profile():
    return {
        "employee_id": fake.unique.random_int(min=1000, max=9999),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "date_of_birth": fake.date_of_birth(minimum_age=22, maximum_age=65).isoformat(),
        "gender": random.choice(["male", "female"]),
        "street": fake.street_address(),
        "city": fake.city(),
        "state": fake.state_abbr(),
        "zip_code": fake.zipcode(),
        "country": "USA",
        "job_title": fake.job(),
        "department": random.choice(["Engineering", "Sales", "HR", "Marketing", "Finance", "Customer Support"]),
        "hire_date": fake.date_between(start_date='-10y', end_date='today').isoformat(),
        "salary": round(random.uniform(50000, 150000), 2),
        "manager_id": fake.random_int(min=1000, max=9999),
        "health_insurance": random.choice(["Basic Plan", "Standard Plan", "Premium Plan"]),
        "pension_plan": random.choice(["401K", "Pension", "None"]),
        "vacation_days": random.randint(10, 30)
    }

# Generate profiles for 100 employees
employees = [generate_employee_profile() for _ in range(100)]

# Convert to JSON
employees_json = json.dumps(employees, indent=4)

# Save to a file
with open('employees_simple.json', 'w') as f:
    f.write(employees_json)

print("Generated JSON for 100 employees.")
