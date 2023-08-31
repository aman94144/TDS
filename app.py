import streamlit as st

def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    st.title("Find the Largest Number")
    
    st.write("Enter three numbers and click the button to find the largest:")
    
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")
    
    if st.button("Find Largest"):
        largest = find_largest(num1, num2, num3)
        st.write(f"The largest number is: **{largest}**")
        st.balloons()  # Add a fun effect when the largest number is displayed

if __name__ == "__main__":
    main()
