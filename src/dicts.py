'''
DTMF telephone keypad from https://en.wikipedia.org/wiki/Dual-tone_multi-frequency_signaling:


Number keys to letters:

0	none (on some telephones, "OPERATOR" or "OPER")  (used often for space)
1	none (on some older telephones, QZ)
2	ABC
3	DEF
4	GHI
5	JKL
6	MNO (on some older telephones, MN)
7	PQRS (on older telephones, PRS)
8	TUV
9	WXYZ (on older telephones, WXY)

tones:

	        1209 Hz	1336 Hz	1477 Hz	1633 Hz
    697 Hz	1	  2	        3	       A
    770 Hz	4	  5	        6	       B
    852 Hz	7	  8	        9	       C
    941 Hz	*	  0	        #	       D

'''

letter_to_num = {
    " ":"0",
    "ABC":"2",
    "DEF":"3",
    "GHI":"4",
    "JKL":"5",
    "MNO":"6",
    "PQRS":"7",
    "TUV":"8",
    "WXYZ":"9"
}

num_to_letter = {v:k for k,v in letter_to_num.items()}

num_to_freq = {
    "0":(941,1336),
    "2":(697,1336),
    "3":(697,1477),
    "4":(770,1209),
    "5":(770,1336),
    "6":(770,1477),
    "7":(852,1209),
    "8":(852,1336),
    "9":(852,1477)
}
