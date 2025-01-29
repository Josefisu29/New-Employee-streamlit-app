import streamlit as st
# Function to toggle the visibility of the pay input based on employee type
def toggle_pay_input(employee_type):
    return bool(employee_type)

# Function to create employee information
def create_employee():
    # Input fields for Employee Information
    firstname = st.text_input("First Name")
    secondname = st.text_input("Second Name")
    employee_type = st.selectbox("Select Employee Type", ["", "Part-Time", "Full-Time"])

    # Show pay input if an employee type is selected
    show_pay_input = toggle_pay_input(employee_type)
    if show_pay_input:
        pay = st.number_input(f"Enter {'Weekly Pay' if employee_type == 'Part-Time' else 'Monthly Pay'}", min_value=0)
    else:
        pay = None

    # Address input fields
    street_number = st.number_input("Street Number", min_value=1)
    street_name = st.text_input("Street Name")
    state_code = st.text_input("State Code")
    state_name = st.text_input("State Name")

    # Button to create employee
    if st.button("Create Employee"):
        if firstname and secondname and employee_type and pay and street_number and street_name and state_code and state_name:
            pay_type = "Weekly Pay" if employee_type == "Part-Time" else "Monthly Pay"
            # Display employee details
            st.success("Employee Created Successfully!")
            st.write(f"**First Name**: {firstname}")
            st.write(f"**Second Name**: {secondname}")
            st.write(f"**Employee Type**: {employee_type}")
            st.write(f"**{pay_type}**: ${pay}")
            st.write(f"**Address**: {street_number} {street_name}, {state_code} {state_name}")
        else:
            st.error("Please fill in all fields.")

# Main function to run the app
def main():
    st.title("Employee Information")
    create_employee()

# Run the app if this script is executed directly
if __name__ == "__main__":
    main()
