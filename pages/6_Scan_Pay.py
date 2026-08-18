import streamlit as st
from footer import show_footer
from header import show_header
show_header()

st.set_page_config(page_title="Scan & Pay", page_icon="📸", layout="wide")

st.title("📸 Scan & Pay")
st.markdown("Pay at merchants by scanning QR code or entering code")

# Two options for payment
payment_method = st.radio(
    "Select payment method:",
    ["📷 Scan QR Code", "📝 Enter Merchant Code"],
    horizontal=True
)

if payment_method == "📷 Scan QR Code":
    st.info("📷 Camera access will be available in the next update")
    st.caption("For now, you can use merchant code instead")
    
    # Simulated QR scanner
    st.markdown("### Demo QR Scanner")
    st.code("""
    ┌─────────────────────────┐
    │                         │
    │      ███████████        │
    │      █  SCAN  █         │
    │      █   QR   █         │
    │      ███████████        │
    │                         │
    │   Position QR code      │
    │   within the frame      │
    └─────────────────────────┘
    """)
    
else:
    st.markdown("### Enter Merchant Details")
    
    merchant_code = st.text_input(
        "Merchant Code",
        placeholder="e.g., MCH123456",
        help="Enter the code displayed at the merchant"
    )
    
    amount = st.number_input("Amount (₦)", min_value=100, step=100)
    
    narration = st.text_input("Description (Optional)", placeholder="e.g., Purchase at Shoprite")
    
    if st.button("Pay Now", type="primary"):
        if not merchant_code:
            st.error("❌ Please enter merchant code")
        elif amount < 100:
            st.error("❌ Minimum amount is ₦100")
        else:
            with st.spinner("Processing payment..."):
                import time
                time.sleep(1.5)
            st.success(f"✅ Payment of ₦{amount:,.0f} sent to {merchant_code}")
            st.balloons()

st.markdown("---")
if st.button("← Back to Dashboard"):
    st.switch_page("app.py")

    show_footer()