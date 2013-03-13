from logging import getLogger, Filter, Formatter, DEBUG, WARNING
from logging.handlers import SysLogHandler, TimedRotatingFileHandler
from os.path import abspath, dirname, exists
from sys import platform

import gdrivefs

default_logger = getLogger()
default_logger.setLevel(WARNING)

# Log to syslog.

if platform == "darwin":
    # Apple made 10.5 more secure by disabling network syslog:
    address = "/var/run/syslog"
elif exists('/dev/log'):
    address = '/dev/log'
else:
    address = ('localhost', 514)

log_syslog = SysLogHandler(address, facility=SysLogHandler.LOG_LOCAL0)
log_format = 'GD: %(name)-12s %(levelname)-7s %(message)s'
log_syslog.setFormatter(Formatter(log_format))
default_logger.addHandler(log_syslog)

# Log to physical file.

#root_path = abspath(dirname(gdrivefs.__file__) + '/..')
#log_filepath = ('%s/logs/gdrivefs.log' % (root_path))
#log_file = TimedRotatingFileHandler(log_filepath, 'D', backupCount=5)
#log_file.setFormatter(Formatter('%(asctime)s [%(name)s %(levelname)s] %(message)s'))
#default_logger.addHandler(log_file)

