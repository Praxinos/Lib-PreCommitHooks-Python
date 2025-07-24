
# pre-commit hooks

## check spaces hook

Check if all whitespaces are:
- only spaces
- or only tabs

## check iddn hook

Check if all files starts with iddn/copyright comment


# DEV

- `py -m venv .venv-dev`
- `.\.venv-dev\Scripts\activate`
- `python.exe -m pip install --upgrade pip`
- `pip install -r .\.requirements-dev.txt`
- `pre-commit try-repo . check-only-spaces --verbose --all-files`
- `pre-commit try-repo . --verbose --all-files`
