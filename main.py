import random


class PaymentContextManager:
    def __enter__(self):
        print("Payment processing context activated.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            if isinstance(exc_value, ValueError) and "Insufficient funds" in str(exc_value):
                print("Error: Insufficient funds. Please deposit more funds or choose a smaller amount.")
            else:
                print(f"Error occurred during payment processing: {exc_value}")
                # Additional error handling logic can be added here, such as logging the error.
        else:
            print("Payment processed successfully.")
        print("Payment processing context deactivated.")


def process_payment(user_id, amount):
    # Simulate random errors
    if random.random() < 0.2:
        raise ValueError("Transaction failed: Insufficient funds.")

    # Simulate successful payment
    print(f"Processing payment of ${amount} for user {user_id}...")
    # Insert payment transaction into database (simulated)
    print("Transaction successful.")


# Tasks:
# 1. Process a payment with sufficient funds.
# 2. Process a payment with insufficient funds (error).
# 3. Process multiple payments in a loop.

# Task 1: Process a payment with sufficient funds
print("\nTask 1: Process a payment with sufficient funds")
with PaymentContextManager():
    process_payment(1, 50)

# Task 2: Process a payment with insufficient funds (error)
print("\nTask 2: Process a payment with insufficient funds")
with PaymentContextManager():
    try:
        process_payment(2, 100)
    except ValueError as e:
        print(f"Error: {e}")

# Task 3: Process multiple payments in a loop
print("\nTask 3: Process multiple payments in a loop")
with PaymentContextManager():
    for i in range(3):
        amount = random.randint(10, 30)
        print(f"\nPayment {i + 1}:")
        try:
            process_payment(i + 1, amount)
        except ValueError as e:
            print(f"Error: {e}")