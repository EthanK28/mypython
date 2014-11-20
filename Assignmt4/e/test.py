__author__ = 'Eunseok'

import sha
a = sha.new("1234").hexdigest()
b = sha.new("1234").hexdigest()

print a
print b
print a == b
