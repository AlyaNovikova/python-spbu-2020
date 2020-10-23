from functools import wraps


class ContractError(Exception):
    """We use this error when someone breaks our contract."""


#: Special value, that indicates that validation for this type is not required.
Any = object()


def check_arg_types(args, arg_types):
    """
    Checks if the types of the arguments from args match the types from arg_types.

    :param args: tuple of arguments to check for types
    :param arg_types: required argument types
    :raises ContractError: if the argument types are not valid
    """
    if len(args) != len(arg_types):
        raise ContractError('Incorrect number of arguments')

    for arg, arg_type in zip(args, arg_types):
        if arg_type is Any:
            continue
        if not isinstance(arg, arg_type):
            raise ContractError('Argument "{0}" does not match with type {1}'.format(arg, arg_type))


def check_function_raises(function, raises, *args, **kwargs):
    """
    Checks that the function raises only valid errors on the given arguments.

    :param function: the function we are checking for valid exceptions
    :param raises: Allowable exceptions that can be thrown from function
    :param args: args to be passed to the function
    :param kwargs: kwargs to be passed to the function
    :return: return value of the function on the passed arguments

    :raises ContractError: in case the function tries to raise an invalid exception
    :raises Exception: function exceptions, if their type is valid
    """
    if raises is None or Any in raises:
        return function(*args, **kwargs)

    try:
        return_value = function(*args, **kwargs)
    except Exception as error:
        if isinstance(error, raises):
            raise error
        raise ContractError('Exception type "{0}" cannot be raised'.format(error)) from error

    return return_value


def contract(arg_types=None, return_type=None, raises=None):  # noqa: WPS231
    """
    Creates a function decorator.

    Decorator checks the types of arguments, return type and the types of exceptions in functions

    :param arg_types: the types of allowed parameters. If None, then any types are allowed
    :param return_type: the type of a valid return value. If None, then any type is allowed
    :param raises: types of allowed function exceptions. If None, then any types are allowed
    :return: function decorator

    :raises ContractError: if the function does not match the given signature
    """
    def decorator(function):  # noqa: WPS231
        @wraps(function)
        def wrapper(*args, **kwargs):  # noqa: WPS430
            if arg_types is not None:
                check_arg_types(args, arg_types)

            return_value = check_function_raises(function, raises, *args, **kwargs)

            if return_type is not None:
                if return_type is not Any and not isinstance(return_value, return_type):
                    raise ContractError('Return value does not match with return type')
            return return_value

        return wrapper
    return decorator
