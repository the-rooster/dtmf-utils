# dtmf-utils
Dual tone multi frequency encoder and decoder

Dual tone multi frequency is a technology employed in older cell phones that ties button presses to a pair of unique tones to facilitate texting.
This repo provides tools to encode alphabetic strings as a .wav DTMF audio file, and also to decode these produced audio files back into a string by
recursively obtaining all of the possible decodings.

Inspired by CTF challenges, and mostly made for fun as it is a unique challenge between algorithms and signal processing.


TODO:
  -Determine a correctness likelihood for each possible decoding and display them ranked
  
   -Either with some kind of entropy calculation like what can be seen on cyberchef, or something more exotic maybe, such as deep learning to determine likelihood of a decoding
     being valid english.
     
  -Create a single commandline tool for both encoding and decoding

More information on DTMF:

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
 
Each number has two frequencies, represented by the row and column label.
