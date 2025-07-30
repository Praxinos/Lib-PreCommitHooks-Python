
# pre-commit hooks checker
All hooks don't modify files.  
They are *read-only* checkers.  

## check-utf8-wihtout-byte-order-marker hook
Check if all files are utf8 **without** BOM

## check-single-newline-end-of-file
Check if all files end with only **1** end of line

## check-no-trailing-spaces
Check if there are no trailing spaces

## check-only-spaces hook
Check if all whitespaces are spaces (no tabs)

## check-copyright hook
Check if all files starts with a valid copyright comment

## check iddn hook
Check if all files starts with a valid iddn comment

## check uplugin hook
Check if uplugin files are valid



# DEV

## Doc :blue_book:

- https://pre-commit.com/
- https://github.com/pre-commit/pre-commit-hooks

## Setup
- `py -m venv .venv-dev` *(if it doesn't exist)*
- `.\.venv-dev\Scripts\activate`
- `(.venv-dev)> python.exe -m pip install --upgrade pip`
- `(.venv-dev)> pip install --upgrade -r .\.requirements-dev.txt`
- `(.venv-dev)> pre-commit install`

## Clean

To force updating the `dev` branch of the cached repository:
- `(.venv-dev)> pre-commit clean`
- `(.venv-dev)> pre-commit run --all-files`

## Tox *(for unit tests)*

- `(.venv-dev)> tox`  
