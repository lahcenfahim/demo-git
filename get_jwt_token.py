import jwt
import time
import argparse

def generate_jwt(app_id, private_key_path):
    """
    Generate a JWT (JSON Web Token) for authenticating a GitHub App.
    
    :param app_id: GitHub App ID
    :param private_key_path: Path to the GitHub App private key (PEM file)
    :return: JWT token as a string
    """
    with open(private_key_path, "r") as key_file:
        private_key = key_file.read()

    # Current time
    now = int(time.time())

    # JWT payload
    payload = {
        'iat': now,           # Issued at time
        'exp': now + 600,     # JWT expiration time (maximum 10 minutes)
        'iss': app_id         # GitHub App ID
    }

    # Generate the JWT
    token = jwt.encode(payload, private_key, algorithm="RS256")
    
    return token

if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser(description="Generate a JWT for GitHub App authentication.")
    parser.add_argument('-app_id', type=str, required=True, help="GitHub App ID")
    parser.add_argument('-private_key_path', type=str, required=True, help="Path to the GitHub App private key (PEM file)")
    
    args = parser.parse_args()

    # Generate JWT
    jwt_token = generate_jwt(args.app_id, args.private_key_path)
    
    # Print the token (this can be captured in the workflow)
    print(jwt_token)
