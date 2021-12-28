from invoke import task


@task
def shell(ctx):
    """Python shell with asyncio support"""
    from IPython import start_ipython
    start_ipython(argv=[], extensions=['asynciomagic'])
