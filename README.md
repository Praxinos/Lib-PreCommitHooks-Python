
# pre-commit hooks

## check spaces hook

Check if all whitespaces are spaces (no tabs)

## check iddn hook

Check if all files starts with iddn/copyright comment


# DEV

## Doc

https://pre-commit.com/

## Test with local version of hooks on this repository itself

### Setup
- `py -m venv .venv-dev`
- `.\.venv-dev\Scripts\activate`
- `python.exe -m pip install --upgrade pip`
- `pip install --upgrade -r .\.requirements-dev.txt`

### Testing
Use all hooks defined in `.pre-commit-hooks.yaml`:
- `pre-commit try-repo . --verbose --all-files`

or just a specific hook:
- `pre-commit try-repo . check-only-spaces --verbose --all-files`

The `.` here is to test the hooks on this repository itself.  
*(This is the only reason why there is a `venv` here to have the `pre-commit` command available)*  

## Test with local version of hooks on another repository

- `cd path/to/another/repository`
The `venv` of this another repository must have installed `pre-commit`  
- `pre-commit try-repo path/to/THIS/repository/where/there/is/.pre_commit_hooks.yaml --verbose --all-files`

## Test with github version of hooks

*(use .pre-commit-config.yaml)*
- `pre-commit clean`
- `pre-commit run --verbose --all-files`

or
- `pre-commit autoupdate`  
*(but this will lead to a new commit)*  
