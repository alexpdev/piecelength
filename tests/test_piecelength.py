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
"""Module containing all the unit tests for the piecelength package."""

import math
from piecelength import piece_length


KiB = 2**10
MiB = KiB**2
GiB = KiB**3
MAX = 16 * MiB
MIN = 16 * KiB

def test_1_4miB_minimum():
    """Test piece_length function with specific parameters."""
    total = MiB * 4
    result = piece_length(total)
    assert result >= MIN

def test_1_4miB_maximum():
    """Test piece_length function with specific parameters."""
    total = MiB * 4
    result = piece_length(total)
    assert result <= MAX

def test_1_4miB_pow_2():
    """Test piece_length function with specific parameters."""
    total = MiB * 4
    result = piece_length(total)
    assert math.log2(result) == int(math.log2(result))

def test_1_4miB():
    """Test piece_length function with specific parameters."""
    total = MiB * 4
    result = piece_length(total)
    assert result % (MIN) == 0

def test_2_50miB_minimum():
    """Test piece_length function with specific parameters."""
    total = MiB * 50
    result = piece_length(total)
    assert result >= MIN

def test_2_50miB_maximum():
    """Test piece_length function with specific parameters."""
    total = MiB * 50
    result = piece_length(total)
    assert result <= MAX

def test_2_50miB_pow_2():
    """Test piece_length function with specific parameters."""
    total = MiB * 50
    result = piece_length(total)
    assert math.log2(result) == int(math.log2(result))

def test_2_50miB():
    """Test piece_length function with specific parameters."""
    total = MiB * 50
    result = piece_length(total)
    assert result % (MIN) == 0

def test_3_130miB_minimum():
    """Test piece_length function with specific parameters."""
    total = MiB * 130
    result = piece_length(total)
    assert result >= MIN

def test_3_130miB_maximum():
    """Test piece_length function with specific parameters."""
    total = MiB * 130
    result = piece_length(total)
    assert result <= MAX

def test_3_130miB_pow_2():
    """Test piece_length function with specific parameters."""
    total = MiB * 130
    result = piece_length(total)
    assert math.log2(result) == int(math.log2(result))

def test_3_130miB():
    """Test piece_length function with specific parameters."""
    total = MiB * 130
    result = piece_length(total)
    assert result % (MIN) == 0

def test_4_150miB_minimum():
    """Test piece_length function with specific parameters."""
    total = MiB * 150
    result = piece_length(total)
    assert result >= MIN

def test_4_150miB_maximum():
    """Test piece_length function with specific parameters."""
    total = MiB * 150
    result = piece_length(total)
    assert result <= MAX

def test_4_150miB_pow_2():
    """Test piece_length function with specific parameters."""
    total = MiB * 150
    result = piece_length(total)
    assert math.log2(result) == int(math.log2(result))

def test_4_150miB():
    """Test piece_length function with specific parameters."""
    total = MiB * 150
    result = piece_length(total)
    assert result % (MIN) == 0

def test_5_256miB_minimum():
    """Test piece_length function with specific parameters."""
    total = MiB * 256
    result = piece_length(total)
    assert result >= MIN

def test_5_256miB_maximum():
    """Test piece_length function with specific parameters."""
    total = MiB * 256
    result = piece_length(total)
    assert result <= MAX

def test_5_256miB_pow_2():
    """Test piece_length function with specific parameters."""
    total = MiB * 256
    result = piece_length(total)
    assert math.log2(result) == int(math.log2(result))

def test_5_256miB():
    """Test piece_length function with specific parameters."""
    total = MiB * 256
    result = piece_length(total)
    assert result % (MIN) == 0

def test_6_350miB_minimum():
    """Test piece_length function with specific parameters."""
    total = MiB * 350
    result = piece_length(total)
    assert result >= MIN

def test_6_350miB_maximum():
    """Test piece_length function with specific parameters."""
    total = MiB * 350
    result = piece_length(total)
    assert result <= MAX

def test_6_350miB_pow_2():
    """Test piece_length function with specific parameters."""
    total = MiB * 350
    result = piece_length(total)
    assert math.log2(result) == int(math.log2(result))

def test_6_350miB():
    """Test piece_length function with specific parameters."""
    total = MiB * 350
    result = piece_length(total)
    assert result % (MIN) == 0

def test_7_485miB_minimum():
    """Test piece_length function with specific parameters."""
    total = MiB * 485
    result = piece_length(total)
    assert result >= MIN

def test_7_485miB_maximum():
    """Test piece_length function with specific parameters."""
    total = MiB * 485
    result = piece_length(total)
    assert result <= MAX

def test_7_485miB_pow_2():
    """Test piece_length function with specific parameters."""
    total = MiB * 485
    result = piece_length(total)
    assert math.log2(result) == int(math.log2(result))

def test_7_485miB():
    """Test piece_length function with specific parameters."""
    total = MiB * 485
    result = piece_length(total)
    assert result % (MIN) == 0

def test_8_512miB_minimum():
    """Test piece_length function with specific parameters."""
    total = MiB * 512
    result = piece_length(total)
    assert result >= MIN

def test_8_512miB_maximum():
    """Test piece_length function with specific parameters."""
    total = MiB * 512
    result = piece_length(total)
    assert result <= MAX

def test_8_512miB_pow_2():
    """Test piece_length function with specific parameters."""
    total = MiB * 512
    result = piece_length(total)
    assert math.log2(result) == int(math.log2(result))

def test_8_512miB():
    """Test piece_length function with specific parameters."""
    total = MiB * 512
    result = piece_length(total)
    assert result % (MIN) == 0

def test_9_720miB_minimum():
    """Test piece_length function with specific parameters."""
    total = MiB * 720
    result = piece_length(total)
    assert result >= MIN

def test_9_720miB_maximum():
    """Test piece_length function with specific parameters."""
    total = MiB * 720
    result = piece_length(total)
    assert result <= MAX

def test_9_720miB_pow_2():
    """Test piece_length function with specific parameters."""
    total = MiB * 720
    result = piece_length(total)
    assert math.log2(result) == int(math.log2(result))

def test_9_720miB():
    """Test piece_length function with specific parameters."""
    total = MiB * 720
    result = piece_length(total)
    assert result % (MIN) == 0

def test_10_1giB_minimum():
    """Test piece_length function with specific parameters."""
    total = GiB
    result = piece_length(total)
    assert result >= MIN

def test_10_1giB_maximum():
    """Test piece_length function with specific parameters."""
    total = GiB
    result = piece_length(total)
    assert result <= MAX

def test_10_1giB_pow_2():
    """Test piece_length function with specific parameters."""
    total = GiB
    result = piece_length(total)
    assert math.log2(result) == int(math.log2(result))

def test_10_1giB():
    """Test piece_length function with specific parameters."""
    total = GiB
    result = piece_length(total)
    assert result % (MIN) == 0

def test_11_1_4giB_minimum():
    """Test piece_length function with specific parameters."""
    total = GiB * 1.4
    result = piece_length(total)
    assert result >= MIN

def test_11_1_4giB_maximum():
    """Test piece_length function with specific parameters."""
    total = GiB * 1.4
    result = piece_length(total)
    assert result <= MAX

def test_11_1_4giB_pow_2():
    """Test piece_length function with specific parameters."""
    total = GiB * 1.4
    result = piece_length(total)
    assert math.log2(result) == int(math.log2(result))

def test_11_1_4giB():
    """Test piece_length function with specific parameters."""
    total = GiB * 1.4
    result = piece_length(total)
    assert result % (MIN) == 0

def test_12_2_5giB_minimum():
    """Test piece_length function with specific parameters."""
    total = GiB * 2.5
    result = piece_length(total)
    assert result >= MIN

def test_12_2_5giB_maximum():
    """Test piece_length function with specific parameters."""
    total = GiB * 2.5
    result = piece_length(total)
    assert result <= MAX

def test_12_2_5giB_pow_2():
    """Test piece_length function with specific parameters."""
    total = GiB * 2.5
    result = piece_length(total)
    assert math.log2(result) == int(math.log2(result))

def test_12_2_5giB():
    """Test piece_length function with specific parameters."""
    total = GiB * 2.5
    result = piece_length(total)
    assert result % (MIN) == 0
