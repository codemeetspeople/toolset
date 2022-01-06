"""Toolset parser module."""

import re
import heapq

from toolset.logs.constants import LogSeverity


class Parser:
    """Class for log files parsing & merging."""

    def __init__(self, files: list[str, ...], level: str = LogSeverity.DEBUG):
        """Initialize Parser instance.

        Arguments:
            files -- list of file names
            level -- Log severity. Possible values (debug, info, warning, error, critical). Default: debug

        Usage:
            parser = Parser(['f1.log', 'f2.log'], 'error')
            parser.merge()
        """
        self._files = files
        self._level = level
        self._limit_level = False
        self._levels = LogSeverity.all()

        try:
            if self._levels.index(level) != 0:
                self._limit_level = True
                self._levels = self._levels[self._levels.index(level):]
        except ValueError:
            pass

    def prepare_file(self, file_name: str) -> list[str, ...]:
        """Prepare file for future  processing.

        Arguments:
            file_name: Log file name
        """
        with open(file_name, 'r') as source:
            if self._limit_level:
                return [
                    x.group() for x in re.finditer(
                        rf'^.+\] \[({"|".join(self._levels)})\] \[.*$', source.read(), re.M
                    )
                ]
            return source.readlines()

    def merge(self):
        """Merge log files."""
        merged = heapq.merge(*(map(lambda x: self.prepare_file(x), self._files)))
        print('\n'.join(merged))
