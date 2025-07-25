
import io

import pytest

from pre_commit_hooks_checker.check_no_trailing_spaces import main

#---

@pytest.mark.parametrize(
        ('content', 'expected_retval'),
        (
            ( b'foo bar laz', 0 ),
            ( b'foo bar laz\n', 0 ),
            ( b'foo bar laz\nfoo bar laz\nfoo bar laz\n', 0 ),
            ( b'foo bar laz\n\n\n\nfoo bar laz\n', 0 ),

            ( b'foo bar laz ', 1 ),
            ( b'foo bar laz    \n', 1 ),
            ( b'foo bar laz \nfoo bar laz\nfoo bar laz\n', 1 ),
            ( b'foo bar laz\n     \n\n\nfoo bar laz\n', 1 ),
            ( b'foo bar laz  ', 1 ), # Only 2 spaces
            ( b'foo bar laz  \n', 1 ), # Only 2 spaces
            ( b'foo bar laz  \nfoo bar laz\nfoo bar laz  \n', 1 ), # Only 2 spaces
            ( b'foo bar laz\n  \n\n\nfoo bar laz\n', 1 ), # Only 2 spaces

            ( b'', 0 ),
            ( b'\n\n\n\n\n', 0 ),
            ( b'\n     \n\n   \n \n', 1 ),
        ),
        )
def test_integration( content, expected_retval, tmpdir ):
    pathfile = tmpdir.join( 'file.txt' )
    pathfile.write_binary( content )

    ret = main( [str(pathfile)] )

    assert ret == expected_retval

#---

@pytest.mark.parametrize(
        ('content', 'expected_retval'),
        (
            ( b'foo bar laz  ', 0 ),
            ( b'foo bar laz  \n', 0 ),
            ( b'foo bar laz  \nfoo bar laz\nfoo bar laz  \n', 0 ),

            ( b'foo bar laz ', 1 ),
            ( b'foo bar laz   \n', 1 ),
            ( b'foo bar laz \nfoo bar laz\nfoo bar laz  \n', 1 ),
            ( b'foo bar laz\n     \n\n\nfoo bar laz\n', 1 ),
            ( b'foo bar laz\n  \n\n\nfoo bar laz\n', 1 ), # Empty line with only 2 spaces

            ( b'', 0 ),
            ( b'\n\n\n\n\n', 0 ),
            ( b'\n     \n\n   \n \n', 1 ),
            ( b'\n  \n\n  \n  \n', 1 ), # Empty line with only 2 spaces
        ),
        )
def test_integration_markdown( content, expected_retval, tmpdir ):
    pathfile = tmpdir.join( 'file.md' )
    pathfile.write_binary( content )

    ret = main( [str(pathfile)] + [ f'--markdown-linebreak-ext', '.md' ] )

    assert ret == expected_retval
