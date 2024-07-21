import random

class OTPGenerator:

    def generate_otp():
        # Generate a 6 digit code
        return "".join(str(random.randint(0, 9)) for _ in range(6))

class OTPVerifier:

    def verify_otp(user_otp, generated_otp):
        return user_otp == generated_otp

# Example usage:
generated_otp = OTPGenerator.generate_otp()
print(f"Generated OTP: {generated_otp}")

# Simulating user input (you can replace this with an actual input mechanism)
user_input_otp = input("Enter the OTP for verification: ")

if OTPVerifier.verify_otp(user_input_otp, generated_otp):
    print("OTP verified successfully!")
else:
    print("OTP verification failed.")
