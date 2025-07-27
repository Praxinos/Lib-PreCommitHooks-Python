
from pathlib import Path
import pytest

from pre_commit_hooks_checker.check_iddn import main

#---

def _GetResources() -> Path:
    return Path( __file__ ).parent / 'resources'

#---

@pytest.mark.parametrize(
        ('filename', 'expected_retval'),
        (
            ( 'iddn.ok.cpp.txt', 0 ),
            ( 'iddn.ok.python.txt', 0 ),

            ( 'iddn.wrong.empty.txt', 1 ),
            ( 'iddn.wrong.only-newlines.txt', 1 ),
            ( 'iddn.wrong.second-line.txt', 1 ),
            ( 'iddn.wrong.comment.txt', 1 ),
            ( 'iddn.wrong.key-missing.txt', 1 ),
            ( 'iddn.wrong.with-prefix.txt', 1 ),
            ( 'iddn.wrong.with-postfix.txt', 1 ),
        ),
        )
def test_integration( filename, expected_retval, tmp_path ):
    reference_pathfile = _GetResources() / filename
    assert main( ( str(reference_pathfile), ) ) == expected_retval

    # Add BOM
    pathfile = tmp_path / 'file-with-bom.txt'
    content = b'\xef\xbb\xbf' + reference_pathfile.read_bytes()
    pathfile.write_bytes( content )
    assert main( ( str(pathfile), ) ) == expected_retval

    # Add shebang
    pathfile = tmp_path / 'file-with-shebang.txt'
    content = b'#!/bin/bash\n' + reference_pathfile.read_bytes()
    pathfile.write_bytes( content )
    assert main( ( str(pathfile), ) ) == expected_retval

    # Add BOM and shebang
    pathfile = tmp_path / 'file-with-bom-and-shebang.txt'
    content = b'\xef\xbb\xbf' + b'#!/bin/bash\n' + reference_pathfile.read_bytes()
    pathfile.write_bytes( content )
    assert main( ( str(pathfile), ) ) == expected_retval
