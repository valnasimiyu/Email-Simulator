import datetime
import re

def is_valid_address(address):
    pattern = r'^[^@\s]+@[^@\s]+\.[^@\s]+$'
    return isinstance(address, str) and re.match(pattern, address) is not None

class Email:
    def __init__(self, sender, receiver, subject, body):
        # sender and receiver are User objects 
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        # Record the moment the email object was created
        self.timestamp = datetime.datetime.now()
        # New emails always start out unread.
        self.read = False

    def mark_as_read(self):
        self.read = True

    def display_full_email(self):
        # Opening an email counts as reading it
        self.mark_as_read()
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        # strftime formats the datetime as e.g. "2026-10-18 14:30".
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

    def __str__(self):
        status = 'Read' if self.read else 'Unread'
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

class User:
    def __init__(self, name,address):
         if not is_valid_address(address):
            raise ValueError(f'Invalid email address: {address}')
        self.name = name
        self.address = address
        # Every user gets a fresh, empty inbox.
        self.inbox = Inbox()

    def send_email(self, receiver, subject, body):
        if not isinstance(receiver, User):
            print('Error: receiver must be a User.\n')
            return False
        if not subject or not subject.strip():
            print('Error: subject cannot be empty.\n')
            return False
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        # Delivery = appending the email to the receiver's inbox.
        receiver.inbox.receive_email(email)
        print(f'Email sent from {self.name} to {receiver.name}!\n')

    def check_inbox(self):
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    def read_email(self, index):
        self.inbox.read_email(index)

    def delete_email(self, index):
        self.inbox.delete_email(index)

class Inbox:
    def __init__(self):
        # Emails are kept in arrival order (oldest first).
        self.emails = []

    def receive_email(self, email):
        self.emails.append(email)

    def list_emails(self):
        if not self.emails:
            print('Your inbox is empty.\n')
            return
        print('\nYour Emails:')
        # start=1 so users see friendly numbering (1, 2, 3...) instead of 0-based.
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')

    def read_email(self, index):
        """Display the full email at the given 1-based index, with validation."""
        if not self.emails:
            print('Inbox is empty.\n')
            return
        # Convert the user's 1-based number to Python's 0-based list index.
        actual_index = index - 1
        # Guard against out-of-range numbers (zero, negatives, too large).
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        self.emails[actual_index].display_full_email()

    def delete_email(self, index):
         """Remove the email at the given 1-based index, with validation."""
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        # Deleting shifts later emails up, so remaining numbers change.
        del self.emails[actual_index]
        print('Email deleted.\n')

def main():
  def main():
    tory = User('Tory', 'tory@example.com')
    ramy = User('Ramy', 'ramy@example.com')

    tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
    tory.send_email(ramy, '   ', 'This should fail')    # empty subject
    tory.send_email('not a user', 'Hi', 'This too')      # bad receiver
    ramy.check_inbox()
# Only run the demo when this file is executed directly,
# not when it is imported as a module.
if __name__ == '__main__':
    main()
