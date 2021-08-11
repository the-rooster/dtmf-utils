import numpy as np
from scipy.signal import spectrogram
from scipy.io import wavfile
import dicts
import cv2

def decode_string(string):
    '''
    decodes a dtmf string (numbers representing button presses) to all of its possible interpretations using a recursive algorithm.
    '''

    class helperClass:
        '''
        recursive algorithm that finds all of the possible decodings of the dtmf string

        TODO: this broke
        '''
        res = []
        def helper(self,currNum,currS):
            #print(len(currNum))
            if len(currNum) == 0:
                print(currS,len(currNum))

                if currS is not None:
                    return currS
            #print(currNum,currS)
            temp = ""

            flag = False
            for i in range(len(currNum)):
                if currNum[i] not in temp:

                    if flag:
                        break
                    flag = True
                    temp = currNum[i]
                else:
                    temp += currNum[i]
                
                #print("THINGS:",currNum[i+1:],currS + dicts.num_to_letter[temp[0]][len(temp) - 1])
                #print("THINGS 2:",len(currNum))
                if len(currNum) > 1:
                    ret = self.helper(currNum[i+1:],currS + dicts.num_to_letter[temp[0]][len(temp) - 1])
                else:
                    ret = self.helper("",currS + dicts.num_to_letter[temp[0]][len(temp) - 1])
                
                if ret != None:
                    self.res.append(ret)

                    
    
    h = helperClass()
    h.helper(string,"")
    print(h.res)

def decode_audio(fname):
    '''
    decodes a audio file of dtmf into plaintext

    we take the stft of the audio and find the frequencies of the dtmf signal, decoding each frequency block into its corresponding button presses

    TODO: this broke too
    '''

    sample_rate, samples = wavfile.read(fname)
    #print(sample_rate,len(samples))
    f,t,Zxx = spectrogram(samples,sample_rate,nperseg=512,noverlap=256)

    cv2.imshow("test",cv2.resize(Zxx / np.max(Zxx),(1000,1000)))
    cv2.waitKey()


    #iterate through columns of spectrogram and find the relevant frequencies
    
    #bottom frequency max is 941 Hz. break frequencies apart based on this boundary

    freq_thresh_bot = 941

    freq_thresh_top = 1209

    num_res = ""

    in_signal = False

    for i in range(Zxx.T.shape[0]):
        col = Zxx.T[i]

        #threshold frequencies

        freqs = []

        if in_signal:
            freqs = f[np.where(col > 25000)]
        else:
            freqs = f[np.where(col > 55000)]



        if freqs.shape[0] > 0 and not in_signal:
            
            botFreq = np.mean(freqs[np.where(freqs < freq_thresh_bot)])

            topFreq = np.mean(freqs[np.where(freqs > freq_thresh_top)])

            
            #print(botFreq,topFreq)
            mostLikely = ("",1000)

            for c,pair in dicts.num_to_freq.items():
                diff = (pair[0] - botFreq)**2 + (pair[1] - topFreq)**2

                if diff < mostLikely[1]:
                    mostLikely = (c,diff)
            
            num_res += mostLikely[0]

            in_signal = True

        else:
            in_signal = False


    print("DECODED TO: {}".format(num_res))
    decode_string(num_res)


            
            
        

decode_audio("C:/Users/dagga/Documents/repos/dtmf-utils/test.wav")
