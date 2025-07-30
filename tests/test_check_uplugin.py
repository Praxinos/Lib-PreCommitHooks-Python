
from pathlib import Path
import pytest

from pre_commit_hooks_checker.check_uplugin import main

#---

def _GetResources() -> Path:
    return Path( __file__ ).parent / 'resources'

#---

@pytest.mark.parametrize(
    ( 'filename', 'expected_retval' ),
    (
        ( 'uplugin.ok.uplugin', 0 ),
        ( 'uplugin.wrong.not-valid-json.uplugin', 1 ),
        ( 'uplugin.wrong.not-valid-missing-field-fileversion.uplugin', 1 ),
        ( 'uplugin.wrong.not-valid-missing-field-module-name.uplugin', 1 ),
        ( 'uplugin.wrong.ansi.uplugin', 1 ),
        ( 'uplugin.wrong.duplicated-keys.uplugin', 1 ),
    ),
)
def test_main( capsys, filename, expected_retval ):
    reference_pathfile = _GetResources() / filename
    ret = main( [str(reference_pathfile)] )
    assert ret == expected_retval
    if expected_retval == 1:
        stdout, _ = capsys.readouterr()
        assert filename in stdout


def test_non_utf8_file( tmp_path ):
    f = tmp_path / 'file.uplugin'
    f.write_bytes( b'\xa9\xfe\x12' )
    assert main( [str(f)] )
