import streamlit as st

# Page config
st.set_page_config(
    page_title="SG WALLET - Send Money, Buy Data & Pay Bills",
    page_icon="💰",
    layout="wide"
)

# Custom CSS for landing
st.markdown("""
<style>
    .hero {
        text-align: center;
        padding: 60px 20px 40px 20px;
        background: linear-gradient(135deg, #1E2A4F 0%, #2A3A6A 100%);
        border-radius: 30px;
        color: white;
        margin-bottom: 40px;
        box-shadow: 0 20px 60px rgba(30, 42, 79, 0.3);
    }
    .hero h1 {
        font-size: 48px;
        font-weight: 700;
        margin-bottom: 12px;
    }
    .hero p {
        font-size: 18px;
        opacity: 0.9;
        max-width: 600px;
        margin: 0 auto 24px auto;
    }
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 20px;
        margin: 40px 0;
    }
    .feature-card {
        background: white;
        border-radius: 20px;
        padding: 24px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        border: 1px solid #eee;
        transition: transform 0.3s ease;
    }
    .feature-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 8px 30px rgba(201, 168, 76, 0.15);
    }
    .feature-card .icon {
        font-size: 40px;
        margin-bottom: 12px;
    }
    .btn-primary {
        background: #C9A84C;
        color: white;
        padding: 14px 40px;
        border-radius: 30px;
        border: none;
        font-size: 18px;
        font-weight: 600;
        cursor: pointer;
        text-decoration: none;
    }
    .btn-primary:hover {
        background: #B8963E;
    }
    @media (max-width: 768px) {
        .feature-grid {
            grid-template-columns: 1fr 1fr;
        }
        .hero h1 {
            font-size: 32px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">
    <h1>💰 SG WALLET</h1>
    <p>Your all-in-one platform for buying data, paying bills, sending money, and more. Fast, secure, and reliable.</p>
    <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
        <a href="?page=login" style="background: #C9A84C; color: white; padding: 14px 36px; border-radius: 30px; text-decoration: none; font-weight: 600;">Get Started</a>
        <a href="?page=login" style="background: transparent; border: 2px solid white; color: white; padding: 14px 36px; border-radius: 30px; text-decoration: none; font-weight: 600;">Login</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Features Grid
st.markdown('<div class="feature-grid">', unsafe_allow_html=True)

features = [
    ("📶", "Buy Data", "Purchase data bundles for MTN, Glo, Airtel & 9mobile instantly."),
    ("📞", "Buy Airtime", "Recharge your phone or send airtime to loved ones."),
    ("💡", "Pay Bills", "Settle electricity, cable TV, water & internet bills easily."),
    ("📤", "Send Money", "Transfer money to mobile numbers or bank accounts in seconds.")
]

for icon, title, desc in features:
    st.markdown(f"""
    <div class="feature-card">
        <div class="icon">{icon}</div>
        <h3>{title}</h3>
        <p style="color: #666; font-size: 14px;">{desc}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# CTA Section
st.markdown("""
<div style="text-align: center; padding: 40px 0;">
    <h2 style="font-size: 28px; color: #1A2A4A;">Ready to get started?</h2>
    <p style="color: #6A7A9A; margin-bottom: 20px;">Join thousands of users managing their finances with SG WALLET.</p>
    <a href="?page=register" style="background: #C9A84C; color: white; padding: 14px 40px; border-radius: 30px; text-decoration: none; font-weight: 600;">Create Free Account</a>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; padding: 20px; color: #aaa; font-size: 12px; border-top: 1px solid #eee;">
    © 2025 SG WALLET. All rights reserved. Built with ❤️ by ADLE Webdesigns
</div>
""", unsafe_allow_html=True)