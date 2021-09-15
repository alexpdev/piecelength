#! /usr/bin/python3
# -*- coding: utf-8 -*-

###############################################################################
# BSD 2-Clause License
#
# Copyright (c) 2021, AlexpDev
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
###############################################################################

import math

__all__ = ["get_piece_length"]

KiB = 2**10
MiB = 2**20

def get_piece_length(size):
    """
    Calculate the ideal piece length for bittorrent data.

    Piece Length is required to be a power of 2, and must be larger than 16KiB.
    Not all clients support the same max length so to be safe it is set at 8MiB.

    Args
    -----------
    size: int
        - total bits of all files incluided in .torrent file

    Returns
    -----------
    int:
        - the ideal piece length calculated from the size arguement
    """
    # Smallest supported piece length is 16KiB
    exp = 14
    # Find the largest piece size possible less than size / 10
    # 8MiB largest possible piece size
    while (2**exp)*10 < size and exp <= 23:
        exp += 1
    # piece length must be a power of 2
    return 2**exp
