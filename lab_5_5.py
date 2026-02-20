#Generate a Python script that logs user activity including username, IP address, and timestamp.The code should clearly show how user activity is recorded.Also explain what data is being logged and whether any sensitive information is included.Add comments to make the logging process transparent and easy to understand.from ast import Add
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="user_activity.log",
    level=logging.INFO,
    format="%(message)s"
)

def log_user_activity(username, ip_address):
    """Logs user activity with username, IP address, and timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"User: {username}, IP: {ip_address}, Time: {timestamp}"
    logging.info(log_message)

# Example usage
log_user_activity("alice", "192.168.1.25")
print("User activity logged successfully.")
