print ('Hello World!')

import os
import helpers as h

if os.path.exists('tmp'):
    os.rmdir('tmp')
    print('tmp-dir removed')

os.mkdir('tmp')
print('tmp-dir created')
h.empty_line()

in1 = h.get_input('Do you want to use a filepath? [Y/n] ', valid_options=["y", "n"])

match in1:
    case "y":
        in2 = h.get_input('Please enter the filepath (at best, starting with "/" for root) ')

    case "n":
        print("OK, (To be implemented)")
