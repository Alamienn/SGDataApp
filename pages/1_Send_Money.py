import streamlit as st
from header import show_header  # Add this line
from footer import show_footer

st.set_page_config(
    page_title="Send Money",
    page_icon="📤",
    layout="wide"
)

# ========== SHOW THE HEADER ==========
show_header()

st.title("📤 Send Money")
st.markdown("Transfer to mobile number or bank account")

# Toggle between send types
send_type = st.radio(
    "Send to:",
    ["📱 Mobile Number", "🏦 Bank Account"],
    horizontal=True
)

if send_type == "📱 Mobile Number":
    st.markdown("### Send to Mobile Money")
    
    recipient = st.text_input(
        "Recipient Phone Number",
        placeholder="e.g., 08012345678",
        help="Enter the phone number of the person you're sending to"
    )
    
    amount = st.number_input(
        "Amount (₦)",
        min_value=100,
        step=100,
        placeholder="Enter amount"
    )
    
    narration = st.text_input(
        "Narration (Optional)",
        placeholder="e.g., Birthday gift, Rent payment"
    )
    
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("Send Money", type="primary", use_container_width=True):
            if not recipient:
                st.error("❌ Please enter a recipient phone number")
            elif amount < 100:
                st.error("❌ Minimum amount is ₦100")
            else:
                # Simulate sending (will connect to real API later)
                with st.spinner("Processing transaction..."):
                    import time
                    time.sleep(1.5)
                
                st.success(f"✅ Sent ₦{amount:,.0f} to {recipient}")
                st.info("Reference: TXN" + str(int(time.time())))
                st.balloons()
else:
    st.markdown("### Send to Bank Account")
    
    bank_name = st.selectbox(
        "Select Bank",
        ["Access Bank", "GTBank", "First Bank", "UBA", "Zenith Bank", "Other"]
    )
    
    account_number = st.text_input(
        "Account Number",
        placeholder="e.g., 0123456789"
    )
    
    account_name = st.text_input(
        "Account Name",
        placeholder="Enter account holder's name",
        disabled=True
    )
    
    amount = st.number_input(
        "Amount (₦)",
        min_value=100,
        step=100
    )
    
    if st.button("Send to Bank", type="primary", use_container_width=True):
        st.info("🔧 Bank transfer integration coming soon!")

st.markdown("---")
if st.button("← Back to Dashboard"):
    st.switch_page("app.py")

    show_footer()