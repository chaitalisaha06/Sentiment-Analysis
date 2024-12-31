import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="Happy New Year!", page_icon="🎉", layout="centered")

# Define the main function
def main():
    # Display the New Year message
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>🎉 Happy New Year! 🎉</h1>
            <p style="font-size: 18px;">May we start the new year together?</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # Create two "Yes" buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Yes", key="button1"):
            st.success("Great! Let's make it a wonderful year ahead!")
    
    with col2:
        if st.button("Yes", key="button2"):
            st.success("Great! Let's make it a wonderful year ahead!")

# Run the app
if __name__ == "__main__":
    main()
