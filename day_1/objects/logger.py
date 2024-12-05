from contextlib import ContextDecorator
from datetime import datetime


class log(ContextDecorator):
    """https://docs.python.org/3/library/contextlib.html"""

    def __init__(self, logfile='log.txt'):
        self.logfile = logfile

    def __enter__(self):
        with open(self.logfile, 'a') as f:
            f.write(f"Block enter at {datetime.now()}\n")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        with open(self.logfile, 'a') as f:
            f.write(f"Block exit at {datetime.now()}\n")
        return False

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            with open(self.logfile, 'a') as f:
                f.write(f"Function {func.__name__} called at {datetime.now()}\n")
            return func(*args, **kwargs)
        return wrapper
