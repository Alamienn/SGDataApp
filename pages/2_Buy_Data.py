import streamlit as st
from footer import show_footer
from header import show_header
show_header()

st.set_page_config(
    page_title="Buy Data",
    page_icon="📶",
    layout="wide"
)

st.title("📶 Buy Data Bundle")
st.markdown("Purchase data for yourself or send to a loved one")

# Network selection with logos (using emojis)
network = st.selectbox(
    "Select Network Provider",
    ["📶 MTN Nigeria", "💚 Glo", "🔴 Airtel Nigeria", "💙 9mobile"]
)

# Phone number input
col1, col2 = st.columns([3, 1])
with col1:
    phone_number = st.text_input(
        "Phone Number",
        placeholder="e.g., 08012345678",
        help="Enter the phone number to receive data"
    )

with col2:
    st.write("")
    st.write("")
    send_to_self = st.checkbox("Send to myself")

if send_to_self:
    phone_number = "08012345678"  # Would pull from user profile

# Data plans based on network
st.markdown("### 📦 Select Data Plan")

if "MTN" in network:
    data_plan = st.selectbox(
        "Data Plan",
        [
            "100MB - ₦50 (Daily)",
            "500MB - ₦100 (Weekly)",
            "1GB - ₦300 (30 Days)",
            "2GB - ₦500 (30 Days)",
            "5GB - ₦1000 (30 Days)",
            "10GB - ₦2000 (30 Days)"
        ]
    )
elif "Glo" in network:
    data_plan = st.selectbox(
        "Data Plan",
        [
            "500MB - ₦120 (Weekly)",
            "1GB - ₦350 (30 Days)",
            "2GB - ₦550 (30 Days)",
            "3GB - ₦750 (30 Days)",
            "5GB - ₦1200 (30 Days)"
        ]
    )
elif "Airtel" in network:
    data_plan = st.selectbox(
        "Data Plan",
        [
            "500MB - ₦110 (Weekly)",
            "1GB - ₦320 (30 Days)",
            "2GB - ₦520 (30 Days)",
            "5GB - ₦1100 (30 Days)",
            "10GB - ₦2100 (30 Days)"
        ]
    )
else:  # 9mobile
    data_plan = st.selectbox(
        "Data Plan",
        [
            "500MB - ₦130 (Weekly)",
            "1GB - ₦380 (30 Days)",
            "2GB - ₦600 (30 Days)",
            "5GB - ₦1300 (30 Days)"
        ]
    )

# Extract amount from selected plan
import re
amount_match = re.search(r'₦([\d,]+)', data_plan)
amount = int(amount_match.group(1).replace(',', '')) if amount_match else 0

# Save as favourite option
save_fav = st.checkbox("⭐ Save this as favourite for quick purchase")

# Order summary
st.markdown("---")
st.subheader("📝 Order Summary")

col1, col2 = st.columns(2)
with col1:
    st.write(f"**Network:** {network}")
    st.write(f"**Phone:** {phone_number if phone_number else 'Not entered'}")
with col2:
    st.write(f"**Plan:** {data_plan}")
    st.write(f"**Amount:** ₦{amount:,}")

# Buy button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    purchase_button = st.button("💳 Purchase Now", type="primary", use_container_width=True)

if purchase_button:
    if not phone_number:
        st.error("❌ Please enter a phone number")
    elif len(phone_number) < 10:
        st.error("❌ Please enter a valid phone number")
    else:
        # Check if user has enough balance (using session state)
        if 'user_balance' in st.session_state and st.session_state.user_balance >= amount:
            with st.spinner("Processing purchase..."):
                import time
                time.sleep(2)  # Simulate API call
            
            # Deduct from balance (temporary)
            st.session_state.user_balance -= amount
            
            # Add to transaction history
            if 'transactions' in st.session_state:
                from datetime import datetime
                st.session_state.transactions.insert(0, {
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "description": f"Bought {data_plan} for {phone_number}",
                    "amount": f"-₦{amount:,}",
                    "status": "Success"
                })
            
            st.success(f"✅ Success! {data_plan} purchased for {phone_number}")
            st.balloons()
            
            if save_fav:
                st.info("⭐ Added to your favourites!")
        else:
            st.error("❌ Insufficient balance! Please fund your wallet.")

st.markdown("---")
if st.button("← Back to Dashboard"):
    st.switch_page("app.py")

    show_footer()