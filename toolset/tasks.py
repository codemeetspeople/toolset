from invoke import Collection, Program

from toolset.version import __version__


from toolset.core.tasks.shell import shell

ns = Collection()
ns.add_task(shell)

toolset = Program(version=__version__, namespace=ns)
