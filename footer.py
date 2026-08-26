import streamlit as st

def show_footer():
    """Display the premium footer on every page"""
    
    st.markdown("""
    <style>
        .footer-premium {
            background: linear-gradient(135deg, #1E2A4F 0%, #2A3A6A 100%);
            border-radius: 20px;
            padding: 32px 40px;
            margin-top: 40px;
            text-align: center;
            border: 1px solid rgba(201, 168, 76, 0.15);
            box-shadow: 0 8px 32px rgba(30, 42, 79, 0.2);
        }
        .footer-brand {
            font-size: 20px;
            font-weight: 700;
            margin-bottom: 8px;
            color: white;
        }
        .footer-brand span {
            color: #C9A84C;
        }
        .footer-subtitle {
            font-size: 12px;
            color: #A8B8D8;
            letter-spacing: 4px;
            text-transform: uppercase;
        }
        .footer-divider {
            border-top: 1px solid rgba(201, 168, 76, 0.1);
            margin: 20px 0;
        }
        .footer-credit {
            font-size: 14px;
            color: #E8D5A8;
        }
        .footer-credit a {
            color: #C9A84C;
            text-decoration: none;
            font-weight: 500;
        }
        .footer-credit a:hover {
            color: #D4B85C;
        }
        .footer-social a {
            color: #A8B8D8;
            text-decoration: none;
            font-size: 20px;
            margin: 0 10px;
            transition: color 0.3s ease;
        }
        .footer-social a:hover {
            color: #C9A84C;
        }
        .footer-copyright {
            font-size: 11px;
            color: #6A7A9A;
            letter-spacing: 1px;
        }
        .footer-copyright span {
            color: #C9A84C;
        }
    </style>
    
    <div class="footer-premium">
        <div class="footer-brand">✦ <span>ADLE Webdesigns</span> ✦</div>
        <div class="footer-subtitle">Premium Digital Solutions</div>
        <div class="footer-divider"></div>
        <div class="footer-credit">📧 <a href="mailto:alamienn02@yahoo.com">alamienn02@yahoo.com</a></div>
        <div class="footer-divider"></div>
        <div class="footer-copyright">© 2025 SG WALLET. All rights reserved. <span>✦</span> Premium Financial Services</div>
    </div>
    """, unsafe_allow_html=True)