import streamlit as st

# Initialize session state, this creates empty variables with 0, None Values

if "balance" not in st.session_state:
    st.session_state.balance = 0
if "user_name" not in st.session_state:
    st.session_state.user_name = None
if "pin" not in st.session_state:
    st.session_state.pin = None
if "verified" not in st.session_state:
    st.session_state.verified = False
if "menu" not in st.session_state:
    st.session_state.menu = False

# We are creating the username in this function


def create_username():

    # this is the home page

    st.subheader("AADHAR : VERIFIED ✅")
    st.subheader("PAN CARD : VERIFIED ✅")
    st.write("YOU CAN REGISTER YOUR NAME AND SET A PIN:")

    # inputs to Mainframe

    user_name = st.text_input("USER NAME:")
    pin = st.text_input("SET A 4-DIGIT PIN:", type="password")

    # verifying the size and datatype and pin

    if st.button("Register"):
        if pin.isdigit() and len(pin) == 4:
            st.session_state.user_name = user_name
            st.session_state.pin = pin
            st.success(f"Hi, {user_name}. You are registered successfully 🎉")
        else:
            st.error("PIN must be 4 digits.")

# verifying pin for extra safety


def verify_pin():
    st.write(f"Hi, {st.session_state.user_name}..")
    st.write("Please, Enter your PIN to continue services:")

    # Pin to Verify

    pin2 = st.text_input("VERIFY YOUR PIN:", type="password")
    if st.button("Verify"):

        # verification

        if pin2 == st.session_state.pin:
            st.session_state.verified = True
            st.success("VERIFIED ✅. THANK YOU FOR THE CO-OPERATION 😊")
        else:
            st.error("❌ INVALID PIN. Try again.")

# To put Money in a new Account


def initial_deposit():
    st.header("Initial Deposit")
    deposit = st.number_input(
        "Enter the amount to deposit:", min_value=0, step=1)

    if st.button("Confirm Deposit"):
        st.session_state.balance += deposit
        st.success(
            f"{deposit}₹ deposited successfully! 🎉 Your total balance: ₹ {st.session_state.balance}")

# This is the HUB of all the functions where the complete process is integrated


def menu():

    # Showing Options to perforn functions in the ACCOUNT

    st.subheader("What services do you want?")
    option = st.radio("Choose an option:", [
                      "Withdraw", "Deposit", "Check Balance", "Exit"])

    # to Withdraw

    if option == "Withdraw":
        debit = st.number_input(
            "Enter the amount to withdraw:", min_value=0, step=1)
        if st.button("Withdraw"):

            # operation is performed

            if debit <= st.session_state.balance:
                st.session_state.balance -= debit
                st.success(
                    f"Amount withdrawn. Balance left: {st.session_state.balance}")
            else:
                st.error("INSUFFICIENT BALANCE !!")

    # to Deposit

    elif option == "Deposit":
        credit = st.number_input(
            "Enter the amount to deposit:", min_value=0, step=1)

        # operation is performed

        if st.button("Deposit"):
            st.session_state.balance += credit
            st.success(
                f"Amount deposited. Balance left: {st.session_state.balance}")

    # to check balance

    elif option == "Check Balance":

        # To view Balance

        if st.button("Show Balance"):
            st.info(f"The current balance is: {st.session_state.balance}")

    # To exit the Program

    elif option == "Exit":
        st.warning("Thank you for using ATB Bank services 🙏")
        st.session_state.menu = False

# The initiater and Command Center, of the whole program..


def main():
    st.title("🏦 ATB BANKING SERVICES")

    if st.session_state.user_name is None:
        create_username()

    elif not st.session_state.verified:
        verify_pin()

    elif st.session_state.balance is 0:
        initial_deposit()

    else:
        menu()


if __name__ == "__main__":

    # the code starts the execution from here

    main()
