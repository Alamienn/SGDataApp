import streamlit as st
from footer import show_footer
from header import show_header
show_header()

st.set_page_config(page_title="Buy Airtime", page_icon="📞", layout="wide")

st.title("📞 Buy Airtime")
st.markdown("Recharge your phone or send to family/friends")

network = st.selectbox("Network", ["MTN", "Glo", "Airtel", "9mobile"])
phone = st.text_input("Phone Number", placeholder="08012345678")

st.markdown("### Select Amount")
amt_col1, amt_col2, amt_col3 = st.columns(3)
with amt_col1:
    if st.button("₦100", use_container_width=True): st.session_state.airtime_amt = 100
    if st.button("₦500", use_container_width=True): st.session_state.airtime_amt = 500
with amt_col2:
    if st.button("₦200", use_container_width=True): st.session_state.airtime_amt = 200
    if st.button("₦1000", use_container_width=True): st.session_state.airtime_amt = 1000
with amt_col3:
    if st.button("₦300", use_container_width=True): st.session_state.airtime_amt = 300
    if st.button("₦2000", use_container_width=True): st.session_state.airtime_amt = 2000

custom_amt = st.number_input("Or enter custom amount", min_value=50, step=50)

amount = custom_amt if custom_amt > 0 else st.session_state.get('airtime_amt', 100)

if st.button("Recharge Now", type="primary"):
    if not phone:
        st.error("Enter phone number")
    else:
        with st.spinner("Processing..."):
            import time
            time.sleep(1)
        st.success(f"✅ ₦{amount} airtime sent to {phone}")

if st.button("← Back"):
    st.switch_page("app.py")

    show_footer()