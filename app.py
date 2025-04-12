import streamlit as st

# Title
st.title("🌐 Unit Converter App")
st.subheader("Convert Length, Weight, and Temperature Units")

# Sidebar for unit type
unit_type = st.sidebar.selectbox("Select Unit Type", ["Length", "Weight", "Temperature"])

# Conversion logic
def convert_length(value, from_unit, to_unit):
    length_units = {
        "meters": 1,
        "kilometers": 1000,
        "miles": 1609.34,
        "feet": 0.3048,
        "inches": 0.0254
    }
    meters = value * length_units[from_unit]
    return meters / length_units[to_unit]

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "grams": 1,
        "kilograms": 1000,
        "pounds": 453.592
    }
    grams = value * weight_units[from_unit]
    return grams / weight_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return ((value - 32) * 5/9) + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return ((value - 273.15) * 9/5) + 32

# Inputs and UI logic
if unit_type == "Length":
    units = ["meters", "kilometers", "miles", "feet", "inches"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter value", value=0.0)
    result = convert_length(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif unit_type == "Weight":
    units = ["grams", "kilograms", "pounds"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter value", value=0.0)
    result = convert_weight(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif unit_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter value", value=0.0)
    result = convert_temperature(value, from_unit, to_unit)
    st.success(f"{value}° {from_unit} = {result:.2f}° {to_unit}")
