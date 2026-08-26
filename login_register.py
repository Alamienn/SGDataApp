import streamlit as st
from auth import register_user, login_user, reset_password

def show_login():
    st.markdown("""
    <style>
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
            width: 100% !important;
        }
        .stButton > button:hover {
            transform: translateY(-3px) !important;
            box-shadow: 0 8px 28px rgba(201, 168, 76, 0.35) !important;
            background: linear-gradient(135deg, #D4B85C, #C9A84C) !important;
            color: white !important;
        }
        .stButton > button:active {
            transform: scale(0.96) !important;
        }
        .stTextInput > div > div > input {
            font-size: 16px !important;
            padding: 10px 14px !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🔐 Login to Your Account")
    st.markdown("Welcome back! Login to access your dashboard.")
    
    with st.form("login_form"):
        email = st.text_input("📧 Email Address", placeholder="you@example.com")
        password = st.text_input("🔑 Password", type="password", placeholder="Enter your password")
        submitted = st.form_submit_button("🔓 Login")
        
        if submitted:
            if not email or not password:
                st.error("❌ Please fill in all fields")
            else:
                success, result = login_user(email, password)
                if success:
                    st.session_state.logged_in = True
                    st.session_state.user_email = email
                    st.session_state.user_data = result
                    st.success("✅ Login successful! 🎉")
                    st.rerun()
                else:
                    st.error(f"❌ {result}")
    
    st.markdown("---")
    st.markdown("Don't have an account? [Switch to Register](#)")

def show_register():
    st.markdown("""
    <style>
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
            width: 100% !important;
        }
        .stButton > button:hover {
            transform: translateY(-3px) !important;
            box-shadow: 0 8px 28px rgba(201, 168, 76, 0.35) !important;
            background: linear-gradient(135deg, #D4B85C, #C9A84C) !important;
            color: white !important;
        }
        .stButton > button:active {
            transform: scale(0.96) !important;
        }
        .stTextInput > div > div > input {
            font-size: 16px !important;
            padding: 10px 14px !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📝 Create Your Account")
    st.markdown("Join thousands of happy users! 🎉")
    
    with st.form("register_form"):
        name = st.text_input("👤 Full Name", placeholder="John Doe")
        email = st.text_input("📧 Email Address", placeholder="you@example.com")
        phone = st.text_input("📱 Phone Number", placeholder="08012345678")
        password = st.text_input("🔑 Password", type="password", placeholder="Min 6 characters")
        confirm = st.text_input("✅ Confirm Password", type="password", placeholder="Re-enter password")
        submitted = st.form_submit_button("🚀 Create Account")
        
        if submitted:
            if not all([name, email, phone, password, confirm]):
                st.error("❌ Please fill in all fields")
            elif password != confirm:
                st.error("❌ Passwords do not match")
            elif len(password) < 6:
                st.error("❌ Password must be at least 6 characters")
            else:
                success, message = register_user(email, password, name, phone)
                if success:
                    st.success("✅ Account created! 🎉🎉🎉")
                    st.balloons()
                    st.info("💡 You can now login with your credentials.")
                else:
                    st.error(f"❌ {message}")
    
    st.markdown("---")
    st.markdown("Already have an account? [Switch to Login](#)")

def show_forgot_password():
    st.markdown("""
    <style>
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
            width: 100% !important;
        }
        .stButton > button:hover {
            transform: translateY(-3px) !important;
            box-shadow: 0 8px 28px rgba(201, 168, 76, 0.35) !important;
            background: linear-gradient(135deg, #D4B85C, #C9A84C) !important;
            color: white !important;
        }
        .stButton > button:active {
            transform: scale(0.96) !important;
        }
        .stTextInput > div > div > input {
            font-size: 16px !important;
            padding: 10px 14px !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🔐 Reset Your Password")
    st.markdown("Enter your email address and new password to reset.")
    
    with st.form("reset_form"):
        email = st.text_input("📧 Email Address", placeholder="you@example.com")
        new_password = st.text_input("🔑 New Password", type="password", placeholder="Min 6 characters")
        confirm = st.text_input("✅ Confirm Password", type="password", placeholder="Re-enter new password")
        submitted = st.form_submit_button("🔄 Reset Password")
        
        if submitted:
            if not email or not new_password or not confirm:
                st.error("❌ Please fill in all fields")
            elif new_password != confirm:
                st.error("❌ Passwords do not match")
            elif len(new_password) < 6:
                st.error("❌ Password must be at least 6 characters")
            else:
                success, message = reset_password(email, new_password)
                if success:
                    st.success("✅ Password reset successful! You can now login.")
                    st.balloons()
                else:
                    st.error(f"❌ {message}")
    
    st.markdown("---")
    st.markdown("Remember your password? [Login here](#)")