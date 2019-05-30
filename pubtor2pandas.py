import nltk

sent_no=0
def parse(input_file):

    with open(input_file) as fp:
        file_contents = fp.read()
    pubtator_entries = file_contents.split("\n\n")
    parse_entry(pubtator_entries[15])
    # for entry in pubtator_entries:
    #     if (entry != '\n'):
    #         # Parse entity separately.
    #         parse_entry(entry)

def parse_entry(entry):
    # Get HTML content
    lines = entry.split('\n')
    final_list=[]

    # Get PMID
    pmid = lines[0].split('|')[0].rstrip()

    # Get title of the paper
    title = lines[0].split('|')[2].rstrip()
    tag_table=[]
    global sent_no
    # Get abstract of the paper
    abstract = lines[1].split('|')[2]
    text_pri=title+abstract
    texts=[]
    for i in nltk.sent_tokenize(text_pri):
        text_sents=nltk.word_tokenize(i)
        nltk.tokenize
        for j in text_sents:
            final_list.append({'SENT_NO':sent_no,'PMID':pmid,'WORD':j,'CAT':'0','OID':'0'})
            texts.append(j)
        sent_no=sent_no+1
    text_tag=nltk.pos_tag(texts, tagset='universal')
    for i in range(0,len(text_tag)):
        final_list[i]['POS']=text_tag[i][1]

    for i in range(2, len(lines)):
        line = lines[i].split('\t')
        startOffset = int(line[1])
        endOffset = int(line[2])
        tag = line[3]
        cat=line[4]
        OID=line[5]
        tem={'pmid':pmid,'start off set':startOffset,'end off set':endOffset,'tag':tag,'OID':OID,'CAT':cat}
        tag_table.append(tem)
    tag_count=0
    tag_table_copy=tag_table.copy()
    tag_table_len=len(tag_table)
    tab_pos=0
    for index, word in enumerate(final_list):
        if tab_pos<tag_table_len:
            tag=tag_table[tab_pos]
            tags = tag['tag'].split(" ")
            print(tags[0]+"    "+word['WORD'])
            if tags[0] in word['WORD'] or word['WORD'] in tags[0]:
                match_seq_flag = False
                if index+len(tags)<=len(final_list):
                    words_lenth=0
                    for lenth in range(1, 25):
                        tem_sent = word['WORD']
                        for next_number in range(1,lenth):
                            tem_sent=tem_sent+" "+final_list[index + next_number]['WORD']
                            print("      sss: " + tem_sent + "    " + tag['tag'])
                        if tag['tag'] in tem_sent:
                            words_lenth=lenth
                            match_seq_flag = True
                            break
                    # if final_list[index + next_number]['WORD'] not in tags[next_number] or tags[next_number] not in \
                    #         final_list[index + next_number]['WORD']:
                    #     match_seq_flag = False


                    if match_seq_flag:
                        tag_count+=1
                        for next_number in range(0, words_lenth):
                            final_list[index+next_number]['CAT'] = tag['CAT']
                            final_list[index+next_number]['OID'] = tag['OID']
                            final_list[index+next_number]['start off set']=tag['start off set']
                            final_list[index+next_number]['end off set']=tag['end off set']
                            print(final_list[index+next_number])
                        tab_pos+=1


    if tag_count!=len(tag_table_copy):
        print(tag_count)
        print(len(tag_table_copy))
        print(tag_table)
        print("this is wrong")


    # count_w = 0
    # for tag in tag_table:
    #     count=0
    #     number_of_word=0
    #     for word in final_list:
    #         if int(tag['start off set'])-10 < count < int(tag['end off set'])+15:
    #             tags=tag['tag'].split(" ")
    #             if word['WORD'] in tags:
    #                 word['CAT']=tag['CAT']
    #                 word['OID']=tag['OID']
    #                 number_of_word = number_of_word + 1
    #                 # print(word)
    #         count = count + len(word['WORD'])

            # if word['WORD'] not in [',','.',')','(',':',';','%','"',"'",'[',']']:
            #     count=count+1
            #print(tag['start off set'])
        # if len(tag['tag'].split(' '))!=number_of_word:
        #     count_w=count_w+1
        #     print(len(tag['tag'].split(' ')))
        #     print(number_of_word)
        #     print("this is wrong")
        #     print(tag)






    # count_yes=0
    #
    # for tag in tag_table:
    #     taglen=len(tag['tag'].split(' '))
    #     for index in range(0,len(text_tag)):
    #         text_total=''
    #         if index+taglen<len(text_tag):
    #             for pos in range(index,index+taglen):
    #                 text_total=text_total+text_tag[pos][0]
    #                 if pos!=index + taglen - 1:
    #                     text_total=text_total+" "
    #         if text_total == tag['tag']:
    #             count_yes+=1
    # print(count_yes)




parse('corpus/NCBItrainset_corpus.txt')
print('rare' in 'rare,')