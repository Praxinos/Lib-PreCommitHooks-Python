
import argparse
import json
from collections.abc import Sequence
from pathlib import Path
from typing import Any


def _raise_duplicate_keys( iOrderedPairs: list[tuple[str, Any]] ) -> dict[str, Any]:
    d = {}
    for key, val in iOrderedPairs:
        if key in d:
            raise ValueError( f'Duplicate key: {key}' )
        else:
            d[key] = val
    return d

def _get_missing_fields( iContent: dict[str,Any] ) -> list[str]:
    missing_fields = []

    if 'FileVersion' not in iContent.keys():
        missing_fields.append( 'FileVersion' )

    if 'Modules' in iContent.keys():
        for module in iContent['Modules']:
            if 'Name' not in module.keys():
                missing_fields.append( 'Modules.Name' )

    return missing_fields

def main( argv: Sequence[str] | None = None ) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument( 'filenames', nargs='*', help='Filenames to check.' )
    args = parser.parse_args( argv )

    retval = 0
    for filename in args.filenames:
        pathfile = Path( filename ).resolve()
        with pathfile.open( 'rb' ) as f:
            try:
                content = json.load( f, object_pairs_hook=_raise_duplicate_keys )
                missing_fields = _get_missing_fields( content )
                if missing_fields:
                    print( f'{filename}: missing fields: {', '.join( missing_fields )}' )
                    retval = 1

            except ValueError as exc:
                print( f'{filename}: failed to uplugin decode ({exc})' )
                retval = 1
    return retval


if __name__ == '__main__':
    raise SystemExit( main() )
