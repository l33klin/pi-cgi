#!/usr/bin/env python
import cgi,cgitb
from res import *

print start_response()
print start_div("center", "margin-top:40px;")
print img("../views/test.jpg")
print end_div()