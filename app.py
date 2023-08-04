import streamlit as st

def main():
    st.title("Sample Streamlit App")
    
    # Text input widget
    name = st.text_input("Enter your name", "John Doe")
    st.write(f"Hello, {name}!")

    # Number input widget
    age = st.number_input("Enter your age", min_value=0, max_value=150, value=30)
    st.write(f"You are {age} years old.")

    # Dropdown widget
    fruit_options = ["Apple", "Banana", "Orange"]
    selected_fruit = st.selectbox("Choose your favorite fruit", fruit_options)
    st.write(f"Your favorite fruit is {selected_fruit}.")

    # Checkbox widget
    agreed = st.checkbox("I agree to the terms and conditions")
    if agreed:
        st.write("Thank you for agreeing!")

    # Button widget
    if st.button("Click Me"):
        st.write("You clicked the button!")

if __name__ == "__main__":
    main()
