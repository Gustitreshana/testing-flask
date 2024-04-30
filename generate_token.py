import secrets

# Generate a secure token
token = secrets.token_urlsafe(256)
print("Generated token:", token)
