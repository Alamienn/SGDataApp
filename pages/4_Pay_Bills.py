import streamlit as st
from footer import show_footer
from header import show_header
show_header()

st.set_page_config(page_title="Pay Bills", page_icon="💡", layout="wide")

st.title("💡 Pay Bills")
st.markdown("Pay electricity, TV, water bills and more")

bill_type = st.selectbox("Select Bill Type", [
    "Electricity Bill", 
    "Cable TV (DSTV/GOTv)", 
    "Water Bill",
    "Internet Bill"
])

if bill_type == "Electricity Bill":
    disco = st.selectbox("Distribution Company", ["IKEDC", "EKEDC", "AEDC", "PHED"])
    meter_number = st.text_input("Meter Number")
    amount = st.number_input("Amount", min_value=100)
    
elif bill_type == "Cable TV (DSTV/GOTv)":
    provider = st.selectbox("Provider", ["DSTV", "GOtv", "Startimes"])
    smartcard_number = st.text_input("Smartcard Number")
    package = st.selectbox("Package", ["Compact", "Compact Plus", "Premium", "Yanga"])
    
else:
    st.info("More bill payment options coming soon!")

if st.button("Pay Bill", type="primary"):
    st.info("🔧 Bill payment integration coming soon. This will connect to VTpass API.")

if st.button("← Back"):
    st.switch_page("app.py")

    show_footer()