import os

def main():
    name = os.getenv('NAME', 'World')
    greeting = os.getenv('GREETING', 'Hello')
    message = f"{greeting}, {name}!"

    print(message)

if __name__ == "__main__":
    main()
