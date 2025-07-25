
import argparse
from collections.abc import Sequence
import os
from pathlib import Path

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        pathfile = Path( filename ).resolve()

        with pathfile.open( 'r', encoding='utf-8' ) as fd:
            try:
                lines = fd.readlines()
            except UnicodeDecodeError:
                print( f'{pathfile}: not a utf8 file' )
                retv = 1

        # Read as binary to avoid managing encoding
        with pathfile.open( 'rb' ) as fd:
            bom = fd.read( 3 )
            if bom == b'\xef\xbb\xbf':
                print( f'{pathfile}: utf8 file WITH BOM' )
                retv = 2

    return retv

if __name__ == '__main__':
    raise SystemExit(main())
