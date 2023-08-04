# Do not modify the code in this file
# Test for easter date

import os.path
import sys
from unittest import TestCase

from easter_date import main
from tud_test_base import *


def test_easter_date():
    try:
        exists = os.path.exists("easter_date.py")
        assert exists == True
    except:
        sys.exit()

    set_keyboard_input([2001])
    main()
    output = get_display_output()
    assert output == [
        "Enter year: ",
        "In 2001 Easter Sunday is on 4/15/2001."
    ]

