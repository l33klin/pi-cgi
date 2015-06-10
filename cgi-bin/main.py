#!/usr/bin/env python
import cgi,cgitb
from res import *

print start_response()
print start_div("center", "margin-top:40px;")
print img("../views/test.jpg")
print end_div()

print start_div("center", "margin-top:60px;")
print input_label("Num1", "adder-1")
print "+"
print input_label("Num2", "adder-2")
print end_div()

