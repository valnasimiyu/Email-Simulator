# Email-Simulator
### A small, in-memory email simulator that demonstrates object-oriented design
in Python. Three classes work together:
 
    Email  - a single message (sender, receiver, subject, body, timestamp, read status)
    Inbox  - a collection of Email objects with list / read / delete operations
    User   - a person who owns an Inbox and can send emails to other users
 
Nothing is saved to disk or sent over a network; everything lives in memory
for the duration of the program.
