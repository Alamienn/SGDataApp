import streamlit as st
from footer import show_footer
from header import show_header
show_header()

st.set_page_config(page_title="Virtual Card", page_icon="💳", layout="wide")

st.title("💳 Virtual Card")
st.markdown("Your digital Mastercard for online payments")

# Check if user has a card
if 'has_card' not in st.session_state:
    st.session_state.has_card = True  # Simulate having a card

if st.session_state.has_card:
    # Display existing card
    st.markdown("### Your Active Card")
    
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
        border-radius: 20px;
        padding: 24px;
        color: white;
        margin: 20px 0;
        font-family: monospace;
    ">
        <div style="font-size: 12px; opacity: 0.7;">BALANCE</div>
        <div style="font-size: 28px; font-weight: bold; margin: 5px 0;">₦12,500</div>
        <div style="margin: 20px 0;">
            <span style="font-size: 18px; letter-spacing: 2px;">****</span>
            <span style="font-size: 18px; letter-spacing: 2px;">****</span>
            <span style="font-size: 18px; letter-spacing: 2px;">****</span>
            <span style="font-size: 18px; letter-spacing: 2px;">1234</span>
        </div>
        <div style="display: flex; justify-content: space-between;">
            <div>
                <div style="font-size: 10px; opacity: 0.7;">CARD HOLDER</div>
                <div>JOHN DOE</div>
            </div>
            <div>
                <div style="font-size: 10px; opacity: 0.7;">EXPIRY</div>
                <div>12/28</div>
            </div>
        </div>
        <div style="margin-top: 15px;">
            <span style="font-size: 24px;">💳</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔒 Freeze Card", use_container_width=True):
            st.warning("Card frozen temporarily")
    with col2:
        if st.button("💰 Fund Card", use_container_width=True):
            st.info("Coming soon: Fund from wallet")
    
else:
    # No card - offer to create one
    st.info("You don't have a virtual card yet")
    if st.button("Create Virtual Card", type="primary"):
        with st.spinner("Creating your virtual card..."):
            import time
            time.sleep(1)
        st.session_state.has_card = True
        st.success("✅ Virtual card created successfully!")
        st.rerun()

st.markdown("---")
st.caption("💡 Use your virtual card for online shopping, subscriptions, and more")

if st.button("← Back to Dashboard"):
    st.switch_page("app.py")

    show_footer()