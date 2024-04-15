from abc import ABC, abstractmethod


class MessageSender(ABC):
    """
    Abstract base class representing a generic message sender interface.
    """
    @abstractmethod
    def send_message(self, recipient, message):
        '''Abstract function to send messafe to a receipt.'''
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

    def send_message(self, recipient, message):
        """
        Send an SMS message to the recipient with the specified message body.

        Parameters:
            recipient (str): The recipient phone number.
            message (str): The message body of the SMS.
        """
        print(f"Sending SMS to {recipient}: {message}")


class NotificationService:
    """
    NotificationService class depending on an abstraction (MessageSender).
    """

    def __init__(self, message_sender: MessageSender):
        self.message_sender = message_sender

    def send_notification(self, recipient, message):
        """
          Send a notification to the recipient using the configured MessageSender implementation.

          Parameters:
              recipient (str): The recipient of the notification.
              subject (str): The subject of the notification.
              message (str): The message body of the notification.
        """
        self.message_sender.send_message(recipient, message)


# Using the NotificationService with different MessageSender implementations
email_notification_service = NotificationService(
    EmailSender())  # Send via email
email_notification_service.send_notification(
    "user@example.com", "Hello, this is a notification!")

sms_notification_service = NotificationService(SmsSender())  # Send via sms
sms_notification_service.send_notification(
    "9840000000", "Hello, this is a notification!")
