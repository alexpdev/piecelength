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
import pytest
from piecelength import get_piece_length


class PieceLengthTest:

    Kb = 2**10
    Mb = Kb**2
    Gb = Kb**3

    def test_1_4mb(self):
        total = self.Mb * 4
        result = get_piece_length(total)
        pieces = total / result
        assert result >= 16*self.Kb
        assert result <= 8*self.Mb
        assert math.log2(result) == int(math.log2(result))
        assert result % (16*self.Kb) == 0
        if 16 * self.Kb != result != 8 * self.Mb:
            assert pieces >= 1000

    def test_2_50mb(self):
        total = self.Mb * 50
        result = get_piece_length(total)
        pieces = total / result
        assert result >= 16*self.Kb
        assert result <= 8*self.Mb
        assert math.log2(result) == int(math.log2(result))
        assert result % (16*self.Kb) == 0
        if 16 * self.Kb != result != 8 * self.Mb:
            assert pieces >= 1000

    def test_3_130mb(self):
        total = self.Mb * 130
        result = get_piece_length(total)
        pieces = total / result
        assert result >= 16*self.Kb
        assert result <= 8*self.Mb
        assert math.log2(result) == int(math.log2(result))
        assert result % (16*self.Kb) == 0
        if 16 * self.Kb != result != 8 * self.Mb:
            assert pieces >= 1000

    def test_4_150mb(self):
        total = self.Mb * 150
        result = get_piece_length(total)
        pieces = total / result
        assert result >= 16*self.Kb
        assert result <= 8*self.Mb
        assert math.log2(result) == int(math.log2(result))
        assert result % (16*self.Kb) == 0
        if 16 * self.Kb != result != 8 * self.Mb:
            assert pieces >= 1000

    def test_5_256mb(self):
        total = self.Mb * 256
        result = get_piece_length(total)
        pieces = total / result
        assert result >= 16*self.Kb
        assert result <= 8*self.Mb
        assert math.log2(result) == int(math.log2(result))
        assert result % (16*self.Kb) == 0
        if 16 * self.Kb != result != 8 * self.Mb:
            assert pieces >= 1000

    def test_6_350mb(self):
        total = self.Mb * 350
        result = get_piece_length(total)
        pieces = total / result
        assert result >= 16*self.Kb
        assert result <= 8*self.Mb
        assert math.log2(result) == int(math.log2(result))
        assert result % (16*self.Kb) == 0
        if 16 * self.Kb != result != 8 * self.Mb:
            assert pieces >= 1000

    def test_7_485mb(self):
        total = self.Mb * 485
        result = get_piece_length(total)
        pieces = total / result
        assert result >= 16*self.Kb
        assert result <= 8*self.Mb
        assert math.log2(result) == int(math.log2(result))
        assert result % (16*self.Kb) == 0
        if 16 * self.Kb != result != 8 * self.Mb:
            assert pieces >= 1000

    def test_8_512mb(self):
        total = self.Mb * 512
        result = get_piece_length(total)
        pieces = total / result
        assert result >= 16*self.Kb
        assert result <= 8*self.Mb
        assert math.log2(result) == int(math.log2(result))
        assert result % (16*self.Kb) == 0
        if 16 * self.Kb != result != 8 * self.Mb:
            assert pieces >= 1000

    def test_9_720mb(self):
        total = self.Mb * 720
        result = get_piece_length(total)
        pieces = total / result
        assert result >= 16*self.Kb
        assert result <= 8*self.Mb
        assert math.log2(result) == int(math.log2(result))
        assert result % (16*self.Kb) == 0
        if 16 * self.Kb != result != 8 * self.Mb:
            assert pieces >= 1000

    def test_10_1gb(self):
        total = self.Gb
        result = get_piece_length(total)
        pieces = total / result
        assert result >= 16*self.Kb
        assert result <= 8*self.Mb
        assert math.log2(result) == int(math.log2(result))
        assert result % (16*self.Kb) == 0
        if 16 * self.Kb != result != 8 * self.Mb:
            assert pieces >= 1000

    def test_11_1_4gb(self):
        total = self.Gb * 1.4
        result = get_piece_length(total)
        pieces = total / result
        assert result >= 16*self.Kb
        assert result <= 8*self.Mb
        assert math.log2(result) == int(math.log2(result))
        assert result % (16*self.Kb) == 0
        if 16 * self.Kb != result != 8 * self.Mb:
            assert pieces >= 1000

    def test_12_2_5gb(self):
        total = self.Gb * 2.5
        result = get_piece_length(total)
        pieces = total / result
        assert result >= 16*self.Kb
        assert result <= 8*self.Mb
        assert math.log2(result) == int(math.log2(result))
        assert result % (16*self.Kb) == 0
        if 16 * self.Kb != result != 8 * self.Mb:
            assert pieces >= 1000
