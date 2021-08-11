import numpy as np
import math
import wave
import struct
import dicts

'''
code adapted from https://github.com/kronengold/tone-generator/blob/master/tonegen.py for tone generation and wav file creation!
'''
def get_tone(rate,freq,frames):
    return np.array([np.sin(2*math.pi*freq*(i / rate)) for i in range(frames)])

def gen_wav(fname, sine_list, frate, amp, nframes):
    '''
    generates a wav file for a given audio sample.
    '''
    nchannels = 1
    sampwidth = 2
    comptype = "NONE"
    compname = "not compressed"

    wav_file = wave.open(fname, "w")
    wav_file.setparams((nchannels, sampwidth, frate, nframes,
        comptype, compname))

    for s in sine_list:
        # write the audio frames to file
        wav_file.writeframes(struct.pack('h', int(s*amp/2)))

    wav_file.close()

    return

def encode_string(frate,nframes,string,sep):
    '''
    encodes a given string (alpha characters only!) into a series of tones with seperation between tones of sep frames
    '''
    
    #turn a string into a series of numbers representing the buttons pressed on a phone
    encoded_str = ""

    for c in string:
        
        if not c.isalpha() and not c == " ":
            raise Exception("Provided string must only be alphabetic characters!")
        
        for group in dicts.letter_to_num.items():
            if c.upper() in group[0]:
                encoded_str += ''.join([str(group[1]) for i in range(group[0].index(c.upper()) + 1)])
                break
    
    print("Encoded string as dtmf: {}".format(encoded_str))

    audio = []

    tone_func = lambda x: get_tone(frate,x,nframes)

    seperation = np.zeros(sep)

    #turns this encoded string into a series of tones
    for c in encoded_str:
        tones = dicts.num_to_freq[c]

        signal = tone_func(tones[0]) + tone_func(tones[1])
        audio.append(signal)
        audio.append(seperation)
    
    return np.concatenate(audio,axis=0)



if __name__ == "__main__":
    frate = 4100
    secsPerTone = 0.2
    sepSecs = 0.1
    amp = 20000

    waves = encode_string(frate,int(frate*secsPerTone),"test string",int(frate*sepSecs))

    gen_wav("test.wav",waves,frate,amp,len(waves))
