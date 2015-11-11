import logbook


class DevelopmentLoggingSetup(object):
    """
    Base Logging setup class based on logbook.
    """
    format_string = None
    handlers = None

    def __init__(self, log_level, format_string=None):
        self.handlers = []
        self.log_level = log_level

        if not format_string:
            self.format_string = '[{record.time}]: {record.level_name} - {record.channel}: {record.message}'

    def add_handler(self, handler):
        self.handlers.append(handler)

    def add_stderr_log(self):
        stderr_handler = logbook.StderrHandler(level=self.log_level)
        stderr_handler.format_string = self.format_string
        stderr_handler.formatter

        self.add_handler(stderr_handler)

    def add_file_handler(self, file_path):
        file_handler = logbook.FileHandler(file_path, level=self.log_level)
        file_handler.format_string = self.format_string
        file_handler.formatter

        self.add_handler(file_handler)

    def get_nested_setup(self):
        return logbook.NestedSetup(self.handlers)

    def set_default_setup(self, logger, file_path='application.log'):

        self.add_stderr_log()

        self.add_file_handler(file_path)
        for handler in self.handlers:
            logger.handlers.append(handler)
        # return self.get_nested_setup()
