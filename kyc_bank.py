import sys
from lib import kyc

ifsc = sys.argv[1]
bacc = sys.argv[2]

kyc.verify_bank(ifsc,bacc)

