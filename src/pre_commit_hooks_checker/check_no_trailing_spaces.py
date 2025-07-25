
import argparse
from collections.abc import Sequence
import os
from pathlib import Path

# Mainly inspired by the original: https://github.com/pre-commit/pre-commit-hooks/blob/main/pre_commit_hooks/trailing_whitespace_fixer.py

def _process_line( iLine: bytes, iIsMarkdown: bool ) -> bytes:
    if iLine[-2:] == b'\r\n':
        eol = b'\r\n'
        iLine = iLine[:-2]
    elif iLine[-1:] == b'\n':
        eol = b'\n'
        iLine = iLine[:-1]
    else:
        eol = b''

    # preserve trailing two-space for non-blank lines in markdown files
    if iIsMarkdown and ( not iLine.isspace() ) and iLine.endswith( b'  ' ):
        return iLine[:-2].rstrip() + b'  ' + eol

    return iLine.rstrip() + eol


def _check_valid( iPathfile: Path, iIsMarkdown: bool ) -> list[tuple[int, bytes]]:
    with iPathfile.open( 'rb' ) as fd:
        lines = fd.readlines()

    wrong_lines = []
    for no_line, line in enumerate( lines ):
        newline = _process_line( line, iIsMarkdown )
        if newline != line:
            wrong_lines.append( ( no_line, line ) )

    return wrong_lines


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--markdown-linebreak-ext',
        action='append',
        default=[],
        metavar='*|EXT[,EXT,...]',
        help=(
            'Markdown extensions (or *) to not strip linebreak spaces.  '
            'default: %(default)s'
        ),
    )
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    md_args = args.markdown_linebreak_ext
    if '' in md_args:
        parser.error('--markdown-linebreak-ext requires a non-empty argument')
    all_markdown = '*' in md_args
    # normalize extensions; split at ',', lowercase, and force 1 leading '.'
    md_exts = [
        '.' + x.lower().lstrip('.') for x in ','.join(md_args).split(',')
    ]

    # reject probable "eaten" filename as extension: skip leading '.' with [1:]
    for ext in md_exts:
        if any(c in ext[1:] for c in r'./\:'):
            parser.error(
                f'bad --markdown-linebreak-ext extension '
                f'{ext!r} (has . / \\ :)\n'
                f"  (probably filename; use '--markdown-linebreak-ext=EXT')",
            )

    #-

    return_code = 0
    for filename in args.filenames:
        pathfile = Path( filename )
        extension = pathfile.suffix.lower()

        md = all_markdown or extension in md_exts
        wrong_lines = _check_valid( pathfile, md )
        if wrong_lines:
            print( f'{pathfile}: ' )
            for no_line, line in wrong_lines:
                print( f'line #{no_line}: "{line}"' )
            return_code = 1

    return return_code


if __name__ == '__main__':
    raise SystemExit(main())
