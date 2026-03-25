print ('Hello World!')

import os
from PIL import Image
import helpers as h
import shutil

if os.path.exists('tmp'):
    #os.rmdir('tmp')
    shutil.rmtree('tmp')
    print('tmp-dir removed')

os.mkdir('tmp')
print('tmp-dir created')
h.empty_line()

in1 = h.get_input('Do you want to use a filepath? [Y/n] ', valid_options=["y", "n"])

match in1:
    case "y":
        filepath = h.trim_quotes(h.get_input('Please enter the filepath (at best, starting with "/" for root): '))
        
        try:
            img = Image.open(filepath)
            print(f"Image loaded: {img.format} - Size: {img.size} - Ratio: {h.calc_ratio(img.width, img.height)}")
            
            filename = os.path.basename(filepath)
            tmp_path = os.path.join('tmp', filename)
            img.save(tmp_path)
            print(f"Image saved to: {tmp_path}")
            
        except FileNotFoundError:
            print(f"Error: File '{filepath}' not found")
        except Exception as e:
            print(f"Error loading image: {e}")
    
    case "n":
        print("OK, (To be implemented)")