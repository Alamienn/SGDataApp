import streamlit as st
from footer import show_footer
from header import show_header
show_header()

st.set_page_config(page_title="Favourites", page_icon="⭐", layout="wide")

st.title("⭐ Your Favourites")
st.markdown("Save frequent transactions here for one-click access")

# Sample favourites
st.subheader("Saved Transactions")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📤 Send Money")
    st.write("**Send to Mom** - ₦5,000")
    if st.button("Send Now", key="send_mom"):
        st.info("🔧 Transaction processing coming soon!")

with col2:
    st.markdown("### 📶 Buy Data")
    st.write("**MTN 1GB** - ₦300")
    if st.button("Buy Now", key="buy_mtn"):
        st.info("🔧 Data purchase coming soon!")

st.markdown("---")
st.subheader("Add New Favourite")

col1, col2, col3 = st.columns(3)
with col1:
    st.selectbox("Service Type", ["Send Money", "Buy Data", "Buy Airtime", "Pay Bills"])
with col2:
    st.text_input("Name/Label", placeholder="e.g., Send to John")
with col3:
    st.number_input("Amount (₦)", min_value=100)

if st.button("Save as Favourite"):
    st.success("⭐ Saved to favourites!")

st.markdown("---")
if st.button("← Back to Dashboard"):
    st.switch_page("app.py")

    show_footer()