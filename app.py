import streamlit as st
from header import show_header
from footer import show_footer
from login_register import show_login, show_register, show_forgot_password

# Page config
st.set_page_config(
    page_title="SG WALLET - Send Money, Buy Data & Pay Bills",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===== CUSTOM CSS =====
st.markdown("""
<style>
    /* ===== GLOBAL TEXT FIXES ===== */
    .stApp {
        background: linear-gradient(180deg, #f8f9fc 0%, #f0f2f8 100%);
    }
    
    .stMarkdown, .stText, .stTitle, .stSubheader, .stHeader, p, li, label, div {
        color: #1A2A4A !important;
        font-weight: 500 !important;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #1A2A4A !important;
        font-weight: 700 !important;
    }
    
    @media (prefers-color-scheme: dark) {
        .stApp {
            background: linear-gradient(180deg, #0f0f1a 0%, #1a1a2e 50%, #0f1a2e 100%);
        }
        .stMarkdown, .stText, .stTitle, .stSubheader, .stHeader, p, li, label, div {
            color: #e8e8f8 !important;
            font-weight: 500 !important;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #f0f2f8 !important;
            font-weight: 700 !important;
        }
        .stTextInput label, .stSelectbox label, .stTextArea label {
            color: #d0d8e8 !important;
            font-weight: 600 !important;
        }
        .stButton button {
            color: white !important;
            font-weight: 700 !important;
        }
        .stAlert {
            background: rgba(255,255,255,0.08) !important;
            color: #e8e8f8 !important;
        }
        .stMetric label {
            color: #d0d8e8 !important;
        }
        div[data-testid="stMetricValue"] {
            color: #C9A84C !important;
        }
        .css-1d391kg {
            background: rgba(15, 15, 30, 0.95) !important;
        }
        .stTabs [data-baseweb="tab"] {
            color: #c8d0e0 !important;
            font-weight: 600 !important;
        }
        .stTabs [aria-selected="true"] {
            color: #C9A84C !important;
        }
    }
    
    .hero {
        text-align: center;
        padding: 60px 20px 40px 20px;
        background: linear-gradient(135deg, #1E2A4F 0%, #2A3A6A 50%, #1E2A4F 100%);
        border-radius: 30px;
        color: white !important;
        margin-bottom: 40px;
        box-shadow: 0 20px 60px rgba(30, 42, 79, 0.3);
        position: relative;
        overflow: hidden;
    }
    .hero h1 {
        font-size: 52px;
        font-weight: 700;
        margin-bottom: 12px;
        color: white !important;
    }
    .hero h1 span {
        color: #C9A84C;
    }
    .hero p {
        font-size: 20px;
        opacity: 0.95;
        max-width: 650px;
        margin: 0 auto 28px auto;
        line-height: 1.6;
        color: #e8e8f8 !important;
        font-weight: 400 !important;
    }
    .hero-badge {
        display: inline-block;
        background: rgba(201, 168, 76, 0.2);
        border: 1px solid rgba(201, 168, 76, 0.3);
        padding: 4px 16px;
        border-radius: 20px;
        font-size: 12px;
        color: #C9A84C !important;
        letter-spacing: 2px;
        margin-bottom: 16px;
        font-weight: 600 !important;
    }
    
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 20px;
        margin: 40px 0;
    }
    .feature-card {
        background: rgba(255, 255, 255, 0.92);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 28px 20px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        border: 1px solid rgba(201, 168, 76, 0.1);
        transition: all 0.4s ease;
    }
    .feature-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 16px 40px rgba(201, 168, 76, 0.15);
        border-color: #C9A84C;
    }
    .feature-card .icon {
        font-size: 48px;
        margin-bottom: 12px;
    }
    .feature-card h3 {
        color: #1A2A4A !important;
        font-size: 18px;
        margin-bottom: 6px;
        font-weight: 700 !important;
    }
    .feature-card p {
        color: #4A5A7A !important;
        font-size: 14px;
        line-height: 1.5;
        font-weight: 400 !important;
    }
    .feature-card .learn-more {
        display: inline-block;
        margin-top: 12px;
        color: #C9A84C !important;
        font-weight: 700 !important;
        font-size: 13px;
    }
    
    .fun-stats {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 16px;
        margin: 30px 0;
    }
    .fun-stat {
        text-align: center;
        padding: 20px;
        background: rgba(255,255,255,0.85);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        border: 1px solid rgba(201, 168, 76, 0.1);
    }
    .fun-stat .number {
        font-size: 32px;
        font-weight: 700;
        color: #C9A84C !important;
    }
    .fun-stat .label {
        font-size: 14px;
        color: #4A5A7A !important;
        margin-top: 4px;
        font-weight: 600 !important;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #C9A84C, #B8963E) !important;
        color: white !important;
        font-weight: 700 !important;
        border-radius: 14px !important;
        padding: 12px 28px !important;
        border: none !important;
        font-size: 16px !important;
        box-shadow: 0 4px 16px rgba(201, 168, 76, 0.25) !important;
        transition: all 0.3s ease !important;
    }
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 28px rgba(201, 168, 76, 0.35) !important;
        background: linear-gradient(135deg, #D4B85C, #C9A84C) !important;
        color: white !important;
    }
    
    .section-title {
        font-size: 32px;
        color: #1A2A4A !important;
        font-weight: 700 !important;
        text-align: center;
    }
    .section-title span {
        color: #C9A84C;
    }
    .section-subtitle {
        color: #4A5A7A !important;
        font-size: 16px;
        text-align: center;
        max-width: 600px;
        margin: 0 auto 30px auto;
        font-weight: 400 !important;
    }
    
    .why-card {
        text-align: center;
        padding: 20px;
    }
    .why-card .icon {
        font-size: 40px;
    }
    .why-card h4 {
        color: #1A2A4A !important;
        font-weight: 700 !important;
        font-size: 18px;
        margin-top: 8px;
    }
    .why-card p {
        color: #4A5A7A !important;
        font-size: 14px;
        font-weight: 400 !important;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    .float-icon {
        animation: float 3s ease-in-out infinite;
        display: inline-block;
    }
    
    @media (max-width: 768px) {
        .feature-grid, .fun-stats {
            grid-template-columns: 1fr 1fr;
        }
        .hero h1 {
            font-size: 32px;
        }
        .hero p {
            font-size: 16px;
        }
    }
</style>
""", unsafe_allow_html=True)

# ===== AUTH CHECK =====
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ============================================================
# ===== NOT LOGGED IN - SHOW LANDING PAGE =====
# ============================================================
if not st.session_state.logged_in:
    
    # Hero Section
    st.markdown("""
    <div class="hero">
        <div class="hero-badge">✦ NIGERIA'S TRUSTED PLATFORM ✦</div>
        <h1>💰 SG <span>WALLET</span></h1>
        <p>
            Your all-in-one platform for buying data, paying bills, sending money, and more.<br>
            <strong style="color: #C9A84C; font-weight: 700;">Fast, secure, and built for you.</strong>
        </p>
        <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
            <a href="#" onclick="document.querySelector('[data-testid=\"tab-register\"]').click(); return false;" style="background: linear-gradient(135deg, #C9A84C, #B8963E); color: white; padding: 14px 40px; border-radius: 30px; text-decoration: none; font-weight: 700; font-size: 18px; box-shadow: 0 4px 20px rgba(201, 168, 76, 0.3); display: inline-block;">🚀 Get Started Free</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Fun Stats
    st.markdown("""
    <div class="fun-stats">
        <div class="fun-stat"><div class="number">50K+</div><div class="label">🎉 Happy Users</div></div>
        <div class="fun-stat"><div class="number">2M+</div><div class="label">📱 Transactions</div></div>
        <div class="fun-stat"><div class="number">24/7</div><div class="label">⭐ Premium Support</div></div>
        <div class="fun-stat"><div class="number">100%</div><div class="label">🔒 Secure & Safe</div></div>
    </div>
    """, unsafe_allow_html=True)

    # Features Grid
    st.markdown('<div class="feature-grid">', unsafe_allow_html=True)
    features = [
        ("📶", "Buy Data", "Purchase data bundles for MTN, Glo, Airtel & 9mobile instantly.", "Learn more →"),
        ("📞", "Buy Airtime", "Recharge your phone or send airtime to loved ones.", "Learn more →"),
        ("💡", "Pay Bills", "Settle electricity, cable TV, water & internet bills easily.", "Learn more →"),
        ("📤", "Send Money", "Transfer money to mobile numbers or bank accounts in seconds.", "Learn more →"),
        ("💳", "Virtual Card", "Get a virtual Mastercard for online shopping and subscriptions.", "Learn more →"),
        ("⭐", "Favourites", "Save frequent transactions for one-click access.", "Learn more →"),
        ("📸", "Scan & Pay", "Pay at merchants by scanning QR codes instantly.", "Learn more →"),
        ("🎯", "Rewards", "Earn cashback and bonuses on every transaction.", "Learn more →")
    ]
    for icon, title, desc, link in features:
        st.markdown(f"""
        <div class="feature-card">
            <div class="icon">{icon}</div>
            <h3>{title}</h3>
            <p>{desc}</p>
            <div class="learn-more">{link}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Why Choose Us
    st.markdown("""
    <div style="text-align: center; padding: 40px 0 20px 0;">
        <div class="section-title">Why <span>SG WALLET</span>?</div>
        <div class="section-subtitle">We make managing your finances simple, secure, and rewarding.</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="why-card">
            <div class="icon">⚡</div>
            <h4>Lightning Fast</h4>
            <p>Transactions complete in seconds. No delays.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="why-card">
            <div class="icon">🔒</div>
            <h4>Bank-Grade Security</h4>
            <p>Your money and data are always protected.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="why-card">
            <div class="icon">🎁</div>
            <h4>Rewards & Bonuses</h4>
            <p>Earn cashback on every transaction you make.</p>
        </div>
        """, unsafe_allow_html=True)

    # Fun Interactive Element
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 30px 0;">
        <div class="float-icon" style="font-size: 48px;">🚀</div>
        <h3 style="color: #1A2A4A; margin-top: 8px; font-weight: 700;">Ready to take control of your finances?</h3>
        <p style="color: #4A5A7A; font-weight: 400;">Join thousands of happy users today. It's free!</p>
    </div>
    """, unsafe_allow_html=True)

    # ===== LOGIN/REGISTER TABS =====
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <h2 style="font-size: 28px; color: #1A2A4A; font-weight: 700;">Get Started with <span style="color: #C9A84C;">SG WALLET</span></h2>
        <p style="color: #4A5A7A; font-weight: 400;">Create an account or login to access all services</p>
    </div>
    """, unsafe_allow_html=True)

    if "active_tab" not in st.session_state:
        st.session_state.active_tab = "login"

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔐 Login", key="tab_login", use_container_width=True):
            st.session_state.active_tab = "login"
            st.rerun()
    with col2:
        if st.button("📝 Register", key="tab_register", use_container_width=True):
            st.session_state.active_tab = "register"
            st.rerun()

    if st.session_state.active_tab == "login":
        show_login()
    else:
        show_register()

    st.stop()

# ============================================================
# ===== LOGGED IN - SHOW DASHBOARD WITH SIDEBAR =====
# ============================================================

# Show header
show_header()

# ===== SIDEBAR (ONLY SHOWN WHEN LOGGED IN) =====
with st.sidebar:
    st.markdown(f"### 👤 {st.session_state.user_data.get('name', 'User')}")
    st.markdown(f"📞 {st.session_state.user_data.get('phone', '')}")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Balance", f"₦{st.session_state.user_data.get('balance', 0):,}")
    
    st.markdown("---")
    st.markdown("**🔒 Protected Services**")
    
    # All service links - only shown when logged in
    services = [
        ("📤 Send Money", "pages/1_Send_Money.py"),
        ("📶 Buy Data", "pages/2_Buy_Data.py"),
        ("📞 Buy Airtime", "pages/3_Buy_Airtime.py"),
        ("💡 Pay Bills", "pages/4_Pay_Bills.py"),
        ("⭐ Favourites", "pages/5_Favourites.py"),
        ("📸 Scan & Pay", "pages/6_Scan_Pay.py"),
        ("💳 Virtual Card", "pages/7_Virtual_Card.py"),
        ("💰 Wallet", "pages/8_Wallet.py"),
        ("👤 Profile", "pages/9_Profile.py")
    ]
    
    for label, path in services:
        if st.button(label, key=path, use_container_width=True):
            try:
                st.switch_page(path)
            except:
                st.info("🔧 Coming soon!")
    
    st.markdown("---")
    
    # === LOGOUT BUTTON ===
    if st.button("🚪 Logout", use_container_width=True):
        for key in ["logged_in", "user_email", "user_data", "active_tab"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

# ===== DASHBOARD CONTENT =====
st.markdown(f"""
<div style="display: flex; align-items: center; gap: 12px; margin-bottom: 16px;">
    <span style="font-size: 28px;">👋</span>
    <h1 style="font-size: 28px; color: #1A2A4A; margin: 0; font-weight: 700;">Welcome back, <span style="color: #C9A84C;">{st.session_state.user_data.get('name', 'User')}</span>!</h1>
</div>
""", unsafe_allow_html=True)

# Balance Card
st.markdown(f"""
<div style="background: linear-gradient(145deg, #1E2A4F 0%, #2A3A6A 50%, #1E2A4F 100%);
            border-radius: 28px; padding: 36px 40px; margin-bottom: 32px;
            box-shadow: 0 20px 60px rgba(30, 42, 79, 0.25);
            border: 1px solid rgba(201, 168, 76, 0.2);">
    <div style="font-size: 13px; color: #A8B8D8; letter-spacing: 3px; text-transform: uppercase; font-weight: 400;">✦ Available Balance</div>
    <div style="font-size: 52px; font-weight: 700; color: #D4B85C; margin: 12px 0 16px 0; text-shadow: 0 2px 20px rgba(201, 168, 76, 0.15);">₦{st.session_state.user_data.get('balance', 0):,}</div>
    <div style="display: flex; gap: 40px;">
        <div>
            <div style="font-size: 11px; color: #A8B8D8; letter-spacing: 2px; text-transform: uppercase; font-weight: 400;">Virtual Card</div>
            <div style="font-size: 16px; color: #E8F0F8; font-weight: 600; margin-top: 4px;">💳 Active</div>
        </div>
        <div>
            <div style="font-size: 11px; color: #A8B8D8; letter-spacing: 2px; text-transform: uppercase; font-weight: 400;">Account Tier</div>
            <div style="font-size: 16px; color: #E8F0F8; font-weight: 600; margin-top: 4px;"><span style="color: #C9A84C;">✦</span> Premium</div>
        </div>
        <div>
            <div style="font-size: 11px; color: #A8B8D8; letter-spacing: 2px; text-transform: uppercase; font-weight: 400;">Status</div>
            <div style="font-size: 16px; color: #66BB6A; font-weight: 600; margin-top: 4px;">● Active</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Quick Actions
st.markdown("""
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
    <span style="font-size: 22px; color: #1A2A4A; font-weight: 700;">⚡ Quick Actions</span>
    <span style="font-size: 13px; color: #4A5A7A; font-weight: 400; letter-spacing: 1px; text-transform: uppercase;">Frequently Used</span>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📤 Send Money", key="dash_send", use_container_width=True):
        st.switch_page("pages/1_Send_Money.py")
with col2:
    if st.button("📶 Buy Data", key="dash_data", use_container_width=True):
        st.switch_page("pages/2_Buy_Data.py")
with col3:
    if st.button("📞 Buy Airtime", key="dash_airtime", use_container_width=True):
        st.switch_page("pages/3_Buy_Airtime.py")
with col4:
    if st.button("💡 Pay Bills", key="dash_bills", use_container_width=True):
        st.switch_page("pages/4_Pay_Bills.py")

# Quick stats
st.markdown("---")
st.markdown("### 📊 Your Activity")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("💰 Total Spent", "₦12,450")
with col2:
    st.metric("📱 Transactions", "24")
with col3:
    st.metric("⭐ Rewards", "₦150")

# Fun streak
st.markdown("---")
st.markdown("""
<div style="background: linear-gradient(135deg, #1E2A4F, #2A3A6A); border-radius: 16px; padding: 20px; text-align: center; border: 1px solid rgba(201, 168, 76, 0.2);">
    <div style="font-size: 32px;">🎉</div>
    <div style="color: #C9A84C; font-weight: 700; font-size: 18px;">You're on a 3-day streak!</div>
    <div style="color: #A8B8D8; font-size: 14px; font-weight: 400;">Keep using SG WALLET to unlock exclusive rewards</div>
</div>
""", unsafe_allow_html=True)

# Footer
show_footer()