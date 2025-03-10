import time
from datetime import datetime
import json
from ping3 import ping
from flask import Flask, render_template
from plyer import notification  # For desktop notifications
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Initialize Flask app
app = Flask(__name__)

# File paths
MACHINE_FILE = "machines.txt"
LOG_FILE = "machine_logs.txt"
TREND_LOG = "trend_data.json"

# Dictionary to hold machine statuses
status_data = {}

# Email configuration
EMAIL_ADDRESS = "your_email@example.com"  # Replace with sender's email
EMAIL_PASSWORD = "your_password"          # Replace with sender's password
RECIPIENT_EMAIL = "recipient@example.com" # Replace with recipient's email

def load_machines():
    """Load machine names/IPs from the file."""
    with open(MACHINE_FILE, "r") as file:
        return [line.strip() for line in file if line.strip()]

def log_status(message):
    """Log status changes to a file."""
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{datetime.now()} - {message}\n")

def update_trend_data(online, offline):
    """Store machine counts over time for trend visualization."""
    try:
        with open(TREND_LOG, "r") as file:
            trend_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        trend_data = []
    
    # Append new data with timestamp
    trend_data.append({"timestamp": datetime.now().strftime("%H:%M"), "online": online, "offline": offline})
    
    # Keep only last 10 entries
    trend_data = trend_data[-10:]
    
    with open(TREND_LOG, "w") as file:
        json.dump(trend_data, file)

def send_email_alert(machine):
    """Send an email alert when a machine goes offline."""
    subject = f"Machine Offline: {machine}"
    body = f"Attention:\n\nThe machine '{machine}' has gone offline as of {datetime.now()}.\n\nPlease investigate the issue."

    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Email alert sent for {machine}.")
    except Exception as e:
        print(f"Failed to send email for {machine}: {e}")

def send_desktop_notification(machine):
    """Send a desktop notification when a machine goes offline."""
    title = "Machine Offline Alert"
    message = f"The machine '{machine}' has gone offline."
    try:
        notification.notify(
            title=title,
            message=message,
            timeout=10  # Notification stays for 10 seconds
        )
        print(f"Desktop notification sent for {machine}.")
    except Exception as e:
        print(f"Failed to send desktop notification for {machine}: {e}")

def check_machines(machines):
    """Ping machines and update their statuses."""
    global status_data
    online_count = 0
    offline_count = 0
    
    for machine in machines:
        is_online = ping(machine, timeout=2) is not None
        if machine not in status_data or status_data[machine] != is_online:
            status_data[machine] = is_online
            status_msg = "ONLINE" if is_online else "OFFLINE"
            log_status(f"Machine {machine} is {status_msg}")
            
            # Trigger alerts if the machine goes offline
            if not is_online:
                send_email_alert(machine)
                send_desktop_notification(machine)
        
        if is_online:
            online_count += 1
        else:
            offline_count += 1
    
    # Update historical trend data
    update_trend_data(online_count, offline_count)
    
    return status_data

@app.route("/")
def dashboard():
    """Render the status dashboard with trend data."""
    machines = load_machines()
    current_status = check_machines(machines)
    
    # Load historical trend data
    try:
        with open(TREND_LOG, "r") as file:
            trend_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        trend_data = []
    
    return render_template("dashboard.html", status=current_status, trend_data=trend_data, time=datetime.now())

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
