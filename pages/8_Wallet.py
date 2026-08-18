import streamlit as st
from footer import show_footer
from header import show_header
show_header()

st.set_page_config(page_title="My Wallet", page_icon="💰", layout="wide")

st.title("💰 My Wallet")

# Get balance from session state
balance = st.session_state.get('user_balance', 25450)

# Display balance prominently
st.markdown(f"""
<div style="
    background: linear-gradient(135deg, #FFB200 0%, #FF8C00 100%);
    border-radius: 24px;
    padding: 32px;
    text-align: center;
    margin: 20px 0;
">
    <div style="font-size: 14px; opacity: 0.8;">TOTAL BALANCE</div>
    <div style="font-size: 48px; font-weight: bold; margin: 10px 0;">₦{balance:,}</div>
    <div style="font-size: 12px;">Available for transactions</div>
</div>
""", unsafe_allow_html=True)

# Quick actions
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("➕ Add Money", use_container_width=True):
        st.info("🔧 Paystack integration coming soon!")
with col2:
    if st.button("📤 Withdraw", use_container_width=True):
        st.info("🔧 Withdrawal coming soon!")
with col3:
    if st.button("📊 Statement", use_container_width=True):
        st.info("Download statement coming soon!")

st.markdown("---")
st.subheader("📜 Transaction History")

transactions = st.session_state.get('transactions', [
    {"date": "2025-05-30", "description": "MTN 1GB Data", "amount": "-₦300", "status": "Success"},
    {"date": "2025-05-29", "description": "Wallet Funding", "amount": "+₦5,000", "status": "Success"},
    {"date": "2025-05-28", "description": "Sent to Mom", "amount": "-₦2,000", "status": "Success"},
])

for t in transactions:
    color = "green" if t['amount'].startswith('+') else "red"
    st.markdown(f"""
    <div style="padding: 12px; border-bottom: 1px solid #eee; display: flex; justify-content: space-between;">
        <div>
            <strong>{t['description']}</strong><br>
            <small>{t['date']}</small>
        </div>
        <div style="color: {color}; font-weight: bold;">{t['amount']}</div>
    </div>
    """, unsafe_allow_html=True)

if st.button("← Back to Dashboard"):
    st.switch_page("app.py")

    show_footer()