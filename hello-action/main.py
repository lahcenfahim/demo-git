import sys
import os
import json

def main():
    # Get inputs from environment variables
    name = os.getenv('INPUT_NAME', 'World')
    greeting = os.getenv('INPUT_GREETING', 'Hello')
    
    # Create the greeting message
    message = f"{greeting}, {name}!"
    
    # Print the message to the console (for GitHub Actions to capture)
    print(message)
    
    # Set the output variable to message
    with open(os.getenv('GITHUB_ENV'), 'a') as f:
        f.write(f"GREETING_MESSAGE={message}\n")

if __name__ == '__main__':
    main()
