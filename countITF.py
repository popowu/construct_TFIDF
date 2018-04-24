#count ITF (each tweet as a document)
import math
import RegPattern
import re
import math
from nltk.corpus import stopwords

def tokens(str1): 
    stop_words = set(stopwords.words('english'))
    result = []
    for i in str1.strip().split(' '):
        # print i
        if i not in stop_words:
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

def readFile (filename):
    f_list = []
    with open(filename,'r') as f:
        lines = f.readlines()[:5000] #<============
        for line in lines:
            temp = line.strip().split('\t')
            # print (temp[0]) 
            f_list.append((str(temp[0]),int(temp[1])))
    return f_list

def readPortalFile(filename): #a tweet as a item in list
    p_list = []
    with open(filename,'r') as f:
        lines = f.readlines()
        for line in lines:
            split_line = line.split('\t')
            if len(split_line) != 2: continue
            p_list.append(tokens(regPatterns(checktag(removeRT(del_url(split_line[1]))))))
    return p_list



movie_list =  (readFile('output9/movie_noportal_Result'))
music_list =  (readFile('output9/music_noportal_Result'))
sport_list =  (readFile('output9/sport_noportal_Result'))
food_list =  (readFile('output9/food_noportal_Result'))

movie_portal = readPortalFile('input/movie_tweets_noportal1002')
music_portal = readPortalFile('input/music_tweets_noportal1002')
sport_portal = readPortalFile('input/sport_tweets_noportal1002')
food_portal = readPortalFile('input/food_tweets_noportal1002')


totalList = [movie_list,music_list,sport_list,food_list] #get total num of text file
totalportalList = [movie_portal,music_portal,sport_portal,food_portal]
interestlList = ['movie','music','sport','food'] #get total num of text file



for topic_list_index in range(len(totalList)):
    word_tuple_count = 0
    for word_tuple in totalList[topic_list_index]:
        word_in_tweet = 0
        for each_tweet in totalportalList[topic_list_index]:
            if word_tuple[0] in each_tweet:
                word_in_tweet += 1
                continue
        # print (round(float(len(movie_list))))
        # print (word_in_tweet)
        with open ('output9/output_ITF_{}'.format(interestlList[topic_list_index]),'a') as out_file:
            out_file.write(word_tuple[0] + '\t' + str(round(float(len(totalportalList[topic_list_index]))/float(word_in_tweet),3))+ '\n')
        word_tuple_count += 1
        if word_tuple_count%10 ==0 : print (word_tuple_count)
    print ("finished==>")




# for topic_list in totalList:    
#     for word_tuple in topic_list:
#         word_in_list = 0
#         for each_topic_list in totalList:
#             for each_topic_word in each_topic_list:
#                 if word_tuple[0] in each_topic_word:
#                     word_in_list += 1
#                     break
#         with open ('output4.0/output_IDFv2_{}'.format(totalList.index(topic_list)),'a') as out_file:
#             out_file.write(word_tuple[0] + '\t' + str(float(len(totalList))/float(word_in_list))+ '\n')
#     print 'finished===>'

        # print(str(totalList.index(topic_list)) + '\t' + word_tuple[0] + '\t' + str(word_in_list))