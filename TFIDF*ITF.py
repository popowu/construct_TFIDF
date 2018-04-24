#find the weight of w1(TF*AIDF) + w2(ITF) 

from collections import OrderedDict
import math

def readFile (filename):
    f_list = OrderedDict()
    with open(filename,'r') as f:
        lines = f.readlines()[:5000]
        for line in lines:
            temp = line.strip().split('\t')
            # print (temp[0]) 
            f_list[str(temp[0])] = float(temp[1])
    return f_list

movie_TF =  (readFile('output9/movie_noportal_Result1'))
music_TF =  (readFile('output9/music_noportal_Result1'))
sport_TF =  (readFile('output9/sport_noportal_Result1'))
food_TF =  (readFile('output9/food_noportal_Result1'))

movie_AIDF =  (readFile('output9/output_AIDF_movie_list'))
music_AIDF =  (readFile('output9/output_AIDF_music_list'))
sport_AIDF =  (readFile('output9/output_AIDF_sport_list'))
food_AIDF =  (readFile('output9/output_AIDF_food_list'))

movie_ITF =  (readFile('output9/output_ITF_movie'))
music_ITF =  (readFile('output9/output_ITF_music'))
sport_ITF =  (readFile('output9/output_ITF_sport'))
food_ITF =  (readFile('output9/output_ITF_food'))

# print (movie_TF)
totalList = [movie_TF,music_TF,sport_TF,food_TF]
totalList1 = [movie_AIDF,music_AIDF,sport_AIDF,food_AIDF]
totalList2 = [movie_ITF,music_ITF,sport_ITF,food_ITF]
interestlList = ['movie','music','sport','food'] #get total num of text file


for i in range(4):
    for word in totalList[i]:
        TF = math.log10(1/totalList[i][word])
        # print (word)
        AIDF = math.log10(totalList1[i][word]+1)
        ITF =1/math.log10(math.log10(math.log10(totalList2[i][word])+1)+1)/10

        # with open ('output9/output_TFIDF1000_{}'.format(interestlList[i]),'a') as out_file:
        #     out_file.write(word + '\t' + str(round(float(1.0*TF*AIDF+0.0*ITF),5))+ '\n')
        # with open ('output9/output_TFIDF0901_{}'.format(interestlList[i]),'a') as out_file:
        #     out_file.write(word + '\t' + str(round(float(0.9*TF*AIDF+0.1*ITF),5))+ '\n')
        # with open ('output9/output_TFIDF0802_{}'.format(interestlList[i]),'a') as out_file:
        #     out_file.write(word + '\t' + str(round(float(0.8*TF*AIDF+0.2*ITF),5))+ '\n')
        with open ('output9/output_TFIDF0703_{}'.format(interestlList[i]),'a') as out_file1:
            out_file1.write(word + '\t' + str(round(float(0.7*TF*AIDF+0.3*ITF),5))+ '\n')
        with open ('output9/output_TFIDF0604_{}'.format(interestlList[i]),'a') as out_file2:
            out_file2.write(word + '\t' + str(round(float(0.6*TF*AIDF+0.4*ITF),5))+ '\n')