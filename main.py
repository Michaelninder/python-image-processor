print ('Hello World!')

import os
import helpers as h

if os.path.exists('tmp'):
    os.rmdir('tmp')
    print('tmp-dir removed')

os.mkdir('tmp')
print('tmp-dir created')
h.empty_line()

in1 = input("Do you want to use a filepath? [Y/n]")

match in1.lower():
    case "y":
        pass
    case "n":
        print ("OK, (To be implemented)")
    case _:
        print ("Re-input (to be implemented)")