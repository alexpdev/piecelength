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
from unittest import TestCase
from piecelength import ideal_length


class PieceLengthTest(TestCase):

    def test_4mb(self):
        bites = 4 * (2**20)
        result = ideal_length(bites)
        expected = 2**14
        pieces = math.ceil(bites/expected)
        print("size:", bites, "result:", result,
            "expected:", expected, "pieces:", pieces)
        self.assertEqual(result,expected)

    def test_50mb(self):
        bites = 50 * (2**20)
        result = ideal_length(bites)
        expected = 2**16
        pieces = math.ceil(bites/expected)
        print("size:", bites, "result:", result,
            "expected:", expected, "pieces:", pieces)
        self.assertEqual(result,expected)

    def test_130mb(self):
        bites = 130 * (2**20)
        result = ideal_length(bites)
        expected = 2**17
        pieces = math.ceil(bites/expected)
        print("size:", bites, "result:", result,
            "expected:", expected, "pieces:", pieces)
        self.assertEqual(result,expected)

    def test_350mb(self):
        bites = 350 * (2**20)
        result = ideal_length(bites)
        expected = 2**18
        pieces = math.ceil(bites/expected)
        print("size:", bites, "result:", result,
            "expected:", expected, "pieces:", pieces)
        self.assertEqual(result,expected)

    def test_700mb(self):
        bites = 700 * (2**20)
        result = ideal_length(bites)
        expected = 2**19
        pieces = math.ceil(bites/expected)
        print("size:", bites, "result:", result,
            "expected:", expected, "pieces:", pieces)
        self.assertEqual(result,expected)

    def test_1_4gb(self):
        bites = 1.4 * (2**30)
        result = ideal_length(bites)
        expected = 2**20
        pieces = math.ceil(bites/expected)
        print("size:", bites, "result:", result,
            "expected:", expected, "pieces:", pieces)
        self.assertEqual(result,expected)

    def test_2_5gb(self):
        bites = 2.5 * (2**30)
        result = ideal_length(bites)
        expected = 2**21
        pieces = math.ceil(bites/expected)
        print("size:", bites, "result:", result,
            "expected:", expected, "pieces:", pieces)
        self.assertEqual(result,expected)

    def test_4_5gb(self):
        bites = 4.5 * (2**30)
        result = ideal_length(bites)
        expected = 2**22
        pieces = math.ceil(bites/expected)
        print("size:", bites, "result:", result,
            "expected:", expected, "pieces:", pieces)
        self.assertEqual(result,expected)
