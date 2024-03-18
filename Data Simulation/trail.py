import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def calculate_income(age):
    if age < 35:
        return np.random.uniform(30000, 120000)
    elif age <= 50:
        return np.random.uniform(80000, 150000)
    else:
        return np.random.uniform(150000, 200000)

def calculate_super_balance(age, income):
    super_rate = 0.1
    working_age = max(0, age - 18)  # Assume people start working at 18
    return working_age * income * super_rate
start_date = datetime.today().date() - timedelta(days=65*365)
end_date = datetime.today().date() - timedelta(days=25*365)
dates_of_birth = pd.Series([pd.to_datetime(np.random.choice(pd.date_range(start_date, end_date))).normalize() for _ in range(5)])
today = pd.to_datetime(datetime.today().date())
ages = (today - dates_of_birth).dt.days // 365
genders = np.random.choice(['Male', 'Female'], 5)
relationship_status = np.random.choice(['Single', 'Couple'], 5)
#incomes = np.array([np.random.uniform(30000, 200000) * (age / 65) for age in ages])
incomes = np.array([calculate_income(age) for age in ages])
#super_balances = np.array([np.random.uniform(10000, 500000) * (age / 65) for age in ages])
super_balances = np.array([calculate_super_balance(age, income) for age, income in zip(ages, incomes)])
print(incomes)
print(super_balances)
print(ages)

def calculate_income(age):
    if age < 35:
        return np.random.uniform(30000, 120000)
    elif age <= 50:
        return np.random.uniform(80000, 150000)
    else:
        return np.random.uniform(150000, 200000)

def calculate_super_balance(age, income):
    super_rate = 0.1
    working_age = max(0, age - 18)  # Assume people start working at 18
    return working_age * income * super_rate