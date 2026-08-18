import streamlit as st
from header import show_header
from footer import show_footer

st.set_page_config(
    page_title="SG WALLET - Premium Financial Services",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== HYBRID MODERN LUXURY CSS - BRIGHT & READABLE ==========
st.markdown("""
<style>
    /* Hide default Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .main {
        background: linear-gradient(180deg, #f8f9fc 0%, #f0f2f8 100%);
    }
    
    /* ===== ALL TEXT COLORS - BRIGHTENED FOR READABILITY ===== */
    
    /* Headers - Dark but clear */
    .premium-title {
        font-family: 'Playfair Display', serif;
        font-size: 28px;
        color: #1A2A4A;
        margin-bottom: 8px;
        font-weight: 700;
    }
    
    .premium-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        color: #5A6A8A;
        font-weight: 400;
        letter-spacing: 1px;
    }
    
    .section-header {
        font-family: 'Playfair Display', serif;
        font-size: 22px;
        color: #1A2A4A;
        margin-bottom: 16px;
        font-weight: 700;
    }
    
    .section-subheader {
        font-family: 'Inter', sans-serif;
        font-size: 13px;
        color: #6A7A9A;
        font-weight: 400;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    
    /* Balance Card */
    .balance-card-premium {
        background: linear-gradient(145deg, #1E2A4F 0%, #2A3A6A 50%, #1E2A4F 100%);
        border-radius: 28px;
        padding: 36px 40px;
        margin-bottom: 32px;
        box-shadow: 0 20px 60px rgba(30, 42, 79, 0.25);
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(201, 168, 76, 0.2);
    }
    
    .balance-card-premium::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -20%;
        width: 60%;
        height: 200%;
        background: radial-gradient(circle, rgba(201, 168, 76, 0.08) 0%, transparent 70%);
        pointer-events: none;
    }
    
    .balance-card-premium::after {
        content: '✦ ✦ ✦';
        position: absolute;
        bottom: 16px;
        right: 24px;
        color: rgba(201, 168, 76, 0.15);
        font-size: 12px;
        letter-spacing: 8px;
    }
    
    .balance-label {
        font-family: 'Inter', sans-serif;
        font-size: 13px;
        color: #A8B8D8;
        letter-spacing: 3px;
        text-transform: uppercase;
        font-weight: 400;
        position: relative;
        z-index: 1;
    }
    
    .balance-amount {
        font-family: 'Playfair Display', serif;
        font-size: 52px;
        font-weight: 700;
        color: #D4B85C;
        margin: 12px 0 16px 0;
        position: relative;
        z-index: 1;
        text-shadow: 0 2px 20px rgba(201, 168, 76, 0.15);
    }
    
    .balance-amount small {
        font-size: 20px;
        color: #E8D5A8;
        font-weight: 300;
    }
    
    .balance-stat-label {
        font-family: 'Inter', sans-serif;
        font-size: 11px;
        color: #A8B8D8;
        letter-spacing: 2px;
        text-transform: uppercase;
    }
    
    .balance-stat-value {
        font-family: 'Inter', sans-serif;
        font-size: 16px;
        color: #E8F0F8;
        font-weight: 600;
        margin-top: 4px;
    }
    
    /* Cards - White background with clear text */
    .premium-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 20px;
        border: 1px solid rgba(201, 168, 76, 0.15);
        box-shadow: 0 4px 20px rgba(0,0,0,0.04);
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
    
    .premium-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 40px rgba(201, 168, 76, 0.15);
        border-color: rgba(201, 168, 76, 0.3);
    }
    
    /* Buttons - Gold */
    .stButton > button {
        background: linear-gradient(135deg, #C9A84C, #B8963E) !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        border-radius: 14px !important;
        padding: 12px 24px !important;
        border: none !important;
        width: 100% !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 15px !important;
        letter-spacing: 0.3px !important;
        box-shadow: 0 4px 16px rgba(201, 168, 76, 0.25) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 28px rgba(201, 168, 76, 0.35) !important;
        background: linear-gradient(135deg, #D4B85C, #C9A84C) !important;
        color: #FFFFFF !important;
    }
    
    .stButton > button:active {
        transform: scale(0.96) !important;
    }
    
    /* Quick Action Buttons - CLEAR TEXT */
    .quick-action-btn .stButton > button {
        background: rgba(255, 255, 255, 0.95) !important;
        color: #1A2A4A !important;
        backdrop-filter: blur(20px);
        border: 1px solid rgba(30, 42, 79, 0.12) !important;
        box-shadow: 0 2px 12px rgba(0,0,0,0.04) !important;
        padding: 16px 12px !important;
        font-size: 14px !important;
        font-weight: 600 !important;
        text-align: center !important;
        height: 80px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        transition: all 0.4s ease !important;
        color: #1A2A4A !important;
    }
    
    .quick-action-btn .stButton > button:hover {
        background: linear-gradient(135deg, #1E2A4F, #2A3A6A) !important;
        color: #FFFFFF !important;
        border-color: #C9A84C !important;
        transform: translateY(-4px) !important;
        box-shadow: 0 8px 28px rgba(30, 42, 79, 0.2) !important;
    }
    
    /* Favourites Cards - CLEAR TEXT */
    .favourite-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 16px;
        padding: 20px;
        border: 1px solid rgba(30, 42, 79, 0.08);
        box-shadow: 0 2px 12px rgba(0,0,0,0.04);
        transition: all 0.3s ease;
        text-align: center;
    }
    
    .favourite-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 28px rgba(201, 168, 76, 0.12);
        border-color: #C9A84C;
    }
    
    .favourite-card .fav-name {
        font-weight: 600;
        color: #1A2A4A;
        font-size: 15px;
    }
    
    .favourite-card .fav-amount {
        color: #C9A84C;
        font-weight: 700;
        font-size: 18px;
        margin: 4px 0;
    }
    
    .favourite-card .fav-sub {
        font-size: 12px;
        color: #6A7A9A;
    }
    
    .favourite-icon {
        font-size: 28px;
        margin-bottom: 8px;
    }
    
    /* Transaction Items - CLEAR TEXT */
    .transaction-item-premium {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        padding: 16px 20px;
        border-radius: 14px;
        margin-bottom: 8px;
        border: 1px solid rgba(30, 42, 79, 0.06);
        display: flex;
        justify-content: space-between;
        align-items: center;
        transition: all 0.3s ease;
    }
    
    .transaction-item-premium:hover {
        background: rgba(255, 255, 255, 0.98);
        border-color: rgba(201, 168, 76, 0.2);
        transform: translateX(4px);
        box-shadow: 0 4px 16px rgba(201, 168, 76, 0.08);
    }
    
    .transaction-item-premium .trans-desc {
        font-weight: 600;
        color: #1A2A4A;
        font-size: 15px;
    }
    
    .transaction-item-premium .trans-date {
        font-size: 12px;
        color: #6A7A9A;
    }
    
    .transaction-amount-positive {
        color: #2E7D32 !important;
        font-weight: 700;
        font-size: 17px;
    }
    
    .transaction-amount-negative {
        color: #C62828 !important;
        font-weight: 700;
        font-size: 17px;
    }
    
    .transaction-status {
        background: #E8F5E9;
        color: #2E7D32;
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 600;
    }
    
    /* Metrics - CLEAR */
    [data-testid="stMetricValue"] {
        color: #C9A84C !important;
        font-family: 'Playfair Display', serif !important;
        font-size: 28px !important;
        font-weight: 700 !important;
    }
    
    [data-testid="stMetricLabel"] {
        font-family: 'Inter', sans-serif !important;
        color: #5A6A8A !important;
        font-weight: 500 !important;
        letter-spacing: 0.5px !important;
        font-size: 14px !important;
    }
    
    /* Divider */
    .premium-divider {
        background: linear-gradient(90deg, transparent, rgba(201, 168, 76, 0.2), transparent);
        height: 1px;
        margin: 32px 0;
    }
    
    /* Sidebar - CLEAR TEXT */
    .css-1d391kg {
        background: rgba(248, 249, 252, 0.9) !important;
        backdrop-filter: blur(20px) !important;
    }
    
    .sidebar-name {
        font-family: 'Playfair Display', serif;
        font-size: 20px;
        color: #1A2A4A;
    }
    
    .sidebar-phone {
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        color: #5A6A8A;
    }
    
    .sidebar-label {
        font-family: 'Inter', sans-serif;
        font-size: 12px;
        color: #6A7A9A;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-weight: 500;
    }
    
    .sidebar-contact {
        font-size: 14px;
        color: #1A2A4A;
        font-weight: 500;
    }
    
    .sidebar-contact-small {
        font-size: 12px;
        color: #6A7A9A;
    }
    
    /* Gold Badge */
    .gold-badge {
        background: linear-gradient(135deg, #C9A84C, #B8963E);
        color: white;
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 1px;
    }
    
    /* Promotional Banner */
    .promo-banner {
        background: linear-gradient(135deg, #1E2A4F 0%, #2A3A6A 100%);
        border-radius: 20px;
        padding: 20px 28px;
        border: 1px solid rgba(201, 168, 76, 0.2);
        box-shadow: 0 8px 32px rgba(30, 42, 79, 0.15);
    }
    
    .promo-title {
        color: #C9A84C;
        font-weight: 700;
        font-size: 18px;
    }
    
    .promo-text {
        color: #E8F0F8;
        font-size: 15px;
        font-weight: 400;
    }
    
    .promo-small {
        color: #A8B8D8;
        font-size: 13px;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 6px;
    }
    ::-webkit-scrollbar-track {
        background: #f0f2f8;
    }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #C9A84C, #B8963E);
        border-radius: 10px;
    }
    
    /* Info/Warning/Success messages */
    .stAlert {
        font-size: 15px !important;
        font-weight: 500 !important;
    }
    
    .stAlert p {
        font-size: 15px !important;
    }
</style>
""", unsafe_allow_html=True)

# ========== SESSION STATE ==========
if 'user_balance' not in st.session_state:
    st.session_state.user_balance = 25450
if 'user_name' not in st.session_state:
    st.session_state.user_name = "Muhd Alamin"
if 'user_phone' not in st.session_state:
    st.session_state.user_phone = "08012345678"
if 'transactions' not in st.session_state:
    st.session_state.transactions = [
        {"date": "May 30, 2025", "description": "MTN 1GB Data Bundle", "amount": "-₦300", "status": "Completed"},
        {"date": "May 29, 2025", "description": "Wallet Funding - Paystack", "amount": "+₦5,000", "status": "Completed"},
        {"date": "May 28, 2025", "description": "Send to Mom", "amount": "-₦2,000", "status": "Completed"},
        {"date": "May 27, 2025", "description": "DSTV Premium Subscription", "amount": "-₦2,500", "status": "Completed"},
    ]

# ========== HEADER ==========
show_header()

# ========== SIDEBAR ==========
with st.sidebar:
    st.markdown(f"""
    <div style="text-align: center; padding: 12px 0;">
        <div style="font-size: 48px; margin-bottom: 8px;">👤</div>
        <div class="sidebar-name">{st.session_state.user_name}</div>
        <div class="sidebar-phone">{st.session_state.user_phone}</div>
        <div style="margin-top: 8px;"><span class="gold-badge">✦ Premium Member</span></div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Balance", f"₦{st.session_state.user_balance:,}")
    with col2:
        st.metric("Transactions", len(st.session_state.transactions))
    
    st.markdown("---")
    st.markdown("""
    <div class="sidebar-label">Quick Links</div>
    """, unsafe_allow_html=True)
    
    st.page_link("app.py", label="🏠 Dashboard", icon="🏠")
    st.page_link("pages/8_Wallet.py", label="💰 Wallet", icon="💰")
    st.page_link("pages/9_Profile.py", label="👤 Profile", icon="👤")
    
    st.markdown("---")
    st.markdown("""
    <div class="sidebar-label">📞 Customer Support</div>
    """, unsafe_allow_html=True)
    
    with st.expander("📝 Lodge a Complaint or Suggestion", expanded=False):
        with st.form("complaint_form"):
            subject = st.selectbox("Subject", ["Complaint", "Suggestion", "Bug Report", "Feature Request"])
            message = st.text_area("Your Message", height=100, placeholder="Please describe your issue or suggestion in detail...")
            submitted = st.form_submit_button("Send Message")
            if submitted:
                if message:
                    st.success("✅ Thank you! We'll respond within 24 hours.")
                else:
                    st.error("❌ Please enter a message")
    
    st.markdown("---")
    st.markdown("""
    <div class="sidebar-contact">📧 sgwallet@gmail.com</div>
    <div class="sidebar-contact">📞 +234 903 684 2183</div>
    <div class="sidebar-contact-small">⏰ 24/7 Premium Support</div>
    """, unsafe_allow_html=True)

# ========== MAIN CONTENT ==========

# Premium Balance Card
st.markdown(f"""
<div class="balance-card-premium">
    <div class="balance-label">✦ Available Balance</div>
    <div class="balance-amount">₦{st.session_state.user_balance:,}</div>
    <div style="display: flex; gap: 40px; margin-top: 8px;">
        <div>
            <div class="balance-stat-label">Virtual Card</div>
            <div class="balance-stat-value">💳 Active</div>
        </div>
        <div>
            <div class="balance-stat-label">Account Tier</div>
            <div class="balance-stat-value"><span style="color: #C9A84C;">✦</span> Premium</div>
        </div>
        <div>
            <div class="balance-stat-label">Status</div>
            <div class="balance-stat-value" style="color: #66BB6A;">● Active</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Quick Actions - CLEAR HEADERS
st.markdown("""
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
    <span class="section-header">⚡ Quick Actions</span>
    <span class="section-subheader">Frequently Used</span>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="quick-action-btn">', unsafe_allow_html=True)
    if st.button("📤 Send Money", key="send_btn", use_container_width=True):
        st.switch_page("pages/1_Send_Money.py")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="quick-action-btn">', unsafe_allow_html=True)
    if st.button("📶 Buy Data", key="data_btn", use_container_width=True):
        st.switch_page("pages/2_Buy_Data.py")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="quick-action-btn">', unsafe_allow_html=True)
    if st.button("📞 Buy Airtime", key="airtime_btn", use_container_width=True):
        st.switch_page("pages/3_Buy_Airtime.py")
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="quick-action-btn">', unsafe_allow_html=True)
    if st.button("💡 Pay Bills", key="bills_btn", use_container_width=True):
        st.switch_page("pages/4_Pay_Bills.py")
    st.markdown('</div>', unsafe_allow_html=True)

col5, col6, col7, col8 = st.columns(4)

with col5:
    st.markdown('<div class="quick-action-btn">', unsafe_allow_html=True)
    if st.button("⭐ Favourites", key="fav_btn", use_container_width=True):
        try:
            st.switch_page("pages/5_Favourites.py")
        except:
            st.info("⭐ Favourites coming soon!")
    st.markdown('</div>', unsafe_allow_html=True)

with col6:
    st.markdown('<div class="quick-action-btn">', unsafe_allow_html=True)
    if st.button("📸 Scan & Pay", key="scan_btn", use_container_width=True):
        st.switch_page("pages/6_Scan_Pay.py")
    st.markdown('</div>', unsafe_allow_html=True)

with col7:
    st.markdown('<div class="quick-action-btn">', unsafe_allow_html=True)
    if st.button("💳 Virtual Card", key="card_btn", use_container_width=True):
        st.switch_page("pages/7_Virtual_Card.py")
    st.markdown('</div>', unsafe_allow_html=True)

with col8:
    st.markdown('<div class="quick-action-btn">', unsafe_allow_html=True)
    if st.button("💰 Wallet", key="wallet_btn", use_container_width=True):
        st.switch_page("pages/8_Wallet.py")
    st.markdown('</div>', unsafe_allow_html=True)

# Divider
st.markdown('<div class="premium-divider"></div>', unsafe_allow_html=True)

# Favourites Section - CLEAR TEXT
st.markdown("""
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
    <span class="section-header">⭐ Your Favourites</span>
    <span class="section-subheader">Quick Access</span>
</div>
""", unsafe_allow_html=True)

fav_col1, fav_col2, fav_col3 = st.columns(3)

with fav_col1:
    st.markdown("""
    <div class="favourite-card">
        <div class="favourite-icon">👩</div>
        <div class="fav-name">Send to Mom</div>
        <div class="fav-amount">₦5,000</div>
        <div class="fav-sub">Instant Transfer</div>
    </div>
    """, unsafe_allow_html=True)

with fav_col2:
    st.markdown("""
    <div class="favourite-card">
        <div class="favourite-icon">📶</div>
        <div class="fav-name">MTN 1GB Data</div>
        <div class="fav-amount">₦300</div>
        <div class="fav-sub">Valid 30 Days</div>
    </div>
    """, unsafe_allow_html=True)

with fav_col3:
    st.markdown("""
    <div class="favourite-card">
        <div class="favourite-icon">📞</div>
        <div class="fav-name">Airtime - Self</div>
        <div class="fav-amount">₦500</div>
        <div class="fav-sub">Instant Recharge</div>
    </div>
    """, unsafe_allow_html=True)

# Divider
st.markdown('<div class="premium-divider"></div>', unsafe_allow_html=True)

# Recent Transactions - CLEAR TEXT
st.markdown("""
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
    <span class="section-header">📋 Recent Transactions</span>
    <span class="section-subheader">Last 5 Activities</span>
</div>
""", unsafe_allow_html=True)

for trans in st.session_state.transactions[:5]:
    color_class = "transaction-amount-positive" if trans['amount'].startswith('+') else "transaction-amount-negative"
    icon = "📈" if trans['amount'].startswith('+') else "📉"
    st.markdown(f"""
    <div class="transaction-item-premium">
        <div>
            <div class="trans-desc">{icon} {trans['description']}</div>
            <div class="trans-date">{trans['date']}</div>
        </div>
        <div style="display: flex; align-items: center; gap: 16px;">
            <div class="{color_class}">{trans['amount']}</div>
            <div class="transaction-status">✓ {trans['status']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Divider
st.markdown('<div class="premium-divider"></div>', unsafe_allow_html=True)

# Promotional Banner
col1, col2 = st.columns([4, 1])
with col1:
    st.markdown("""
    <div class="promo-banner">
        <div style="display: flex; align-items: center; gap: 16px;">
            <div style="font-size: 32px;">🎉</div>
            <div>
                <div class="promo-title">✦ Special Gold Offer ✦</div>
                <div class="promo-text">Buy 2GB data and get 500MB FREE!</div>
                <div class="promo-small">Valid for MTN customers • Limited time offer</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    if st.button("Claim Offer →", key="offer_btn"):
        st.balloons()
        st.success("🎉 Offer claimed! Check your data balance.")

# ========== FOOTER ==========
show_footer()