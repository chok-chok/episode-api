from uuid import UUID


def validate_uuid(input, version=4):
    """
    Check if the input is valid uuid.

    Assume the uuid version 4 as default,
    Unless it's speicified in the argument.
    """
    try:
        return UUID(input).version == version
    except ValueError:
        return False
