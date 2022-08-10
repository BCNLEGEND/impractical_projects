"""Load a text file as a list.

Arguments:
- text file name (and directory path, if needed)

Returns:
-A list of all words in a text file in lower case.

Requires:
-Import sys
"""
import sys

def load(file):
    """Open a text file & return list of lowercase strings."""
    try:
        with open(file, encoding='utf-8') as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as error:
        print(f'{error}\n Error opening {file}. Terminating program.', file=sys.stderr)
        sys.exit(1)
        