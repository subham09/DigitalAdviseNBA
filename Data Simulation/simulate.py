import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def simulate_data(num_records):

    np.random.seed(0)

    # Basic demographic data

    start_date = datetime.today().date() - timedelta(days=65*365)
    end_date = datetime.today().date() - timedelta(days=25*365)
    dates_of_birth = pd.Series([pd.to_datetime(np.random.choice(pd.date_range(start_date, end_date))).normalize() for _ in range(num_records)])
    today = pd.to_datetime(datetime.today().date())
    ages = (today - dates_of_birth).dt.days // 365
    genders = np.random.choice(['Male', 'Female'], num_records)
    relationship_status = np.random.choice(['Single', 'Couple'], num_records)
    incomes = np.array([calculate_income(age) for age in ages])
    super_balances = np.array([calculate_super_balance(age, income) for age, income in zip(ages, incomes)])
    postcodes = np.random.randint(1000, 9999, num_records)
    num_dependents = np.random.randint(0, 5, num_records)

    # Partner data
    
    has_partner = np.random.choice([True, False], num_records)
    partner_dobs = pd.Series([dob + pd.DateOffset(years=np.random.randint(-5, 6)) if has_p else None for dob, has_p in zip(dates_of_birth, has_partner)])
    partner_ages = ((today - partner_dobs).dt.days // 365).where(partner_dobs.notna())
    partner_genders = [np.random.choice(['Male', 'Female']) if partner else None for partner in has_partner]
    partner_incomes = np.array([calculate_income(age) if age is not None else None for age in partner_ages])
    partner_super_balances = np.array([calculate_super_balance(age, income) for age, income in zip(partner_ages, incomes)])

    # Financial and insurance data
    
    risk_profiles = np.random.choice(['Defensive', 'Conservative', 'Moderate', 'Balanced', 'Growth', 'High Growth'], num_records)
    current_sg = incomes * 0.12
    current_vol_conccont = np.random.uniform(0, 10000, num_records)
    #current_vol_nconccont = np.random.uniform(0, 10000, num_records)
    current_vol_nconccont = np.random.choice([np.random.uniform(27500, current_sg[i]) if np.random.rand() < 0.25 else 0 for i in range(num_records)], num_records)
    unused_concessional_cap = (25000 - current_sg - current_vol_conccont) * 5
    retirement_ages = np.random.randint(60, 75, num_records)
    target_retirement_incomes = np.where(has_partner, np.random.uniform(70000, 100000, num_records), np.random.uniform(30000, 60000, num_records))

    # More complex insurance data
    
    current_life_insurance_in_fund = np.random.uniform(50000, 1000000, num_records)
    current_income_prot_in_fund = np.random.uniform(0, 20000, num_records)
    current_tpd_in_fund = np.random.uniform(50000, 500000, num_records)
    current_life_insurance_outside_fund = np.random.uniform(50000, 1000000, num_records)
    current_income_prot_outside_fund = np.random.uniform(0, 20000, num_records)
    current_tpd_outside_fund = np.random.uniform(50000, 500000, num_records)
    current_trauma_outside_fund = np.random.uniform(50000, 500000, num_records)

    # Investment data

    current_investment_option = np.random.choice(['Balanced', 'High Growth', 'Growth'], num_records)

    # Digital journey completion flags
    
    completed_flags = np.random.choice([False], size=(num_records, 5))

    # Debt and fees
    
    current_total_debt = np.random.uniform(0, 1000000, num_records)
    current_fee_percent_investments = np.random.uniform(0, 1, num_records)
    current_fee_percent_platform = np.random.uniform(0, 1, num_records)
    current_fee_dollar_platform = np.random.uniform(0, 500, num_records)

    # Combine into a DataFrame
    

    data = pd.DataFrame({
        'Date of Birth': dates_of_birth.dt.date, 'Age': ages,'Gender': genders, 'Relationship Status': relationship_status,
        'Income': incomes, 'Super Balance': super_balances, 'Postcode': postcodes, 'Dependents': num_dependents,
        'Partner': has_partner, 'Partner DoB': partner_dobs.dt.date, 'Partner Age': partner_ages,'Partner Gender': partner_genders,
        'Partner Income': partner_incomes, 'Partner Super Balance': partner_super_balances, 'Risk Profile': risk_profiles,
        'Current SG': current_sg, 'Current Vol ConcCont': current_vol_conccont, 'Current Vol NConcCont': current_vol_nconccont,
        'Unused Concessional Cap': unused_concessional_cap, 'Retirement Age': retirement_ages,
        'Target Retirement Income': target_retirement_incomes, 'Current Life Insurance in Fund': current_life_insurance_in_fund,
        'Current Income Protection in Fund': current_income_prot_in_fund, 'Current TPD in Fund': current_tpd_in_fund,
        'Current Life Insurance outside Fund': current_life_insurance_outside_fund,
        'Current Income Protection outside Fund': current_income_prot_outside_fund, 'Current TPD outside Fund': current_tpd_outside_fund,
        'Current Trauma outside Fund': current_trauma_outside_fund,
        'Current Investment Option': current_investment_option, 'Has completed Retirement': completed_flags[:, 0],
        'Has completed Insurance': completed_flags[:, 1], 'Has completed Investment Choice': completed_flags[:, 2],
        'Has completed TTR': completed_flags[:, 3], 'Has completed Contributions': completed_flags[:, 4],
        'Current Total Debt': current_total_debt, 'Current % Fee of Investments': current_fee_percent_investments,
        'Current % Fee of Platform': current_fee_percent_platform, 'Current $ Fee of Platform': current_fee_dollar_platform
    })
    
    return data

def calculate_income(age):
    if age < 35:
        return np.random.uniform(30000, 120000)
    elif age <= 50:
        return np.random.uniform(80000, 150000)
    else:
        return np.random.uniform(150000, 200000)

def calculate_super_balance(age, income):
    if age is None or np.isnan(age):
        return None
    super_rate = 0.1
    working_age = max(0, age - 18)  # Assume people start working at 18
    total_super_balance = 0
    for i in range(int(working_age)):
        yearly_income = income * ((i / working_age) if working_age > 0 else 1)
        total_super_balance += yearly_income * super_rate
    return total_super_balance

# Generate the data and save it to a files

num_records = 10  # Define how many records you want to generate
simulated_data = simulate_data(num_records)

print(simulated_data)
simulated_data.to_excel('simulated_data.xlsx', index=False)

