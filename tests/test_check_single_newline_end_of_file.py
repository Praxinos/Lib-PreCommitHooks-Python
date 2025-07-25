
import io

import pytest

from pre_commit_hooks_checker.check_single_newline_end_of_file import main

#---

CRLF = b'\r\n'
LF = b'\n'
CR = b'\r'

@pytest.mark.parametrize(
        ('content', 'expected_retval'),
        (
            # empty file
            ( b'', 0 ),

            # 1 byte file
            ( LF, 0 ),
            ( CR, 0 ),
            ( b'x', 1 ),

            # 2 bytes file
            ( LF + LF, 1 ),
            ( LF + CR, 1 ),
            ( LF + b'x', 1 ),

            ( CRLF, 0 ),
            ( CR + CR, 1 ),
            ( CR + b'x', 1 ),

            ( b'x' + LF, 0 ),
            ( b'x' + CR, 0 ),
            ( b'x' + b'x', 1 ),

            # 3 bytes file
            ( LF + LF + LF, 1 ),
            ( LF + LF + CR, 1 ),
            ( LF + LF + b'x', 1 ),
            ( LF + CRLF, 1 ),
            ( LF + CR + CR, 1 ),
            ( LF + CR + b'x', 1 ),
            ( LF + b'x' + LF, 0 ),
            ( LF + b'x' + CR, 0 ),
            ( LF + b'x' + b'x', 1 ),

            ( CRLF + LF, 1 ),
            ( CRLF + CR, 1 ),
            ( CRLF + b'x', 1 ),
            ( CR + CRLF, 1 ),
            ( CR + CR + CR, 1 ),
            ( CR + CR + b'x', 1 ),
            ( CR + b'x' + LF, 0 ),
            ( CR + b'x' + CR, 0 ),
            ( CR + b'x' + b'x', 1 ),

            ( b'x' + LF + LF, 1 ),
            ( b'x' + LF + CR, 1 ),
            ( b'x' + LF + b'x', 1 ),
            ( b'x' + CRLF, 0 ),
            ( b'x' + CR + CR, 1 ),
            ( b'x' + CR + b'x', 1 ),
            ( b'x' + b'x' + LF, 0 ),
            ( b'x' + b'x' + CR, 0 ),
            ( b'x' + b'x' + b'x', 1 ),

            # >=4 bytes file
            ( b'wxyz', 1 ),

            ( b'xyz' + LF + CR, 1 ),
            ( b'xyz' + CRLF, 0 ),
            ( b'xyz' + LF, 0 ),
            ( b'xyz' + CR, 0 ),

            ( b'z' + CRLF    + LF     , 1 ),
            ( b'z' + CRLF    + CR     , 1 ),
            ( b'z' + CRLF    + CRLF   , 1 ),
            ( b'z' + CRLF    + LF + CR, 1 ),
            ( b'z' + LF + CR + LF     , 1 ),
            ( b'z' + LF + CR + CR     , 1 ),
            ( b'z' + LF + CR + CRLF   , 1 ),
            ( b'z' + LF + CR + LF + CR, 1 ),

        ),
        )
def test_integration( content, expected_retval, tmpdir ):
    path = tmpdir.join( 'file.txt' )
    path.write_binary( content )

    ret = main( [str(path)] )

    assert ret == expected_retval
