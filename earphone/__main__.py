import os
import sys

import usb.core
import usb.util


def main(**kwargs):
    # find sennheiser hd bt4.40 earphone
    dev = usb.core.find(idVendor=0x1395, idProduct=0xffff)

    if dev is None:
        raise ValueError('Device not found')
    else:
        print(dev)


if __name__ == '__main__':
    main(**dict(arg.replace('--', '').split('=') for arg in sys.argv[1:]))  # kwargs
