
# pre-commit hooks

## check spaces hook

Check if all whitespaces are:
- only spaces
- or only tabs

## check iddn hook

Check if all files starts with iddn/copyright comment


# DEV

## Setup
- `py -m venv .venv-dev`
- `.\.venv-dev\Scripts\activate`
- `python.exe -m pip install --upgrade pip`
- `pip install -r .\.requirements-dev.txt`

## Test with local version of hooks
- `pre-commit try-repo . check-only-spaces --verbose --all-files`
- `pre-commit try-repo . --verbose --all-files`

## Test with github version of hooks
- `pre-commit autoupdate --bleeding-edge`
- `pre-commit run --verbose --all-files`
