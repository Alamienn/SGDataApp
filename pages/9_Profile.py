import streamlit as st
from footer import show_footer
from header import show_header
show_header()

st.set_page_config(page_title="Profile", page_icon="👤", layout="wide")

st.title("👤 Profile & Settings")

# User info
st.subheader("Personal Information")
col1, col2 = st.columns(2)
with col1:
    st.text_input("Full Name", value=st.session_state.get('user_name', 'John Doe'))
    st.text_input("Phone Number", value=st.session_state.get('user_phone', '08012345678'))
with col2:
    st.text_input("Email", value="john.doe@example.com")
    st.selectbox("Preferred Language", ["English", "Hausa", "Igbo", "Yoruba"])

st.markdown("---")
st.subheader("Security")
col1, col2 = st.columns(2)
with col1:
    if st.button("Change PIN", use_container_width=True):
        st.info("PIN change coming soon")
with col2:
    if st.button("Enable Biometric", use_container_width=True):
        st.info("Biometric login coming soon")

st.markdown("---")
st.subheader("App Settings")
st.checkbox("Dark Mode", value=True)
st.checkbox("Transaction Notifications", value=True)
st.checkbox("Weekly Statements", value=False)

if st.button("← Back to Dashboard"):
    st.switch_page("app.py")

    show_footer()