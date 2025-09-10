import streamlit as st

st.set_page_config(page_title="Pollution Source Identifier")

st.title(" AI-Powered Pollution Source Identifier")

city = st.text_input("Enter a city name", placeholder="e.g., Delhi")

if st.button("Analyze"):
    if city.strip() == "":
        st.warning(" Please enter a valid city name.")
    else:
        st.success(f"Analyzing pollution sources for: {city}")
        st.markdown(f"""
        ###  AI Analysis Results for **{city}** (Simulated)
        - **Main Pollutants:** PM2.5, NOx, SO2
        - **Likely Sources:**
            -  Vehicle emissions
            - Industrial activity
            -  Biomass/garbage burning
        - **Air Quality Index (AQI):** 185 (Unhealthy)
        - **Recommendation:** Limit outdoor activity. Use masks. Air purifiers recommended indoors.
        """)
