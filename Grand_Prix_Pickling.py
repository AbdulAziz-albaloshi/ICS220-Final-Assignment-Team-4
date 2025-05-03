
import pickle
import os

# Binary file path to store Fan users
USER_DATA_FILE = "grand prix users.pkl"


# Save all users (Fan objects) to a binary file using pickle
def save_users_to_file(users_dict):
    # Try saving the dictionary of Fan objects to 'grand prix users.pkl'
    try:
        with open(USER_DATA_FILE, "wb") as file:
            pickle.dump(users_dict, file)
        print("Users saved to binary file successfully.")
    except Exception as e:
        print(f"Error while saving users: {e}")


# Load all users (Fan objects) from the binary file
def load_users_from_file():
    # Check if file exists before attempting to load
    if os.path.exists(USER_DATA_FILE):
        try:
            with open(USER_DATA_FILE, "rb") as file:
                users_dict = pickle.load(file)
            print("Users loaded from binary file successfully.")
            return users_dict
        except Exception as e:
            print(f"Error while loading users: {e}")
            return {}
    else:
        # If file doesn't exist, return empty dictionary
        print("No saved users found. Starting with empty data.")
        return {}

