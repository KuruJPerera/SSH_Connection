import paramiko  # Import for SSH connections

def ssh_connect(target_ip, username, password):
    # Create an SSH client instance
    client = paramiko.SSHClient()

    # Automatically accept unknown host keys
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Attempt to connect using the given username and password
    try:
        client.connect(target_ip, username=username, password=password, timeout=5)
        print(f"Success! Connected to {target_ip} with Username: {username}, Password: {password}")
    except paramiko.AuthenticationException:
        print(f"Authentication failed for Username: {username}, Password: {password}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()  # Close the connection after attempt

# Usage
target = input("Enter target IP: ")
user = input("Enter SSH username: ")
password = input("Enter the known password: ")

ssh_connect(target, user, password)
