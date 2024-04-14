from abc import ABC, abstractmethod
import logging

class Logger(ABC):
  """Abstract base class representing a logger."""
  @abstractmethod
  def log(self, message, level):
    pass

class FileLogger(Logger):
  """Class for filelogger"""
  def __init__(self, filename):
    self.logger = logging.getLogger(__name__+'-filelog')
    self.logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(filename)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    self.logger.addHandler(file_handler)

  def log(self, message):
    self.logger.info(message)

class ConsoleLogger(Logger):
  """Class for consolse logger"""
  def __init__(self):
    self.logger = logging.getLogger(__name__+'-consolelog')
    self.logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    self.logger.addHandler(console_handler)

  def log(self, message):
    self.logger.info(message)

class DatabaseLogger(Logger):
  """Class for database logger."""
  def __init__(self,filename):
    self.logger = logging.getLogger(__name__+'-dblog')
    self.logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(filename)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    self.logger.addHandler(file_handler)

  def log(self, message):
        self.logger.info(message)



def create_logger(log_type, *args):
    """Creates a logger object based on the type and optional arguments."""
    try:  
        if log_type == "file":
            return FileLogger(*args)
        elif log_type == "console":
            return ConsoleLogger()
        elif log_type == "database":
            return DatabaseLogger(*args)
        else:
            raise ValueError("Invalid logger type")
    except:
       print('Failed to create logger.')

def main():
  logs = {'file':'file.log','database':'database.log','console':'console.log'}
  loggers = {}

  for log_type,filename in logs.items():
    loggers[log_type]=create_logger(log_type,filename)
    
  loggers['file'].log("This is a file log")
  loggers['database'].log("This is a database log")
  loggers['console'].log("This is a console log")

if __name__ == "__main__":
  main()
