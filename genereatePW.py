import secrets

def generate_password(length):
    """Generate a securely random password of the specified length."""
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    password = ""
    for i in range(length):
        password += alphabet[secrets.randbelow(len(alphabet))]
    return password

print("Generated Password:", generate_password(16))

def test_generate_password():
    """Test the generate_password function."""
    length = 16
    password = generate_password(length)
    assert len(password) == length, "Password length is incorrect"
    assert any(c.islower() for c in password), "Password must contain at least one lowercase letter"
    # print final conclusion after all tests are done
    print("All tests passed!")

test_generate_password()
