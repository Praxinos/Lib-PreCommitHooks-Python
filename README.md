
# pre-commit hooks checker
All hooks don't modify files.  
There are *read-only* checker.  

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



# DEV

## Doc :blue_book:

- https://pre-commit.com/
- https://github.com/pre-commit/pre-commit-hooks

## Tox *(for unit tests)*

### Setup
- `py -m venv .venv-dev` *(if it doesn't exist)*
- `.\.venv-dev\Scripts\activate`
- `(.venv-dev)> python.exe -m pip install --upgrade pip`
- `(.venv-dev)> pip install --upgrade -r .\.requirements-dev.txt`

### Usage
- `(.venv-dev)> tox`

To quickly test specific environment:  
*(which is one of the values in `pyproject.toml` in `envlist` attribute)*
- `(.venv-dev)> tox -e {my_specific_env}`

## Use these hooks on this repository itself

### Setup
- `py -m venv .venv-dev` *(if it doesn't exist)*
- `.\.venv-dev\Scripts\activate`
- `(.venv-dev)> python.exe -m pip install --upgrade pip`
- `(.venv-dev)> pip install --upgrade -r .\.requirements-dev.txt`

### Use this local version of hooks
- `(.venv-dev)> pre-commit try-repo . --all-files`  
*All local modifications are taken into account, but use **only** hooks defined in `.pre-commit-hooks.yaml`*

### Use the github version of hooks
- `(.venv-dev)> pre-commit clean`
- `(.venv-dev)> pre-commit run --all-files`  
*No local modifications are taken into account, but use all hooks defined in `.pre-commit-config.yaml`*
