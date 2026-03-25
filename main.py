print ('Hello World!')

import os

if os.path.exists('tmp'):
    os.rmdir('tmp')
    print('tmp-dir removed')

os.mkdir('tmp')
print('tmp-dir created')