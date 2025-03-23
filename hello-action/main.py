import os

def main():
    name = os.getenv('NAME', 'World')
    greeting = os.getenv('GREETING', 'Hello')
    message = f"{greeting}, {name}!"
    
    # Print the message (this will be captured as output)
    print(f"::set-output name=message::{message}")

if __name__ == "__main__":
    main()
