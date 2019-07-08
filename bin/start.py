#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys

# from core import main

base_url = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_url)
sys.path.append(base_url)

from core import main

if __name__ == '__main__':
    main.run()

