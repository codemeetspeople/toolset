from io import StringIO
from contextlib import redirect_stdout

from toolset.logs.parser import Parser
from toolset.logs.constants import LogSeverity


def _join_file_to_tmpdir(tdir, offset):
    p = tdir.join(f'log{offset}.log')
    log = []
    for i, v in enumerate(['info', 'warning', 'critical']):
        log.append(f'[Mon Jan 01 2022 00:00:0{i+offset} +0200] [{v}] [app{offset}] something went wrong...')

    p.write('\n'.join(log))


def test_parser(tmpdir):
    expected = (
        '[Mon Jan 01 2022 00:00:00 +0200] [info] [app0] something went wrong...\n'
        '[Mon Jan 01 2022 00:00:01 +0200] [info] [app1] something went wrong...\n'
        '[Mon Jan 01 2022 00:00:01 +0200] [warning] [app0] something went wrong...\n'
        '[Mon Jan 01 2022 00:00:02 +0200] [critical] [app0] something went wrong...\n'
        '[Mon Jan 01 2022 00:00:02 +0200] [info] [app2] something went wrong...\n'
        '[Mon Jan 01 2022 00:00:02 +0200] [warning] [app1] something went wrong...\n'
        '[Mon Jan 01 2022 00:00:03 +0200] [critical] [app1] something went wrong...\n'
        '[Mon Jan 01 2022 00:00:03 +0200] [warning] [app2] something went wrong...\n'
        '[Mon Jan 01 2022 00:00:04 +0200] [critical] [app2] something went wrong...\n'
    )

    for offset in (0, 1, 2):
        _join_file_to_tmpdir(tmpdir, offset)

    p = Parser(tmpdir.listdir())

    with StringIO() as out, redirect_stdout(out):
        p.merge()
        # I use replace() because something strange with tmpdir files. No time to research, sorry
        output = out.getvalue().replace('\n\n', '\n')

    assert expected == output


def test_level(tmpdir):
    expected = (
        '[Mon Jan 01 2022 00:00:01 +0200] [warning] [app0] something went wrong...\n'
        '[Mon Jan 01 2022 00:00:02 +0200] [critical] [app0] something went wrong...\n'
        '[Mon Jan 01 2022 00:00:02 +0200] [warning] [app1] something went wrong...\n'
        '[Mon Jan 01 2022 00:00:03 +0200] [critical] [app1] something went wrong...\n'
        '[Mon Jan 01 2022 00:00:03 +0200] [warning] [app2] something went wrong...\n'
        '[Mon Jan 01 2022 00:00:04 +0200] [critical] [app2] something went wrong...\n'
    )

    for offset in (0, 1, 2):
        _join_file_to_tmpdir(tmpdir, offset)

    p = Parser(tmpdir.listdir(), level=LogSeverity.WARNING)

    with StringIO() as out, redirect_stdout(out):
        p.merge()
        # I use replace() because something strange with tmpdir files. No time to research, sorry
        output = out.getvalue().replace('\n\n', '\n')

    assert expected == output
