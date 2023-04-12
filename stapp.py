import streamlit as st

def main():
    st.title("My Streamlit App")
    st.write("Hello, world!")

if __name__ == "__main__":
    app = main()  # Create the Streamlit app instance
    app.run(debug=True)  # Run the app with debugging enabled