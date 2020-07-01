# main.py

from utils.utils import get_sum
from utils.class_utils import Encoder,Decoder
from src import sub_main

print(get_sum(1, 2))

encoder = Encoder()
decoder = Decoder()

print(encoder.encode('abcde'))
print(decoder.decode('edcba'))

