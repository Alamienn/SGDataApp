import streamlit as st

def show_header():
    """Display the SG WALLET header with logo and navigation on every page"""
    
    st.markdown("""
    <style>
        /* Premium Header Styling - HYBRID */
        .sg-header {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            padding: 16px 32px;
            border-radius: 20px;
            margin-bottom: 32px;
            box-shadow: 0 8px 32px rgba(30, 42, 79, 0.08);
            border: 1px solid rgba(201, 168, 76, 0.15);
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            transition: all 0.3s ease;
        }
        
        .sg-header:hover {
            box-shadow: 0 12px 40px rgba(201, 168, 76, 0.12);
        }
        
        .logo-section {
            display: flex;
            align-items: center;
            gap: 14px;
        }
        
        .logo-icon {
            font-size: 36px;
            background: linear-gradient(135deg, #1E2A4F, #2A3A6A);
            padding: 8px;
            border-radius: 14px;
            box-shadow: 0 4px 12px rgba(30, 42, 79, 0.2);
        }
        
        .logo-text {
            font-size: 26px;
            font-weight: 700;
            background: linear-gradient(135deg, #C9A84C, #B8963E);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: 0.5px;
            font-family: 'Segoe UI', sans-serif;
        }
        
        .logo-subtitle {
            font-size: 10px;
            color: #C9A84C;
            letter-spacing: 3px;
            text-transform: uppercase;
            opacity: 0.8;
            font-weight: 500;
        }
        
        .nav-buttons {
            display: flex;
            gap: 8px;
        }
        
        /* Premium Nav Buttons - BRIGHTER TEXT */
        .stButton button {
            background: transparent !important;
            color: #1A2A4A !important;
            border: none !important;
            padding: 10px 20px !important;
            font-weight: 600 !important;
            font-size: 14px !important;
            border-radius: 12px !important;
            transition: all 0.3s ease !important;
            font-family: 'Inter', sans-serif !important;
        }
        
        .stButton button:hover {
            background: linear-gradient(135deg, rgba(30, 42, 79, 0.08), rgba(201, 168, 76, 0.05)) !important;
            color: #C9A84C !important;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(201, 168, 76, 0.1);
        }
        
        .stButton button:active {
            transform: scale(0.96);
        }
        
        div[data-testid="column"] {
            display: flex;
            align-items: center;
        }
        
        @media (max-width: 768px) {
            .sg-header {
                flex-direction: column;
                gap: 16px;
                padding: 16px;
            }
            .nav-buttons {
                width: 100%;
                justify-content: center;
                flex-wrap: wrap;
            }
            .stButton button {
                padding: 8px 14px !important;
                font-size: 12px !important;
            }
        }
    </style>
    """, unsafe_allow_html=True)
    
    col_left, col_right = st.columns([1, 2])
    
    with col_left:
        st.markdown("""
        <div class="logo-section">
            <span class="logo-icon">💰</span>
            <div>
                <div class="logo-text">SG WALLET</div>
                <div class="logo-subtitle">✦ Premium Financial Services</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_right:
        nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)
        
        with nav_col1:
            if st.button("🏠 Home", key="nav_home", use_container_width=True):
                st.switch_page("app.py")
        
        with nav_col2:
            if st.button("📊 Analytics", key="nav_analytics", use_container_width=True):
                st.info("📈 Analytics coming soon!")
        
        with nav_col3:
            if st.button("🔔 Notifications", key="nav_notifications", use_container_width=True):
                st.info("🔔 No new notifications")
        
        with nav_col4:
            if st.button("👤 Profile", key="nav_profile", use_container_width=True):
                st.switch_page("pages/9_Profile.py")
    
    st.markdown("---")