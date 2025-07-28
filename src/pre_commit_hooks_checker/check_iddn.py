
import argparse
from collections.abc import Sequence
import os
from pathlib import Path
import re

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        pathfile = Path( filename ).resolve()

        # Read as binary to avoid managing encoding
        with pathfile.open( 'rb' ) as fd:
            # Test a potential BOM flag
            bom = fd.read( 3 )
            if bom != b'\xef\xbb\xbf':
                # If no BOM, return to the start
                fd.seek( 0, os.SEEK_SET )

            # Read the first line
            line = fd.readline()
            # If it is a shebang, read the next line (and considering this next line as the first one)
            if line.startswith( b'#!' ):
                line = fd.readline()

            # IDDN must be on the first line
            line = line.rstrip( b'\r\n' ) # remove end of line

            iddn_pattern = rb'IDDN' + rb'[.]FR' + rb'[.]\d{3,}' + rb'[.]\d{6,}' + rb'[.]\d{3,}' + rb'[.][RDSCX]' + rb'[.][PCAX]' + rb'[.]\d{4}' + rb'[.]\d{3,}' + rb'[.]\d{5,}'
            pattern_single = re.compile( rb'^(//|#|;|@[Rr][Ee][Mm]) ' + iddn_pattern + rb'$' )
            pattern_multiple = re.compile( rb'^(<!--) ' + iddn_pattern + rb' (-->)$' )

            match_single = re.match( pattern_single, line )
            match_multiple = re.match( pattern_multiple, line )
            if not match_single and not match_multiple:
                print( f'{pathfile}: doesn\'t contain a valid iddn' )
                retv = 1

    return retv

if __name__ == '__main__':
    raise SystemExit(main())
