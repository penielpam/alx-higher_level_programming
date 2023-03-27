#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    """Execute a function safely.
    Args:
        fct: The function to execute.
        args: Arguments for fct.
    Returns:
        if  an error occurs - None.
        Otherwise - the result of the call to fct.
    """
    try:
        r = fct(*args)
        return r
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return (None)
