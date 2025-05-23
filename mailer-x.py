import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import shutil

# Fixed Info
sender_email = "rakib121325@gmail.com"
app_password = "vtkr uyqi semd zrag"

# Design Section
def show_banner():
    os.system("clear" if os.name == "posix" else "cls")

    terminal_width = shutil.get_terminal_size().columns
    purple = "\033[95m"
    aqua = "\033[96m"
    red     = "\033[91m"
    blue = "\033[94m"
    bold = "\033[1m"
    reset = "\033[0m"

    banner_lines = [
        "███╗░░░███╗░█████╗░██╗██╗░░░░░███████╗██████╗░  ██╗░░██╗",
        "████╗░████║██╔══██╗██║██║░░░░░██╔════╝██╔══██╗  ╚██╗██╔╝",
        "██╔████╔██║███████║██║██║░░░░░█████╗░░██████╔╝  ░╚███╔╝░",
        "██║╚██╔╝██║██╔══██║██║██║░░░░░██╔══╝░░██╔══██╗  ░██╔██╗░",
        "██║░╚═╝░██║██║░░██║██║███████╗███████╗██║░░██║  ██╔╝╚██╗",
        "╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝╚══════╝╚═╝░░╚═╝  ╚═╝░░╚═╝"
    ]

    print(purple)
    for line in banner_lines:
        print(line.center(terminal_width))
    print(reset)

    print(aqua + bold + "=" * terminal_width + reset)
    print(aqua + bold + " Owner Information".center(terminal_width))
    print(aqua + bold + "   Name: Md Rakib".center(terminal_width))
    print("    Brand: Bd Ware".center(terminal_width))
    print("    Country: Bangladesh".center(terminal_width))
    print("    Telegram: https://t.me/bd_ware".center(terminal_width))
    print("    YouTube: https://youtube.com/@bd_ware".center(terminal_width))
    print(reset)
    print(aqua + bold + "=" * terminal_width + reset)
    print()

# Email validation
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# Main Function
def main():
    green = "\033[92m"
    reset = "\033[0m"

    print(">>> Running Mailer X by Bd Ware")
    show_banner()

    while True:
        receiver_email = input(green + "Receiver Email: " + reset)
        if is_valid_email(receiver_email):
            break
        else:
            print("Wrong email! Please try again.")

    sender_name = input(green + "Sender Name: " + reset)
    subject = input(green + "Subject: " + reset)
    message_text = input(green + "Message: " + reset)

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = f"{sender_name} <{sender_email}>"
    message["To"] = receiver_email
    message.attach(MIMEText(message_text, "plain"))

    try:
        print("\nSending...")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Mail has been sent successfully")
    except smtplib.SMTPAuthenticationError:
        print("Login Information (Email/Password) is wrong!")
    except Exception as e:
        print(f"Error: {e}")

# Run
if __name__ == "__main__":
    main()
