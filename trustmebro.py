import qrcode

def generate_qr(actions, platform):
    # Define action commands as key-value pairs
    action_map = {
        "vibrate": lambda: "vibrate://",  # iOS compatible vibrate command
        "open_website": lambda url: f"http://{url}",
        "call_number": lambda number: f"tel:{number}",
    }

    # Adjust commands for Android if necessary (can add more variations)
    if platform.lower() == 'android':
        action_map["vibrate"] = lambda: "intent://vibrate#Intent;scheme=qrcode;package=com.example;end"

    # Create a list of commands based on the actions array
    commands = []
    for action, param in actions:
        if action in action_map:
            # Check if the action needs a parameter (like a URL or phone number)
            if param:
                commands.append(action_map[action](param))
            else:
                commands.append(action_map[action]())

    # Join all commands into one string
    qr_data = ";".join(commands)  # Adjust separator if needed

    # Generate the QR code with the data
    qr = qrcode.make(qr_data)
    return qr

def get_user_actions():
    # Available actions
    available_actions = {
        "1": "vibrate",
        "2": "open_website",
        "3": "call_number",
    }
    
    actions = []
    print("Choose actions to include in the QR code:")
    for key, action in available_actions.items():
        print(f"{key}. {action}")
    
    while True:
        choice = input("Enter the number of the action you want to add (or 'done' to finish): ")
        
        if choice.lower() == 'done':
            break
        elif choice in available_actions:
            action = available_actions[choice]
            
            # Ask for parameters if needed
            param = None
            if action == "open_website":
                param = input("Enter the URL (without 'http://'): ")
            elif action == "call_number":
                param = input("Enter the phone number: ")
            
            actions.append((action, param))
        else:
            print("Invalid choice. Please select a valid action number.")
    
    return actions  # Make sure to return the actions list

def get_platform_choice():
    while True:
        platform = input("Which platform are you using? (iPhone/Android): ")
        if platform.lower() in ['iphone', 'android']:
            return platform
        else:
            print("Invalid choice. Please enter 'iPhone' or 'Android'.")

# Run the script
platform = get_platform_choice()
actions = get_user_actions()
qr_code = generate_qr(actions, platform)

# Save QR Code to file
qr_code.save("generated_qrcode.png")
print("QR Code generated and saved as generated_qrcode.png")
