"""Toolset package entry point script.

Usage (from command-line):
    toolset [--core-opts] <subcommand> [--subcommand-opts]

Available commands:
    toolset shell => Python shell with asyncio support
    toolset logs.merge => Parse, merge, sort log files and exclude log records up to severity level
"""

from invoke import Collection, Program

from toolset.version import __version__
from toolset.logs.tasks import ns as logs_tasks


from toolset.core.tasks.shell import shell

ns = Collection()
ns.add_task(shell)
ns.add_collection(logs_tasks)

toolset = Program(version=__version__, namespace=ns)
