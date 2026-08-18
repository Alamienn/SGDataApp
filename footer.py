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
            font-family: 'Playfair Display', serif;
            font-size: 20px;
            font-weight: 700;
            margin-bottom: 8px;
            color: white;
        }
        
        .footer-brand span {
            color: #C9A84C;
        }
        
        .footer-subtitle {
            font-family: 'Inter', sans-serif;
            font-size: 12px;
            color: #7A8AA8;
            letter-spacing: 4px;
            text-transform: uppercase;
        }
        
        .footer-divider {
            border-top: 1px solid rgba(201, 168, 76, 0.1);
            margin: 20px 0;
        }
        
        .footer-credit {
            font-family: 'Inter', sans-serif;
            font-size: 14px;
            color: #E8D5A8;
        }
        
        .footer-credit a {
            color: #C9A84C;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s ease;
        }
        
        .footer-credit a:hover {
            color: #D4B85C;
            text-decoration: underline;
        }
        
        .footer-social {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 12px;
        }
        
        .footer-social a {
            color: #7A8AA8;
            text-decoration: none;
            font-size: 20px;
            transition: color 0.3s ease;
        }
        
        .footer-social a:hover {
            color: #C9A84C;
            transform: translateY(-2px);
        }
        
        .footer-copyright {
            font-family: 'Inter', sans-serif;
            font-size: 11px;
            color: #5A6A8A;
            letter-spacing: 1px;
        }
        
        .footer-copyright span {
            color: #C9A84C;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="footer-premium">
        <div class="footer-brand">
            ✦ <span>ADLE Webdesigns</span> ✦
        </div>
        <div class="footer-subtitle">Premium Digital Solutions</div>
        
        <div class="footer-divider"></div>
        
        <div class="footer-credit">
            📧 <a href="mailto:alamienn02@yahoo.com">alamienn02@yahoo.com</a>
        </div>
        
        <div class="footer-social">
            <a href="#" title="Instagram">📱</a>
            <a href="#" title="Twitter">🐦</a>
            <a href="#" title="WhatsApp">💬</a>
            <a href="#" title="Email">📧</a>
        </div>
        
        <div class="footer-divider"></div>
        
        <div class="footer-copyright">
            © 2025 SG WALLET. All rights reserved. <span>✦</span> Premium Financial Services
        </div>
    </div>
    """, unsafe_allow_html=True)