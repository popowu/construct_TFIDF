import sys, gzip, re, os, fileinput
from collections import defaultdict
import operator
# sys.path.append('/home/jamie/Documents/getTweets/RegPattern.py')
import RegPattern
from nltk.corpus import stopwords
from nltk.corpus import words
from langdetect import detect
import langdetect
from datetime import datetime

#some pre-processing functions
def tokens(str1): 
    stop_words = set(stopwords.words('english'))
    result = []
    for i in str1.strip().split(' '):
        # print i
        # if i not in stop_words: #remove stopwords
        result.append(i)
    if result == []:
        result = ['']
    return result

# to remove url
def del_url(line): #return re.sub(r'https?:\/\/.*', "", line).lower()
    result = ''
    # p_list = ["s'","'s"]
    for i in re.sub(r'(https?:\/\/.*)|(pic\.twitter\.com)\S*', "", line).lower().split(' '):
        if "s'" in i:
            result += i.replace("s'"," ")
        elif "'s" in i:
            result += i.replace("'s"," ")
        elif i.startswith("'"):
            result += i.replace("'"," ") + " "
        elif i.endswith("'"):
            result += i.replace("'"," ")
        else:
            result += i + " "
                

    return result
# print (tokens(del_url("")))

def checktag(tweet):
    result = ''
    for i in tweet.split(' '):
        if i.startswith('#'): #remove @ amd # (# result += '<HASHTAG>' + ' ' + i.replace('#',''))
            # result += '<HASHTAG>'
            result += '<HASHTAG>' + ' ' + i.replace('#','')
            result += ' '
        elif i.startswith('@'):
            result += '<USER>'
            result += ' '
        elif 'pm' in i:
            result += i.replace('pm',' <PM>')#change the time format and add 'space' to be tokenized
            result += ' '
        else:
            result += i
            result += ' '
    return result

def removeRT(tweet): #if RT: then discard this tweet
    result = ''
    for i in tweet.split(' '):
        if i.startswith('rt') or i.startswith('RT'): #remove @ amd #
            break
        else:
            result += i
            result += ' '
    return result

reg = RegPattern.RegPattern()

def regTime(tweet):
    finalResult1 = ''
    result = (reg.get_pattern(tweet,'re_time'))
    # print reg.re_time
    # print result
    for i in result:
        finalResult1 += str(i) + ' '
    return finalResult1

def regPatterns(tweet):
    finalResult = ''
    result = (reg.get_pattern(tweet,'re_all'))
    # print result
    for i in result:
        finalResult += i + ' '
    return finalResult  

# print (tokens(regPatterns(checktag(removeRT(del_url("RT Oscar nominations uproar raises the question: Did racial bias, conscious or not, come into… https://t.co/M66tLsfwAH https://t.co/GQpyW4bipa"))))))

print (str(datetime.now())[:-7])
word_count_dict = defaultdict(lambda : 0)
with open('<YOUR INPUT FILE!>','r') as f: #<======
    for line in f.readlines():
        split_line = line.strip().split('\t')
        if len(split_line) != 2: continue
        uid, text = split_line
        # print (tokens(regPatterns(checktag(removeRT(del_url(text))))))
        
        if tokens(regPatterns(checktag(removeRT(del_url(text)))))[0] != '':
            for word in tokens(regPatterns(checktag(removeRT(del_url(text))))):
                word_count_dict[word] += 1

# #get TF result: wordcount/totalcount 
# totalcount = 0
# TF_dic = dict(word_count_dict)
# for word in TF_dic:
#     totalcount += TF_dic[word]
# for word in TF_dic:
#     TF_dic[word] = TF_dic[word]/totalcount

out = open('<YOUR OUTPUT FILE>','w')#<======
# out1 = open('output9/cooccurence_original/movie_noportal_Result1','w')#<======

for line in sorted(word_count_dict.items(), key=operator.itemgetter(1), reverse = True):
    out.write('{}\t{}\n'.format(line[0], str(round(line[1],7))))
    # out1.write('{}\t{}\n'.format(line[0], str(round(TF_dic[line[0]],7))))
# print (del_url("Meet Bolt. Usain Bolt.  Why the sprinter is 'not slick enough to be 007'.  Watch: https://t.co/FXKZif58yZ https://t.co/cxSFvzhTuD"))
print (str(datetime.now())[:-7])                                                                                                                                                                                                                                                                                                                        