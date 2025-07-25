
from pathlib import Path
import pytest

from pre_commit_hooks_checker.check_utf8_wihtout_byte_order_marker import main

def _GetResources() -> Path:
    return Path( __file__ ).parent / 'resources'

#---

@pytest.mark.parametrize(
        ('filename', 'expected_retval'),
        (
            ( 'text.utf8.txt', 0 ),
            ( 'text.utf8-with-bom.txt', 2 ),
            ( 'text.windows-1252.ansi.txt', 1 ),
            ( 'text.windows-932.japanese.txt', 1 ),
        ),
        )
def test_integration( filename, expected_retval ):
    f = _GetResources() / filename
    assert main( ( str(f), ) ) == expected_retval
