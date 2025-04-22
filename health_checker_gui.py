import tkinter as tk
import psutil
import platform
import socket

def check_health():
    # Get system info
    system = platform.system() + " " + platform.release()
    cpu = f"{psutil.cpu_percent()}%"
    memory = f"{psutil.virtual_memory().percent}%"
    disk = psutil.disk_usage('/')

    # Check internet
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        internet = "Connected"
    except OSError:
        internet = "Not Connected"

    # Update labels
    result.set(
        f"System: {system}\n"
        f"CPU Usage: {cpu}\n"
        f"Memory Usage: {memory}\n"
        f"Disk Usage: {disk.used // (2**30)} GB used of {disk.total // (2**30)} GB\n"
        f"Internet: {internet}"
    )

# Create window
window = tk.Tk()
window.title("System Health Checker")
window.geometry("400x250")

# Create widgets
result = tk.StringVar()
label = tk.Label(window, textvariable=result, justify="left", font=("Arial", 11))
label.pack(pady=10)

button = tk.Button(window, text="Check System Health", command=check_health, font=("Arial", 12))
button.pack(pady=10)

# Default message
result.set("Click the button to check system health.")

# Run app
window.mainloop()
