import streamlit as st

# Define deduction percentages (higher-end estimates)
TAX_RATES = {
    "federal": 11.81,
    "state": 4.79,
    "sdi_pfl": 1.05,
    "social_security": 6.20,  # H1B only
    "medicare": 1.45          # H1B only
}

# ---- Page Config ----
st.set_page_config(
    page_title="Paycheck Estimator",
    page_icon="💵",
    layout="centered"
)

# ---- App Title ----
st.title("Paycheck Estimator")
st.caption("Estimate your gross and net paycheck based on visa status and salary.")

# ---- Inputs ----
salary = st.number_input("Enter your annual salary ($):", min_value=40000, step=1000, value=60000)
status = st.radio("Select your visa status:", options=["F1 (OPT/STEM)", "H1B"])

# ---- Gross Pay Calculation ----
biweekly_gross = salary / 24  # 24 pay periods assumed (twice a month)
monthly_gross = salary / 12
yearly_gross = salary

# ---- Deduction Calculation ----
deductions = TAX_RATES.copy()
if status == "F1 (OPT/STEM)":
    deductions["social_security"] = 0
    deductions["medicare"] = 0

deduction_values = {k: (v / 100) * biweekly_gross for k, v in deductions.items()}
total_deductions = sum(deduction_values.values())
net_biweekly = biweekly_gross - total_deductions
net_monthly = net_biweekly * 2
net_yearly = net_monthly * 12

st.divider()

# ---- Display Results ----
st.subheader("Per Paycheck (Semi-Monthly)")
st.write(f"**:green[Gross]:** ${biweekly_gross:,.2f}")
st.write(f"**:green[Net]:** ${net_biweekly:,.2f}")

st.subheader("Monthly")
st.write(f"**:green[Gross]:** ${monthly_gross:,.2f}")
st.write(f"**:green[Net]:** ${net_monthly:,.2f}")

st.subheader("Annual")
st.write(f"**:green[Gross]:** ${yearly_gross:,.2f}")
st.write(f"**:green[Net]:** ${net_yearly:,.2f}")

st.subheader("Deductions Per Paycheck")
for k, v in deduction_values.items():
    st.write(f"- **{k.replace('_', ' ').title()}**: ${v:.2f} ({TAX_RATES[k]}%)")
