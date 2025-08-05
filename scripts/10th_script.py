# Automating Email Access
import imaplib
import email
from email.header import decode_header

# Connect to Gmail IMAP server
imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login("your_email@gmail.com", "your_app_password")  # Use app password for Gmail

# Select inbox
imap.select("inbox")

# Search for unread emails
status, messages = imap.search(None, 'UNSEEN')
for num in messages[0].split():
    status, data = imap.fetch(num, "(RFC822)")
    msg = email.message_from_bytes(data[0][1])

    subject, encoding = decode_header(msg["Subject"])[0]
    if isinstance(subject, bytes):
        subject = subject.decode(encoding or "utf-8")
    print("Subject:", subject)

    # Download attachments
    for part in msg.walk():
        if part.get_content_disposition() == "attachment":
            filename = part.get_filename()
            if filename:
                with open(filename, "wb") as f:
                    f.write(part.get_payload(decode=True))
                print(f"Downloaded: {filename}")

imap.logout()
