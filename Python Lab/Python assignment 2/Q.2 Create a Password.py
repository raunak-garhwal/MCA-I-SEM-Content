while(1):
    def is_valid_password(password):
        # Check the length of the password
        if len(password) < 8:
            print("Password must be atleast eight characters long.")
            return False

        # Check for at least one uppercase letter
        has_upper = False
        for char in password:
            if 'A' <= char <= 'Z':
                has_upper = True
                break
        if has_upper == False :
            print("Your password does not have any uppercase letter.")

        # Check for at least one lowercase letter
        has_lower = False
        for char in password:
            if 'a' <= char <= 'z':
                has_lower = True
                break
        if has_lower == False :
            print("Your password does not have any lowercase letter.")

        # Check for at least one numeric digit
        has_digit = False
        for char in password:
            if '0' <= char <= '9':
                has_digit = True
                break
        if has_digit == False :
            print("Your password does not have any digit.")

        # Return True if all conditions are met
        return has_upper and has_lower and has_digit

    # Get user input for the password
    user_password = input("\nEnter your password: ")

    # Check if the password is valid
    if is_valid_password(user_password):
        print("\nYour entered Password is valid!\n")
        break
    else:
        print("So, Please enter the Password again!")