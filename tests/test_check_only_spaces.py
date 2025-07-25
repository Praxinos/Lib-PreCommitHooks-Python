
import io

import pytest

from more_pre_commit_hooks.check_only_spaces import main

#---

@pytest.mark.parametrize(
        ('content', 'expected_retval'),
        (
            ( b'foo bar laz', 0 ),
            ( b'foo bar   laz', 0 ),
            ( b'foo bar\tlaz', 1 ),
            ( b'foo\tbar\tlaz', 1 ),
        ),
        )
def test_integration( content, expected_retval, tmpdir ):
    path = tmpdir.join( 'file.txt' )
    path.write_binary( content )

    ret = main( [str(path)] )

    assert ret == expected_retval
