from abc import ABC, abstractmethod

class MessageSender(ABC):
  """
  Abstract base class representing a generic message sender interface.
  """
  @abstractmethod
  def send_message(self, recipient, subject, message):
    pass

class EmailSender(MessageSender):
  """
  Concrete class implementing the MessageSender interface for sending emails.
  """
  def send_message(self, recipient, message):
    print(f"Sending email to {recipient}: - {message}")

class SmsSender(MessageSender):
  """
  Concrete class implementing the MessageSender interface for sending SMS.
  """
  def send_message(self, phone, message):
    print(f"Sending SMS to {phone}: {message}")

class NotificationService:
  """
  NotificationService class depending on an abstraction (MessageSender).
  """
  def __init__(self, message_sender: MessageSender):
    self.message_sender = message_sender

  def send_notification(self, recipient, message):
    self.message_sender.send_message(recipient, message)


# Using the NotificationService with different MessageSender implementations
email_notification_service = NotificationService(EmailSender())  # Send via email
email_notification_service.send_notification("user@example.com", "Hello, this is a notification!")

sms_notification_service = NotificationService(SmsSender())  # Send via sms
sms_notification_service.send_notification("9840000000", "Hello, this is a notification!")
