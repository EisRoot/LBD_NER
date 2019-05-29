
def parse(input_file):

    with open(input_file) as fp:
        file_contents = fp.read()
    pubtator_entries = file_contents.split("\n\n")

    for entry in pubtator_entries:
        if (entry != '\n'):
            # Parse entity separately.
            parse_entry(entry)

def parse_entry(entry):
    # Get HTML content
    lines = entry.split('\n')

    # Get PMID
    pmid = lines[0].split('|')[0].rstrip()

    # Get title of the paper
    title = lines[0].split('|')[2].rstrip()
    cutoff = len(title)

    # Get abstract of the paper
    abstract = lines[1].split('|')[2]



    for i in range(2, len(lines)):

        # Define empty entity dictionary
        entity = {}
        line = lines[i].split('\t')

        # Start offset
        startOffset = int(line[1])
        endOffset = int(line[2])

        tag = line[3]
        cat=line[4]
        OID=line[5]
        mydata={'pmid':pmid,'start off set:':startOffset,'end off set':endOffset,'tag':tag,'OID':OID}
        print(mydata)


parse('corpus/NCBItrainset_corpus.txt')