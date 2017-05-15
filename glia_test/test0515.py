
#Q 2-1

import string
from collections import defaultdict

def ngrams_probs(filename='raw_sentences.txt'):
    '''
    filename: 'raw_sentences.txt'
    output: tuple
    
    '''
    
    filename = open(filename, 'r')
    filelines = filename.readlines()

    word_cnt=[]
    for line in filelines:

        line = line.rstrip() #去除'\n'
        identity = string.maketrans(' ',' ')
        pun_num = string.punctuation + string.digits # 指定刪除的字符為：標點符號和數字
        line = line.translate(identity, pun_num) # 完成字符串中標點符號和數字的刪除
        line = line.lower()        
        word_list = line.split(' ')
        word_cnt += word_list

    filter(None, word_cnt) #刪除空白字串''
    word_cnt.remove('')
    ' '.join(word_cnt).split()
    #print(word_cnt)

    #輸出 n-grams
    N = 2
    grams2 = [word_cnt[i:i+N] for i in xrange(len(word_cnt) - N + 1)]
    #for gram in grams: print gram

    N = 3
    grams3 = [word_cnt[i:i+N] for i in xrange(len(word_cnt) - N + 1)]


    # 轉為出現頻率
    g2 = defaultdict(list)
    for g in grams2:
        g2[g] += 1

    g3 = defaultdict(list)
    for g in grams3:
        g3[g] += 1


    return g2, g3
        

# Q 2-2

def prob3(bigram, cnt2=cnt2, cnt3=cnt3):
    '''
    bigram: tuple
    cnt2: bigram probabilities
    cnt3: trigram probabilities
    '''
    
    

