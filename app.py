import streamlit as st

st.title('Building Energy Survey')

# General Information
st.header('General Information')
org_name = st.text_input("Organization's Name")
address = st.text_input("Address")
state = st.selectbox("State", ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'])
building_size = st.number_input("Building Size (in sq. ft)", min_value=1)
building_type = st.selectbox("Building Type", ['Residential', 'Commercial', 'Industrial'])
year_built = st.number_input("Year Built", min_value=1800, max_value=2100)

# Building Occupancy Information
st.header('Building Occupancy Information')
number_of_occupants = st.number_input("Number of Occupants", min_value=1)
occupancy_hours = st.number_input("Average Daily Occupancy Hours", min_value=1, max_value=24)

# Energy Consumption Information
st.header('Energy Consumption Information')
electricity_use = st.number_input("Annual Electricity Consumption (in kWh)", min_value=1)
natural_gas_use = st.number_input("Annual Natural Gas Consumption (in cubic feet)", min_value=1)
water_use = st.number_input("Annual Water Consumption (in gallons)", min_value=1)

# Heating, Ventilation, and Air Conditioning (HVAC) Information
st.header('HVAC Information')
hvac_system_type = st.selectbox("HVAC System Type", ['Forced Air', 'Radiant', 'Heat Pump', 'Other'])
hvac_age = st.number_input("Age of HVAC System (in years)", min_value=0)

# Lighting Information
st.header('Lighting Information')
lighting_type = st.selectbox("Predominant Lighting Type", ['LED', 'CFL', 'Fluorescent', 'Incandescent', 'Other'])
percentage_lighting_led = st.slider("Percentage of Lighting that is LED", min_value=0, max_value=100)

# Submission Button
if st.button('Submit'):
    # Here you could add some functionality to store the inputs in a database or conduct some initial analysis.
    st.success('The energy survey has been submitted successfully.')
