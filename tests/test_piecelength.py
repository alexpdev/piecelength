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
from piecelength import piece_length

Kb = 2**10
Mb = Kb**2
Gb = Kb**3

def test_1_4mb_minimum():
    total = Mb * 4
    result = piece_length(total)
    assert result >= 16*Kb

def test_1_4mb_maximum():
    total = Mb * 4
    result = piece_length(total)
    assert result <= 8*Mb

def test_1_4mb_pow_2():
    total = Mb * 4
    result = piece_length(total)
    assert math.log2(result) == int(math.log2(result))

def test_1_4mb():
    total = Mb * 4
    result = piece_length(total)
    assert result % (16*Kb) == 0

def test_2_50mb_minimum():
    total = Mb * 50
    result = piece_length(total)
    assert result >= 16*Kb

def test_2_50mb_maximum():
    total = Mb * 50
    result = piece_length(total)
    assert result <= 8*Mb

def test_2_50mb_pow_2():
    total = Mb * 50
    result = piece_length(total)
    assert math.log2(result) == int(math.log2(result))

def test_2_50mb():
    total = Mb * 50
    result = piece_length(total)
    assert result % (16*Kb) == 0

def test_3_130mb_minimum():
    total = Mb * 130
    result = piece_length(total)
    assert result >= 16*Kb

def test_3_130mb_maximum():
    total = Mb * 130
    result = piece_length(total)
    assert result <= 8*Mb

def test_3_130mb_pow_2():
    total = Mb * 130
    result = piece_length(total)
    assert math.log2(result) == int(math.log2(result))

def test_3_130mb():
    total = Mb * 130
    result = piece_length(total)
    assert result % (16*Kb) == 0

def test_4_150mb_minimum():
    total = Mb * 150
    result = piece_length(total)
    assert result >= 16*Kb

def test_4_150mb_maximum():
    total = Mb * 150
    result = piece_length(total)
    assert result <= 8*Mb

def test_4_150mb_pow_2():
    total = Mb * 150
    result = piece_length(total)
    assert math.log2(result) == int(math.log2(result))

def test_4_150mb():
    total = Mb * 150
    result = piece_length(total)
    assert result % (16*Kb) == 0

def test_5_256mb_minimum():
    total = Mb * 256
    result = piece_length(total)
    assert result >= 16*Kb

def test_5_256mb_maximum():
    total = Mb * 256
    result = piece_length(total)
    assert result <= 8*Mb

def test_5_256mb_pow_2():
    total = Mb * 256
    result = piece_length(total)
    assert math.log2(result) == int(math.log2(result))

def test_5_256mb():
    total = Mb * 256
    result = piece_length(total)
    assert result % (16*Kb) == 0

def test_6_350mb_minimum():
    total = Mb * 350
    result = piece_length(total)
    assert result >= 16*Kb

def test_6_350mb_maximum():
    total = Mb * 350
    result = piece_length(total)
    assert result <= 8*Mb

def test_6_350mb_pow_2():
    total = Mb * 350
    result = piece_length(total)
    assert math.log2(result) == int(math.log2(result))

def test_6_350mb():
    total = Mb * 350
    result = piece_length(total)
    assert result % (16*Kb) == 0

def test_7_485mb_minimum():
    total = Mb * 485
    result = piece_length(total)
    assert result >= 16*Kb

def test_7_485mb_maximum():
    total = Mb * 485
    result = piece_length(total)
    assert result <= 8*Mb

def test_7_485mb_pow_2():
    total = Mb * 485
    result = piece_length(total)
    assert math.log2(result) == int(math.log2(result))

def test_7_485mb():
    total = Mb * 485
    result = piece_length(total)
    assert result % (16*Kb) == 0

def test_8_512mb_minimum():
    total = Mb * 512
    result = piece_length(total)
    assert result >= 16*Kb

def test_8_512mb_maximum():
    total = Mb * 512
    result = piece_length(total)
    assert result <= 8*Mb

def test_8_512mb_pow_2():
    total = Mb * 512
    result = piece_length(total)
    assert math.log2(result) == int(math.log2(result))

def test_8_512mb():
    total = Mb * 512
    result = piece_length(total)
    assert result % (16*Kb) == 0

def test_9_720mb_minimum():
    total = Mb * 720
    result = piece_length(total)
    assert result >= 16*Kb

def test_9_720mb_maximum():
    total = Mb * 720
    result = piece_length(total)
    assert result <= 8*Mb

def test_9_720mb_pow_2():
    total = Mb * 720
    result = piece_length(total)
    assert math.log2(result) == int(math.log2(result))

def test_9_720mb():
    total = Mb * 720
    result = piece_length(total)
    assert result % (16*Kb) == 0

def test_10_1gb_minimum():
    total = Gb
    result = piece_length(total)
    assert result >= 16*Kb

def test_10_1gb_maximum():
    total = Gb
    result = piece_length(total)
    assert result <= 8*Mb

def test_10_1gb_pow_2():
    total = Gb
    result = piece_length(total)
    assert math.log2(result) == int(math.log2(result))

def test_10_1gb():
    total = Gb
    result = piece_length(total)
    assert result % (16*Kb) == 0

def test_11_1_4gb_minimum():
    total = Gb * 1.4
    result = piece_length(total)
    assert result >= 16*Kb

def test_11_1_4gb_maximum():
    total = Gb * 1.4
    result = piece_length(total)
    assert result <= 8*Mb

def test_11_1_4gb_pow_2():
    total = Gb * 1.4
    result = piece_length(total)
    assert math.log2(result) == int(math.log2(result))

def test_11_1_4gb():
    total = Gb * 1.4
    result = piece_length(total)
    assert result % (16*Kb) == 0

def test_12_2_5gb_minimum():
    total = Gb * 2.5
    result = piece_length(total)
    assert result >= 16*Kb

def test_12_2_5gb_maximum():
    total = Gb * 2.5
    result = piece_length(total)
    assert result <= 8*Mb

def test_12_2_5gb_pow_2():
    total = Gb * 2.5
    result = piece_length(total)
    assert math.log2(result) == int(math.log2(result))

def test_12_2_5gb():
    total = Gb * 2.5
    result = piece_length(total)
    assert result % (16*Kb) == 0
