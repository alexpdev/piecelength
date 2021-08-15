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
import piecelength

get_piece_length = piecelength.get_piece_length

Kb = 2**10
Mb = Kb**2
Gb = Kb**3


def test_1_4mb():
    total = Mb * 4
    result = get_piece_length(total)
    pieces = total / result
    assert result >= 16*Kb
    assert result <= 8*Mb
    assert math.log2(result) == int(math.log2(result))
    assert result % (16*Kb) == 0
    if 16 * Kb != result != 8 * Mb:
        assert pieces >= 1000

def test_2_50mb():
    total = Mb * 50
    result = get_piece_length(total)
    pieces = total / result
    assert result >= 16*Kb
    assert result <= 8*Mb
    assert math.log2(result) == int(math.log2(result))
    assert result % (16*Kb) == 0
    if 16 * Kb != result != 8 * Mb:
        assert pieces >= 1000

def test_3_130mb():
    total = Mb * 130
    result = get_piece_length(total)
    pieces = total / result
    assert result >= 16*Kb
    assert result <= 8*Mb
    assert math.log2(result) == int(math.log2(result))
    assert result % (16*Kb) == 0
    if 16 * Kb != result != 8 * Mb:
        assert pieces >= 1000

def test_4_150mb():
    total = Mb * 150
    result = get_piece_length(total)
    pieces = total / result
    assert result >= 16*Kb
    assert result <= 8*Mb
    assert math.log2(result) == int(math.log2(result))
    assert result % (16*Kb) == 0
    if 16 * Kb != result != 8 * Mb:
        assert pieces >= 1000

def test_5_256mb():
    total = Mb * 256
    result = get_piece_length(total)
    pieces = total / result
    assert result >= 16*Kb
    assert result <= 8*Mb
    assert math.log2(result) == int(math.log2(result))
    assert result % (16*Kb) == 0
    if 16 * Kb != result != 8 * Mb:
        assert pieces >= 1000

def test_6_350mb():
    total = Mb * 350
    result = get_piece_length(total)
    pieces = total / result
    assert result >= 16*Kb
    assert result <= 8*Mb
    assert math.log2(result) == int(math.log2(result))
    assert result % (16*Kb) == 0
    if 16 * Kb != result != 8 * Mb:
        assert pieces >= 1000

def test_7_485mb():
    total = Mb * 485
    result = get_piece_length(total)
    pieces = total / result
    assert result >= 16*Kb
    assert result <= 8*Mb
    assert math.log2(result) == int(math.log2(result))
    assert result % (16*Kb) == 0
    if 16 * Kb != result != 8 * Mb:
        assert pieces >= 1000

def test_8_512mb():
    total = Mb * 512
    result = get_piece_length(total)
    pieces = total / result
    assert result >= 16*Kb
    assert result <= 8*Mb
    assert math.log2(result) == int(math.log2(result))
    assert result % (16*Kb) == 0
    if 16 * Kb != result != 8 * Mb:
        assert pieces >= 1000

def test_9_720mb():
    total = Mb * 720
    result = get_piece_length(total)
    pieces = total / result
    assert result >= 16*Kb
    assert result <= 8*Mb
    assert math.log2(result) == int(math.log2(result))
    assert result % (16*Kb) == 0
    if 16 * Kb != result != 8 * Mb:
        assert pieces >= 1000

def test_10_1gb():
    total = Gb
    result = get_piece_length(total)
    pieces = total / result
    assert result >= 16*Kb
    assert result <= 8*Mb
    assert math.log2(result) == int(math.log2(result))
    assert result % (16*Kb) == 0
    if 16 * Kb != result != 8 * Mb:
        assert pieces >= 1000

def test_11_1_4gb():
    total = Gb * 1.4
    result = get_piece_length(total)
    pieces = total / result
    assert result >= 16*Kb
    assert result <= 8*Mb
    assert math.log2(result) == int(math.log2(result))
    assert result % (16*Kb) == 0
    if 16 * Kb != result != 8 * Mb:
        assert pieces >= 1000

def test_12_2_5gb():
    total = Gb * 2.5
    result = get_piece_length(total)
    pieces = total / result
    assert result >= 16*Kb
    assert result <= 8*Mb
    assert math.log2(result) == int(math.log2(result))
    assert result % (16*Kb) == 0
    if 16 * Kb != result != 8 * Mb:
        assert pieces >= 1000
