import qrcode

def generate_qr(actions):
    # Define action commands as key-value pairs
    action_map = {
        "vibrate": lambda: "intent://vibrate#Intent;scheme=qrcode;package=com.example;end",  # Android only
        "open_website": lambda url: f"http://{url}",
        "call_number": lambda number: f"tel:{number}",
        "send_sms": lambda number, message: f"sms:{number}?body={message}",  # SMS action
    }
    
    # Create a list of commands based on the actions array
    commands = []
    for action, params in actions:
        if action in action_map:
            # Check if the action needs parameters
            commands.append(action_map[action](*params))

    # Join all commands into one string
    qr_data = ";".join(commands)

    # Generate the QR code with the data
    qr = qrcode.make(qr_data)
    return qr

def get_user_actions():
    # Available actions
    available_actions = {
        "1": "vibrate",
        "2": "open_website",
        "3": "call_number",
        "4": "send_sms",
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
            params = []
            if action == "open_website":
                params.append(input("Enter the URL (without 'http://'): "))
            elif action == "call_number":
                params.append(input("Enter the phone number: "))
            elif action == "send_sms":
                params.append(input("Enter the phone number: "))
                params.append(input("Enter the message: "))
            
            actions.append((action, params))
        else:
            print("Invalid choice. Please select a valid action number.")

    return actions

# Run the script
actions = get_user_actions()
qr_code = generate_qr(actions)

# Save QR Code to file
qr_code.save("generated_qrcode.png")
print("QR Code generated and saved as generated_qrcode.png")
