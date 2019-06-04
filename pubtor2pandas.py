import nltk
import pandas as pd

sent_no=0
error_pmid=''
bug_model=False
def parse(input_file):

    with open(input_file) as fp:
        file_contents = fp.read()
    pubtator_entries = file_contents.split("\n\n")
    final_list=[]
    # parse_entry(pubtator_entries[15])
    for entry in pubtator_entries:
        if (entry != '\n'):
            # Parse entity separately.
            final_list.extend(parse_entry(entry))
    return final_list

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
    text_pri=title+" "+abstract
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
            tag_name = tag['tag'].split(" ")
            if tag['pmid'] == error_pmid:
                print('First char in tag: '+tag_name[0]+", WORD:  "+word['WORD']+", LENTH: "+str(len(word['WORD'])))
            if len(word['WORD'])>1 and (tag_name[0] in word['WORD'] or word['WORD'] in tag_name[0]):
                tab_pos, tag_count = found_match_word(final_list, index, tab_pos, tag, tag_count, tag_name, word)
            elif len(word['WORD'])==1 and tag_name[0]==word['WORD']:
                tab_pos, tag_count = found_match_word(final_list, index, tab_pos, tag, tag_count, tag_name, word)

    if tag_count!=len(tag_table_copy):
        print(tag_count)
        print(len(tag_table_copy))
        print(tag_table)
        print("this is wrong")
    if bug_model:print (final_list)
    return final_list

def found_match_word(final_list, index, tab_pos, tag, tag_count, tag_name, word):
    match_seq_flag = False
    if index + len(tag_name) <= len(final_list):
        words_lenth = 0
        for lenth in range(1, 25):
            tem_sent = word['WORD']
            if index+lenth<=len(final_list):
                for next_number in range(1, lenth):
                    tem_sent = tem_sent + final_list[index + next_number]['WORD']
                tem_sent2=tem_sent.replace(' ', '')
                tag2=tag['tag'].replace(' ', '')
                if tag['pmid']==error_pmid:
                    print("Compare: " + tem_sent2 + "， WITH TAG： " + tag2)
                if tag2 in tem_sent2 :
                    if tag['pmid'] == error_pmid:
                        print ("MATCH:"+tag2)
                    words_lenth = lenth
                    match_seq_flag = True
                    break

        if match_seq_flag:
            tag_count += 1
            if bug_model:print ('It is:')
            for next_number in range(0, words_lenth):
                final_list[index + next_number]['CAT'] = tag['CAT']
                final_list[index + next_number]['OID'] = tag['OID']
                # final_list[index + next_number]['start off set'] = tag['start off set']
                # final_list[index + next_number]['end off set'] = tag['end off set']
                if bug_model:print(final_list[index + next_number])
            tab_pos += 1
            if bug_model:print ('')
    return tab_pos, tag_count


list=parse('corpus/NCBItrainset_corpus.txt')
pd_data=pd.DataFrame(data=list)
pd_data.to_csv('NCBI_corpus_trainset.csv')
print (pd_data)
