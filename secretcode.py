#now i am going to again attempt this exercise this time with a hint
#SECRET CODE
msg=input("Enter your message : ")
print("Press 1 for encoding\nPress 2 for decoding\nPress 3 to quit")
ch=int(input("Enter your choice : "))
if ch==1:
    newstr=msg.split()
    # print(newstr)
    newwords=[]
    for word in newstr:
        if len(word)>3:
            word=word[1:]+word[0]
            word="are"+word+"stp"
            newwords.append(word)
            # print("The encrypted message : ",word)

        else:
            word=word[::-1]  #this is method of reversing the string through slicing
            newwords.append(word)
    # print("The encrypted message : ",word)

    sentence=" ".join(newwords)
    print(sentence)

    # print("The encrypted message : ", sentence)



if ch==2:
    newstr=msg.split()
    newwords=[]
    for word in newstr:
        if len(word)>3:
            word=word[3:len(word)-3]
            word=word[len(word)-1]+word[0:len(word)-1]
            newwords.append(word)
            # print("The decoded message : ",word)

        else:
            word=word[::-1]
            newwords.append(word)
            # print("The encrypted message : ",word)
    sentence=" ".join(newwords)
    print(sentence)


    # if(len(msg)>3):
    #     newlist=[]
    #     for word in msg:
    #         newlist.append(word)
    #
    #     # temp=list(msg)
    #     # temp.append(msg[0])
if ch==3:
    exit()


