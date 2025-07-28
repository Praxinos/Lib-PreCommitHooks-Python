
from pathlib import Path
import pytest

from pre_commit_hooks_checker.check_copyright import main

#---

def _GetResources() -> Path:
    return Path( __file__ ).parent / 'resources'

#---

@pytest.mark.parametrize(
        ('filename', 'expected_retval'),
        (
            ( 'copyright.ok.cpp.txt', 0 ),
            ( 'copyright.ok.python.txt', 0 ),
            ( 'copyright.ok.bat.txt', 0 ),
            ( 'copyright.ok.bat2.txt', 0 ),
            ( 'copyright.ok.html.txt', 0 ),

            ( 'copyright.wrong.empty.txt', 1 ),
            ( 'copyright.wrong.only-newlines.txt', 1 ),
            ( 'copyright.wrong.first-line.txt', 1 ),
            ( 'copyright.wrong.third-line.txt', 1 ),
            ( 'copyright.wrong.comment.txt', 1 ),
            ( 'copyright.wrong.comment-html.txt', 1 ),
            ( 'copyright.wrong.key-copyright-missing.txt', 1 ),
            ( 'copyright.wrong.key-c-missing.txt', 1 ),
            ( 'copyright.wrong.key-praxinos-missing.txt', 1 ),
            ( 'copyright.wrong.key-year-missing.txt', 1 ),
            ( 'copyright.wrong.with-prefix.txt', 1 ),
            ( 'copyright.wrong.with-postfix.txt', 1 ),
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
