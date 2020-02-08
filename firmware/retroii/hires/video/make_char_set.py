# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Commodore 64 Character Bitmap Generator
#
# Author:  Mike Christle
# Version: 1.0
# Copyright (c) 2018
#
# Writes SPIN byte statements to the file char_set.txt.
#
# History:
# 1.0   - Original release - 10/10/2018.
#---------------------------------------------------------------------------
#┌──────────────────────────────────────────────────────────────────────────┐
#│                       TERMS OF USE: MIT License                          │                                                            
#├──────────────────────────────────────────────────────────────────────────┤
#│Permission is hereby granted, free of charge, to any person obtaining a   │
#│copy of this software and associated documentation files (the "Software"),│
#│to deal in the Software without restriction, including without limitation │
#│the rights to use, copy, modify, merge, publish, distribute, sublicense,  │
#│and/or sell copies of the Software, and to permit persons to whom the     │
#│Software is furnished to do so, subject to the following conditions:      │                                                           │
#│                                                                          │                                                  │
#│The above copyright notice and this permission notice shall be included in│
#│all copies or substantial portions of the Software.                       │
#│                                                                          │                                                  │
#│THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR│
#│IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  │
#│FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL   │
#│THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER│
#│LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING   │
#│FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER       │
#│DEALINGS IN THE SOFTWARE.                                                 │
#└──────────────────────────────────────────────────────────────────────────┘

bitmap = (
	(  "32 Space",
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000),
	(  "33 !",
	0b00000000,
	0b00001000,
	0b00001000,
	0b00001000,
	0b00001000,
	0b00001000,
	0b00000000,
	0b00001000),
	(  "34 \"",
	0b00000000,
	0b00010100,
	0b00010100,
	0b00010100,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000),
	(  "35 #",
	0b00000000,
	0b00010100,
	0b00010100,
	0b00111110,
	0b00010100,
	0b00111110,
	0b00010100,
	0b00010100),
	(  "36 $",
	0b00000000,
	0b00001000,
	0b00011110,
	0b00101000,
	0b00011100,
	0b00001010,
	0b00111100,
	0b00001000),
	(  "37 %",
	0b00000000,
	0b00110000,
	0b00110010,
	0b00000100,
	0b00001000,
	0b00010000,
	0b00100110,
	0b00000110),
	(  "38 &",
	0b00000000,
	0b00010000,
	0b00101000,
	0b00101000,
	0b00010000,
	0b00101010,
	0b00100100,
	0b00011010),
	(  "39 '",
	0b00000000,
	0b00001000,
	0b00001000,
	0b00001000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000),
	(  "40 (",
	0b00000000,
	0b00000100,
	0b00001000,
	0b00010000,
	0b00010000,
	0b00010000,
	0b00001000,
	0b00000100),
	(  "41 )",
	0b00000000,
	0b00010000,
	0b00001000,
	0b00000100,
	0b00000100,
	0b00000100,
	0b00001000,
	0b00010000),
	(  "42 *",
	0b00000000,
	0b00001000,
	0b00101010,
	0b00011100,
	0b00001000,
	0b00011100,
	0b00101010,
	0b00001000),
	(  "43 +",
	0b00000000,
	0b00000000,
	0b00001000,
	0b00001000,
	0b00111110,
	0b00001000,
	0b00001000,
	0b00000000),
	(  "44 ,",
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00001000,
	0b00001000,
	0b00010000),
	(  "45 -",
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00111110,
	0b00000000,
	0b00000000,
	0b00000000),
	(  "46 .",
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00001000,
	0b00000000),
	(  "47 /",
	0b00000000,
	0b00000000,
	0b00000010,
	0b00000100,
	0b00001000,
	0b00010000,
	0b00100000,
	0b00000000),
	(  "48 0",
	0b00000000,
	0b00011100,
	0b00100010,
	0b00100110,
	0b00101010,
	0b00110010,
	0b00100010,
	0b00011100),
	(  "49 1",
	0b00000000,
	0b00001000,
	0b00011000,
	0b00001000,
	0b00001000,
	0b00001000,
	0b00001000,
	0b00011100),
	(  "50 2",
	0b00000000,
	0b00011100,
	0b00100010,
	0b00000010,
	0b00001100,
	0b00010000,
	0b00100000,
	0b00111110),
	(  "51 3",
	0b00000000,
	0b00111110,
	0b00000010,
	0b00000100,
	0b00001100,
	0b00000010,
	0b00100010,
	0b00011100),
	(  "52 4",
	0b00000000,
	0b00000100,
	0b00001100,
	0b00010100,
	0b00100100,
	0b00111110,
	0b00000100,
	0b00000100),
	(  "53 5",
	0b00000000,
	0b00111110,
	0b00100000,
	0b00111100,
	0b00000010,
	0b00000010,
	0b00100010,
	0b00011100),
	(  "54 6",
	0b00000000,
	0b00001110,
	0b00010000,
	0b00100000,
	0b00111100,
	0b00100010,
	0b00100010,
	0b00011100),
	(  "55 7",
	0b00000000,
	0b00111110,
	0b00000010,
	0b00000100,
	0b00001000,
	0b00010000,
	0b00010000,
	0b00010000),
	(  "56 8",
	0b00000000,
	0b00011100,
	0b00100010,
	0b00100010,
	0b00011100,
	0b00100010,
	0b00100010,
	0b00011100),
	(  "57 9",
	0b00000000,
	0b00011100,
	0b00100010,
	0b00100010,
	0b00011110,
	0b00000010,
	0b00000100,
	0b00111000),
	(  "58 :",
	0b00000000,
	0b00000000,
	0b00000000,
	0b00001000,
	0b00000000,
	0b00001000,
	0b00000000,
	0b00000000),
	(  "59 ;",
	0b00000000,
	0b00000000,
	0b00000000,
	0b00001000,
	0b00000000,
	0b00001000,
	0b00001000,
	0b00010000),
	(  "60 <",
	0b00000000,
	0b00000010,
	0b00000100,
	0b00001000,
	0b00010000,
	0b00001000,
	0b00000100,
	0b00000010),
	(  "61 =",
	0b00000000,
	0b00000000,
	0b00000000,
	0b00111110,
	0b00000000,
	0b00111110,
	0b00000000,
	0b00000000),
	(  "62 >",
	0b00000000,
	0b00100000,
	0b00010000,
	0b00001000,
	0b00000100,
	0b00001000,
	0b00010000,
	0b00100000),
	(  "63 ?",
	0b00000000,
	0b00011100,
	0b00100010,
	0b00000100,
	0b00001000,
	0b00001000,
	0b00000000,
	0b00001000),
	(  "64 @",
	0b00000000,
	0b00011100,
	0b00100010,
	0b00101010,
	0b00101110,
	0b00101100,
	0b00100000,
	0b00011110),
	(  "65 A",
	0b00000000,
	0b00001000,
	0b00010100,
	0b00100010,
	0b00100010,
	0b00111110,
	0b00100010,
	0b00100010),
	(  "66 B",
	0b00000000,
	0b00111100,
	0b00100010,
	0b00100010,
	0b00111100,
	0b00100010,
	0b00100010,
	0b00111100),
	(  "67 C",
	0b00000000,
	0b00011100,
	0b00100010,
	0b00100000,
	0b00100000,
	0b00100000,
	0b00100010,
	0b00011100),
	(  "68 D",
	0b00000000,
	0b00111100,
	0b00100010,
	0b00100010,
	0b00100010,
	0b00100010,
	0b00100010,
	0b00111100),
	(  "69 E",
	0b00000000,
	0b00111110,
	0b00100000,
	0b00100000,
	0b00111100,
	0b00100000,
	0b00100000,
	0b00111110),
	(  "70 F",
	0b00000000,
	0b00111110,
	0b00100000,
	0b00100000,
	0b00111100,
	0b00100000,
	0b00100000,
	0b00100000),
	(  "71 G",
	0b00000000,
	0b00011110,
	0b00100000,
	0b00100000,
	0b00100000,
	0b00100110,
	0b00100010,
	0b00011110),
	(  "72 H",
	0b00000000,
	0b00100010,
	0b00100010,
	0b00100010,
	0b00111110,
	0b00100010,
	0b00100010,
	0b00100010),
	(  "73 I",
	0b00000000,
	0b00011100,
	0b00001000,
	0b00001000,
	0b00001000,
	0b00001000,
	0b00001000,
	0b00011100),
	(  "74 J",
	0b00000000,
	0b00000010,
	0b00000010,
	0b00000010,
	0b00000010,
	0b00000010,
	0b00100010,
	0b00011100),
	(  "75 K",
	0b00000000,
	0b00100010,
	0b00100100,
	0b00101000,
	0b00110000,
	0b00101000,
	0b00100100,
	0b00100010),
	(  "76 L",
	0b00000000,
	0b00100000,
	0b00100000,
	0b00100000,
	0b00100000,
	0b00100000,
	0b00100000,
	0b00111110),
	(  "77 M",
	0b00000000,
	0b00100010,
	0b00110110,
	0b00101010,
	0b00101010,
	0b00100010,
	0b00100010,
	0b00100010),
	(  "78 N",
	0b00000000,
	0b00100010,
	0b00100010,
	0b00110010,
	0b00101010,
	0b00100110,
	0b00100010,
	0b00100010),
	(  "79 O",
	0b00000000,
	0b00011100,
	0b00100010,
	0b00100010,
	0b00100010,
	0b00100010,
	0b00100010,
	0b00011100),
	(  "80 P",
	0b00000000,
	0b00111100,
	0b00100010,
	0b00100010,
	0b00111100,
	0b00100000,
	0b00100000,
	0b00100000),
	(  "81 Q",
	0b00000000,
	0b00011100,
	0b00100010,
	0b00100010,
	0b00100010,
	0b00101010,
	0b00100100,
	0b00011010),
	(  "82 R",
	0b00000000,
	0b00111100,
	0b00100010,
	0b00100010,
	0b00111100,
	0b00101000,
	0b00100100,
	0b00100010),
	(  "83 S",
	0b00000000,
	0b00011100,
	0b00100010,
	0b00100000,
	0b00011100,
	0b00000010,
	0b00100010,
	0b00011100),
	(  "84 T",
	0b00000000,
	0b00111110,
	0b00001000,
	0b00001000,
	0b00001000,
	0b00001000,
	0b00001000,
	0b00001000),
	(  "85 U",
	0b00000000,
	0b00100010,
	0b00100010,
	0b00100010,
	0b00100010,
	0b00100010,
	0b00100010,
	0b00011100),
	(  "86 V",
	0b00000000,
	0b00100010,
	0b00100010,
	0b00100010,
	0b00100010,
	0b00100010,
	0b00010100,
	0b00001000),
	(  "87 W",
	0b00000000,
	0b00100010,
	0b00100010,
	0b00100010,
	0b00101010,
	0b00101010,
	0b00110110,
	0b00100010),
	(  "88 X",
	0b00000000,
	0b00100010,
	0b00100010,
	0b00010100,
	0b00001000,
	0b00010100,
	0b00100010,
	0b00100010),
	(  "89 Y",
	0b00000000,
	0b00100010,
	0b00100010,
	0b00010100,
	0b00001000,
	0b00001000,
	0b00001000,
	0b00001000),
	(  "90 Z",
	0b00000000,
	0b00111110,
	0b00000010,
	0b00000100,
	0b00001000,
	0b00010000,
	0b00100000,
	0b00111110),
	(  "91 [",
	0b00000000,
	0b00111110,
	0b00110000,
	0b00110000,
	0b00110000,
	0b00110000,
	0b00110000,
	0b00111110),
	(  "92 \\",
	0b00000000,
	0b00000000,
	0b00100000,
	0b00010000,
	0b00001000,
	0b00000100,
	0b00000010,
	0b00000000),
	(  "93 ]",
	0b00000000,
	0b00111110,
	0b00000110,
	0b00000110,
	0b00000110,
	0b00000110,
	0b00000110,
	0b00111110),
	(  "94 ^",
	0b00000000,
	0b00001000,
	0b00010100,
	0b00100010,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000),
	(  "95 _",
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b01111111),
	(  "96 `",
	0b00000000,
	0b00010000,
	0b00001000,
	0b00000100,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000),
	(  "97 a",
	0b00000000,
	0b00000000,
	0b00111100,
	0b00000110,
	0b00111110,
	0b01100110,
	0b00111110,
	0b00000000),
	(  "98 b",
	0b00000000,
	0b01100000,
	0b01100000,
	0b01111100,
	0b01100110,
	0b01100110,
	0b01111100,
	0b00000000),
	(  "99 c",
	0b00000000,
	0b00000000,
	0b00111100,
	0b01100000,
	0b01100000,
	0b01100000,
	0b00111100,
	0b00000000),
	(  "100 d",
	0b00000000,
	0b00000110,
	0b00000110,
	0b00111110,
	0b01100110,
	0b01100110,
	0b00111110,
	0b00000000),
	(  "101 e",
	0b00000000,
	0b00000000,
	0b00111100,
	0b01100110,
	0b01111110,
	0b01100000,
	0b00111100,
	0b00000000),
	(  "102 f",
	0b00000000,
	0b00001110,
	0b00011000,
	0b00111110,
	0b00011000,
	0b00011000,
	0b00011000,
	0b00000000),
	(  "103 g",
	0b00000000,
	0b00000000,
	0b00111110,
	0b01100110,
	0b01100110,
	0b00111110,
	0b00000110,
	0b01111100),
	(  "104 h",
	0b00000000,
	0b01100000,
	0b01100000,
	0b01111100,
	0b01100110,
	0b01100110,
	0b01100110,
	0b00000000),
	(  "105 i",
	0b00000000,
	0b00011000,
	0b00000000,
	0b00111000,
	0b00011000,
	0b00011000,
	0b00111100,
	0b00000000),
	(  "106 j",
	0b00000000,
	0b00000110,
	0b00000000,
	0b00000110,
	0b00000110,
	0b00000110,
	0b00000110,
	0b00111100),
	(  "107 k",
	0b00000000,
	0b01100000,
	0b01100000,
	0b01101100,
	0b01111000,
	0b01101100,
	0b01100110,
	0b00000000),
	(  "108 l",
	0b00000000,
	0b00111000,
	0b00011000,
	0b00011000,
	0b00011000,
	0b00011000,
	0b00111100,
	0b00000000),
	(  "109 m",
	0b00000000,
	0b00000000,
	0b01100110,
	0b01111111,
	0b01111111,
	0b01101011,
	0b01100011,
	0b00000000),
	(  "110 n",
	0b00000000,
	0b00000000,
	0b01111100,
	0b01100110,
	0b01100110,
	0b01100110,
	0b01100110,
	0b00000000),
	(  "111 o",
	0b00000000,
	0b00000000,
	0b00111100,
	0b01100110,
	0b01100110,
	0b01100110,
	0b00111100,
	0b00000000),
	(  "112 p",
	0b00000000,
	0b00000000,
	0b01111100,
	0b01100110,
	0b01100110,
	0b01111100,
	0b01100000,
	0b01100000),
	(  "113 q",
	0b00000000,
	0b00000000,
	0b00111110,
	0b01100110,
	0b01100110,
	0b00111110,
	0b00000110,
	0b00000110),
	(  "114 r",
	0b00000000,
	0b00000000,
	0b01111100,
	0b01100110,
	0b01100000,
	0b01100000,
	0b01100000,
	0b00000000),
	(  "115 s",
	0b00000000,
	0b00000000,
	0b00111110,
	0b01100000,
	0b00111100,
	0b00000110,
	0b01111100,
	0b00000000),
	(  "116 t",
	0b00000000,
	0b00011000,
	0b01111110,
	0b00011000,
	0b00011000,
	0b00011000,
	0b00001110,
	0b00000000),
	(  "117 u",
	0b00000000,
	0b00000000,
	0b01100110,
	0b01100110,
	0b01100110,
	0b01100110,
	0b00111110,
	0b00000000),
	(  "118 v",
	0b00000000,
	0b00000000,
	0b01100110,
	0b01100110,
	0b01100110,
	0b00111100,
	0b00011000,
	0b00000000),
	(  "119 w",
	0b00000000,
	0b00000000,
	0b01100011,
	0b01101011,
	0b01111111,
	0b00111110,
	0b00110110,
	0b00000000),
	(  "120 x",
	0b00000000,
	0b00000000,
	0b01100110,
	0b00111100,
	0b00011000,
	0b00111100,
	0b01100110,
	0b00000000),
	(  "121 y",
	0b00000000,
	0b00000000,
	0b01100110,
	0b01100110,
	0b01100110,
	0b00111110,
	0b00001100,
	0b01111000),
	(  "122 z",
	0b00000000,
	0b00000000,
	0b01111110,
	0b00001100,
	0b00011000,
	0b00110000,
	0b01111110,
	0b00000000),
	(  "123 {",
	0b00000000,
	0b00001110,
	0b00011000,
	0b00011000,
	0b00110000,
	0b00011000,
	0b00011000,
	0b00001110),
	(  "124 |",
	0b00001000,
	0b00001000,
	0b00001000,
	0b00001000,
	0b00001000,
	0b00001000,
	0b00001000,
	0b00001000),
	(  "125 }",
	0b00000000,
	0b00111000,
	0b00001100,
	0b00001100,
	0b00000110,
	0b00001100,
	0b00001100,
	0b00111000),
	(  "126 ~",
	0b00000000,
	0b00011010,
	0b00101100,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000),
	(  "127 Left Arrow",
	0b00000000,
	0b00010000,
	0b00110000,
	0b01111111,
	0b01111111,
	0b00110000,
	0b00010000,
	0b00000000),
	(  "128 British Pound",
	0b00001100,
	0b00010010,
	0b00110000,
	0b01111100,
	0b00110000,
	0b01100010,
	0b11111100,
	0b00000000),
	(  "129 Up Arrow",
	0b00000000,
	0b00011000,
	0b00111100,
	0b01111110,
	0b00011000,
	0b00011000,
	0b00011000,
	0b00011000),
	(  "130 Left Arrow",
	0b00000000,
	0b00010000,
	0b00110000,
	0b01111111,
	0b01111111,
	0b00110000,
	0b00010000,
	0b00000000),
	(  "131 Checker Board",
	0b10101010,
	0b01010101,
	0b10101010,
	0b01010101,
	0b10101010,
	0b01010101,
	0b10101010,
	0b01010101),
	(  "132",
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000),
	(  "133 F1",
	0b00000000,
	0b00000000,
	0b01110010,
	0b01000110,
	0b01100010,
	0b01000010,
	0b01000111,
	0b00000000),
	(  "134 F3",
	0b00000000,
	0b00000000,
	0b01110111,
	0b01000001,
	0b01100011,
	0b01000001,
	0b01000111,
	0b00000000),
	(  "135 F5",
	0b00000000,
	0b00000000,
	0b01110111,
	0b01000100,
	0b01100110,
	0b01000001,
	0b01000110,
	0b00000000),
	(  "136 F7",
	0b00000000,
	0b00000000,
	0b01110111,
	0b01000001,
	0b01100001,
	0b01000010,
	0b01000010,
	0b00000000),
	(  "137 F2",
	0b00000000,
	0b00000000,
	0b01110110,
	0b01000001,
	0b01100110,
	0b01000100,
	0b01000111,
	0b00000000),
	(  "138 F4",
	0b00000000,
	0b00000000,
	0b01110010,
	0b01000110,
	0b01101111,
	0b01000010,
	0b01000010,
	0b00000000),
	(  "139 F6",
	0b00000000,
	0b00000000,
	0b01110011,
	0b01000100,
	0b01100111,
	0b01000101,
	0b01000111,
	0b00000000),
	(  "140 F8",
	0b00000000,
	0b00000000,
	0b01110111,
	0b01000101,
	0b01100111,
	0b01000101,
	0b01000111,
	0b00000000),
	(  "141",
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000),
	(  "142",
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000),
	(  "143",
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000),
	(  "144",
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000),
	(  "145",
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000),
	(  "146",
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000),
    (  "147",
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000),
    (  "148",
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000,
	0b00000000),
    (  "149",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000111,
    0b00001111,
    0b00011100,
    0b00011000,
    0b00011000),
    (  "150",
    0b11000011,
    0b11100111,
    0b01111110,
    0b00111100,
    0b00111100,
    0b01111110,
    0b11100111,
    0b11000011),
    (  "151",
    0b00000000,
    0b00111100,
    0b01111110,
    0b01100110,
    0b01100110,
    0b01111110,
    0b00111100,
    0b00000000),
    (  "152 Club",
    0b00011000,
    0b00011000,
    0b01100110,
    0b01100110,
    0b00011000,
    0b00011000,
    0b00111100,
    0b00000000),
    (  "153",
    0b00000110,
    0b00000110,
    0b00000110,
    0b00000110,
    0b00000110,
    0b00000110,
    0b00000110,
    0b00000110),
    (  "154 Diamond",
    0b00001000,
    0b00011100,
    0b00111110,
    0b01111111,
    0b00111110,
    0b00011100,
    0b00001000,
    0b00000000),
    (  "155",
    0b00011000,
    0b00011000,
    0b00011000,
    0b11111111,
    0b11111111,
    0b00011000,
    0b00011000,
    0b00011000),
    (  "156",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "157",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "158",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "159",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "160",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "161",
    0b11110000,
    0b11110000,
    0b11110000,
    0b11110000,
    0b11110000,
    0b11110000,
    0b11110000,
    0b11110000),
    (  "162",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b11111111,
    0b11111111,
    0b11111111,
    0b11111111),
    (  "163",
    0b11111111,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "164",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b11111111),
    (  "165",
    0b10000000,
    0b10000000,
    0b10000000,
    0b10000000,
    0b10000000,
    0b10000000,
    0b10000000,
    0b10000000),
    (  "166",
    0b11001100,
    0b11001100,
    0b00110011,
    0b00110011,
    0b11001100,
    0b11001100,
    0b00110011,
    0b00110011),
    (  "167",
    0b00000001,
    0b00000001,
    0b00000001,
    0b00000001,
    0b00000001,
    0b00000001,
    0b00000001,
    0b00000001),
    (  "168",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b11001100,
    0b11001100,
    0b00110011,
    0b00110011),
    (  "169",
    0b11111111,
    0b11111110,
    0b11111100,
    0b11111000,
    0b11110000,
    0b11100000,
    0b11000000,
    0b10000000),
    (  "170",
    0b00000011,
    0b00000011,
    0b00000011,
    0b00000011,
    0b00000011,
    0b00000011,
    0b00000011,
    0b00000011),
    (  "171",
    0b00011000,
    0b00011000,
    0b00011000,
    0b00011111,
    0b00011111,
    0b00011000,
    0b00011000,
    0b00011000),
    (  "172",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00001111,
    0b00001111,
    0b00001111,
    0b00001111),
    (  "173",
    0b00011000,
    0b00011000,
    0b00011000,
    0b00011111,
    0b00011111,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "174",
    0b00000000,
    0b00000000,
    0b00000000,
    0b11111000,
    0b11111000,
    0b00011000,
    0b00011000,
    0b00011000),
    (  "175",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b11111111,
    0b11111111),
    (  "176",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00011111,
    0b00011111,
    0b00011000,
    0b00011000,
    0b00011000),
    (  "177",
    0b00011000,
    0b00011000,
    0b00011000,
    0b11111111,
    0b11111111,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "178",
    0b00000000,
    0b00000000,
    0b00000000,
    0b11111111,
    0b11111111,
    0b00011000,
    0b00011000,
    0b00011000),
    (  "179",
    0b00011000,
    0b00011000,
    0b00011000,
    0b11111000,
    0b11111000,
    0b00011000,
    0b00011000,
    0b00011000),
    (  "180",
    0b11000000,
    0b11000000,
    0b11000000,
    0b11000000,
    0b11000000,
    0b11000000,
    0b11000000,
    0b11000000),
    (  "181",
    0b11100000,
    0b11100000,
    0b11100000,
    0b11100000,
    0b11100000,
    0b11100000,
    0b11100000,
    0b11100000),
    (  "182",
    0b00000111,
    0b00000111,
    0b00000111,
    0b00000111,
    0b00000111,
    0b00000111,
    0b00000111,
    0b00000111),
    (  "183",
    0b11111111,
    0b11111111,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "184",
    0b11111111,
    0b11111111,
    0b11111111,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "185",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b11111111,
    0b11111111,
    0b11111111),
    (  "186",
    0b00000011,
    0b00000011,
    0b00000011,
    0b00000011,
    0b00000011,
    0b00000011,
    0b11111111,
    0b11111111),
    (  "187",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b11110000,
    0b11110000,
    0b11110000,
    0b11110000),
    (  "188",
    0b00001111,
    0b00001111,
    0b00001111,
    0b00001111,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "189",
    0b00011000,
    0b00011000,
    0b00011000,
    0b11111000,
    0b11111000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "190",
    0b11110000,
    0b11110000,
    0b11110000,
    0b11110000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "191",
    0b11110000,
    0b11110000,
    0b11110000,
    0b11110000,
    0b00001111,
    0b00001111,
    0b00001111,
    0b00001111),
    (  "192",
    0b00000000,
    0b00000000,
    0b00000000,
    0b11111111,
    0b11111111,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "193 Spade",
    0b00001000,
    0b00011100,
    0b00111110,
    0b01111111,
    0b01111111,
    0b00011100,
    0b00111110,
    0b00000000),
    (  "194",
    0b00011000,
    0b00011000,
    0b00011000,
    0b00011000,
    0b00011000,
    0b00011000,
    0b00011000,
    0b00011000),
    (  "195",
    0b00000000,
    0b00000000,
    0b00000000,
    0b11111111,
    0b11111111,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "196",
    0b00000000,
    0b00000000,
    0b11111111,
    0b11111111,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "197",
    0b00000000,
    0b11111111,
    0b11111111,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "198",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b11111111,
    0b11111111,
    0b00000000,
    0b00000000),
    (  "199",
    0b00110000,
    0b00110000,
    0b00110000,
    0b00110000,
    0b00110000,
    0b00110000,
    0b00110000,
    0b00110000),
    (  "200",
    0b00001100,
    0b00001100,
    0b00001100,
    0b00001100,
    0b00001100,
    0b00001100,
    0b00001100,
    0b00001100),
    (  "201",
    0b00000000,
    0b00000000,
    0b00000000,
    0b11100000,
    0b11110000,
    0b00111000,
    0b00011000,
    0b00011000),
    (  "202",
    0b00011000,
    0b00011000,
    0b00011100,
    0b00001111,
    0b00000111,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "203",
    0b00011000,
    0b00011000,
    0b00111000,
    0b11110000,
    0b11100000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "204",
    0b11000000,
    0b11000000,
    0b11000000,
    0b11000000,
    0b11000000,
    0b11000000,
    0b11111111,
    0b11111111),
    (  "205",
    0b11000000,
    0b11100000,
    0b01110000,
    0b00111000,
    0b00011100,
    0b00001110,
    0b00000111,
    0b00000011),
    (  "206",
    0b00000011,
    0b00000111,
    0b00001110,
    0b00011100,
    0b00111000,
    0b01110000,
    0b11100000,
    0b11000000),
    (  "207",
    0b11111111,
    0b11111111,
    0b11000000,
    0b11000000,
    0b11000000,
    0b11000000,
    0b11000000,
    0b11000000),
    (  "208",
    0b11111111,
    0b11111111,
    0b00000011,
    0b00000011,
    0b00000011,
    0b00000011,
    0b00000011,
    0b00000011),
    (  "209",
    0b00000000,
    0b00111100,
    0b01111110,
    0b01111110,
    0b01111110,
    0b01111110,
    0b00111100,
    0b00000000),
    (  "210",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b11111111,
    0b11111111,
    0b00000000),
    (  "211 Heart",
    0b00110110,
    0b01111111,
    0b01111111,
    0b01111111,
    0b00111110,
    0b00011100,
    0b00001000,
    0b00000000),
    (  "212",
    0b01100000,
    0b01100000,
    0b01100000,
    0b01100000,
    0b01100000,
    0b01100000,
    0b01100000,
    0b01100000),
    (  "213",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000111,
    0b00001111,
    0b00011100,
    0b00011000,
    0b00011000),
    (  "214",
    0b11000011,
    0b11100111,
    0b01111110,
    0b00111100,
    0b00111100,
    0b01111110,
    0b11100111,
    0b11000011),
    (  "215",
    0b00000000,
    0b00111100,
    0b01111110,
    0b01100110,
    0b01100110,
    0b01111110,
    0b00111100,
    0b00000000),
    (  "216 Club",
    0b00011000,
    0b00011000,
    0b01100110,
    0b01100110,
    0b00011000,
    0b00011000,
    0b00111100,
    0b00000000),
    (  "217",
    0b00000110,
    0b00000110,
    0b00000110,
    0b00000110,
    0b00000110,
    0b00000110,
    0b00000110,
    0b00000110),
    (  "218 Diamond",
    0b00001000,
    0b00011100,
    0b00111110,
    0b01111111,
    0b00111110,
    0b00011100,
    0b00001000,
    0b00000000),
    (  "219",
    0b00011000,
    0b00011000,
    0b00011000,
    0b11111111,
    0b11111111,
    0b00011000,
    0b00011000,
    0b00011000),
    (  "220",
    0b11000000,
    0b11000000,
    0b00110000,
    0b00110000,
    0b11000000,
    0b11000000,
    0b00110000,
    0b00110000),
    (  "221",
    0b00011000,
    0b00011000,
    0b00011000,
    0b00011000,
    0b00011000,
    0b00011000,
    0b00011000,
    0b00011000),
    (  "222 PI",
    0b00000000,
    0b00000000,
    0b00000011,
    0b00111110,
    0b01110110,
    0b00110110,
    0b00110110,
    0b00000000),
    (  "223",
    0b11111111,
    0b01111111,
    0b00111111,
    0b00011111,
    0b00001111,
    0b00000111,
    0b00000011,
    0b00000001),
    (  "224",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "225",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "226",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "227",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "228",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "229",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "230",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "231",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "232",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "233",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "234",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "235",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "236",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "237",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "238",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "239",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "240",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "241",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "242",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "243",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "244",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "245",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "246",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "247",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "248",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "249",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "250",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "251",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "252",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "253",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "254",
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000),
    (  "255 Smiley",
    0b00111100,
    0b01000010,
    0b10100101,
    0b10000001,
    0b10100101,
    0b10011001,
    0b01000010,
    0b00111100)
)

#----------------------------------------------------------------------------
def flip_bits(abyte):

    val = 0
    for _ in range(8):
        val <<= 1
        if abyte & 1:
            val |= 1
        abyte >>= 1

    return val

#----------------------------------------------------------------------------
print("Make C64 Char Set -> char_set.txt")

with open("char_set.txt", "wt") as ofp:
    for tpl in bitmap:

        ofp.write("\t\t\tbyte\t")
        for i in range(1, 8):
            val = flip_bits(tpl[i])
            s1 = "${:02X}, ".format(val)
            ofp.write(s1)

        val = flip_bits(tpl[8])
        s1 = "${:02X} ' {} \n".format(val, tpl[0])
        ofp.write(s1)
    



