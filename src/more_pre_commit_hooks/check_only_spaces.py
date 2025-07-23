
import argparse
from collections.abc import Sequence
from pathlib import Path

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        pathfile = Path( filename ).resolve()
        # Read as binary to avoid managing encoding
        with pathfile.open( 'rb' ) as f:
            lines = f.readlines()

            error_in_line=b''
            error_in_noline=-1
            for i, line in enumerate( lines ):
                if b'\t' in line:
                    error_in_noline = i + 1
                    error_in_line = line

            if error_in_noline >= 0:
                print( f'{pathfile}:' )
                print( f'line #{error_in_noline}: {error_in_line}' )

                retv = 1

    return retv

if __name__ == '__main__':
    raise SystemExit(main())
