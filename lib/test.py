import sys

if sys.version_info < (3, 9):
    from .compat import BooleanOptionalAction
else:
    from argparse import BooleanOptionalAction
