#count IDF
import math
def readFile (filename):
    f_list = []
    with open(filename,'r') as f:
        lines = f.readlines()[:10000]
        for line in lines:
            # print (line)
            temp = line.strip().split('\t')
            f_list.append((str(temp[0]),int(temp[1])))
    return f_list


movie_list =  (readFile('output9/movie_noportal_Result'))
music_list =  (readFile('output9/music_noportal_Result'))
sport_list =  (readFile('output9/sport_noportal_Result'))
food_list =  (readFile('output9/food_noportal_Result'))

totalList = [movie_list,music_list,sport_list,food_list] #get total num of text file
interestlList = ['movie_list','music_list','sport_list','food_list'] #get total num of text file

# print len(totalList)

# word_total = p(word|every_document)

for topic_list in totalList:   
    with open ('output9/output_AIDF_{}'.format(interestlList[totalList.index(topic_list)]),'w') as out_file:

        for word_tuple in topic_list:
            word_total = 0
            for each_topic_list in totalList:
                for each_topic_word in each_topic_list:
                    if word_tuple[0] in each_topic_word:
                        word_total += each_topic_word[1]
                        break
            out_file.write(word_tuple[0] + '\t' + str(round(float(word_total)/float(word_tuple[1]),7))+ '\n')
    print ('finished===>')

        # print(str(totalList.index(topic_list)) + '\t' + word_tuple[0] + '\t' + str(word_in_list))

