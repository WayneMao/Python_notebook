# src/sub_main.py

import sys
import os
print(os.getcwd())
sys.path.append("../")
 
print(os.getcwd())
from utils.class_utils import *

# encoder = Encoder()
# decoder = Decoder()

# print(encoder.encode('abcde'))
# print(decoder.decode('edcba'))

########## 输出 ##########
'''
edcba
abcde
'''