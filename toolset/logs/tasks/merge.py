"""Toolset merge logs command module."""

from invoke import task

from toolset.logs.parser import Parser
from toolset.logs.constants import LogSeverity


@task(iterable=['file'], optional=['level'], help={
    'file': 'Log file name to merge',
    'level': 'Minimum log level. Default: debug'
})
def merge(ctx, file, level=LogSeverity.DEBUG):
    """Parse, merge, sort log files and exclude log records up to severity level."""
    if len(file) < 2:
        raise ValueError('Should be at least 2 files to merge')
    parser = Parser(file, level)
    parser.merge()
