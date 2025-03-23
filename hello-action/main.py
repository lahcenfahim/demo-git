import os

def main():
    name = os.getenv('NAME', 'World')
    greeting = os.getenv('GREETING', 'Hello')
    message = f"{greeting}, {name}!"

    # Set output using environment files
    with open(os.environ['GITHUB_ENV'], 'a') as env_file:
        env_file.write(f"message={message}\n")

if __name__ == "__main__":
    main()
