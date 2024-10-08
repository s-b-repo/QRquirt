import qrcode

def generate_qr(actions, platform):
    # Define action commands as key-value pairs (including new control actions)
    action_map = {
        "vibrate": lambda: "vibrate://",  # iOS compatible vibrate command
        "open_website": lambda url: f"http://{url}",
        "call_number": lambda number: f"tel:{number}",
        "install_app": lambda app_id: f"market://details?id={app_id}",  # Install Play Store App
        "turn_flashlight_on": lambda: "intent://flashlight/on#Intent;scheme=qrcode;package=com.example;end",
        "turn_flashlight_off": lambda: "intent://flashlight/off#Intent;scheme=qrcode;package=com.example;end",
        "take_picture": lambda: "intent://camera#Intent;action=android.media.action.IMAGE_CAPTURE;end",  # Open camera to take a picture
        "rickroll": lambda: "http://youtube.com/watch?v=dQw4w9WgXcQ",  # Rickroll link
        "fake_update": lambda: "http://fake-update.com",  # Fake OS update screen
        "random_fact": lambda: "http://uselessfacts.net",  # Sends to a useless facts page
        "cat_video": lambda: "http://youtube.com/watch?v=J---aiyznGQ",  # Funny cat video
        "annoying_beep": lambda: "http://beep.com/beep.wav",  # A loud, annoying beep sound
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
    qr_data = ";".join(commands)

    # Generate the QR code with the data
    qr = qrcode.make(qr_data)
    return qr

def get_user_actions():
    # Available actions including new phone control actions
    available_actions = {
        "1": "vibrate",
        "2": "open_website",
        "3": "call_number",
        "4": "install_app",
        "5": "turn_flashlight_on",
        "6": "turn_flashlight_off",
        "7": "take_picture",
        "8": "rickroll",
        "9": "fake_update",
        "10": "random_fact",
        "11": "cat_video",
        "12": "annoying_beep",
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
            elif action == "install_app":
                param = input("Enter the Play Store app ID (e.g., com.example.app): ")
            
            actions.append((action, param))
        else:
            print("Invalid choice. Please select a valid action number.")
    
    return actions

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
