
import argparse
from collections.abc import Sequence
import os
from pathlib import Path
from typing import IO

CRLF = b'\r\n'
LF = b'\n'
CR = b'\r'

def _check_valid( iIO: IO[bytes] ) -> bool:
    iIO.seek( 0, os.SEEK_END )
    size = iIO.tell()
    if not size:
        return True

    if size >= 4:
        iIO.seek( -4, os.SEEK_END )
        content = iIO.read( 4 )
        content = [ b.to_bytes() for b in content ]
        # If windows end of line, check before the last 2 bytes
        if content[-2] + content[-1] == CRLF:
            return content[-3] not in [ CR, LF ]

        # Otherwise, just check the 2 last bytes
        return content[-2] not in [ CR, LF ] and content[-1] in [ CR, LF ]

    iIO.seek( -size, os.SEEK_END )
    content = iIO.read( size )
    # This convert a bytes to an array of bytes to make comparaison easier
    # (Otherwise content[x] will return an integer and it is not comparable to a list of bytes)
    # content = b'foo\n'
    # ->
    # content = [ b'f', b'o', b'o', b'\n' ]
    # Now content[x] will be easily comparable to [b'\n', b'\r']
    content = [ b.to_bytes() for b in content ]

    if len( content ) == 3:
        # If windows end of line, check before the last 2 bytes
        if content[-2] + content[-1] == CRLF:
            return content[-3] not in [ CR, LF ]

        return content[-2] not in [ CR, LF ] and content[-1] in [ CR, LF ]

    if len( content ) == 2:
        # If windows end of line
        if content[-2] + content[-1] == CRLF:
            return True

        return content[-2] not in [ CR, LF ] and content[-1] in [ CR, LF ]

    if len( content ) == 1:
        return content[0] in [ CR, LF ]

    return False

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        pathfile = Path( filename ).resolve()
        # Read as binary to avoid managing encoding
        with pathfile.open( 'rb' ) as fd:
            valid = _check_valid( fd )
            if not valid:
                print( f'{pathfile}: multiple empty lines at end of file' )

                retv = 1

    return retv

if __name__ == '__main__':
    raise SystemExit(main())
