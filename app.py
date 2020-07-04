
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("csv_data/positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("csv_data/negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def strip_punctuation(x):
    for z in punctuation_chars:
        x = x.replace(z, '')
    return x
def get_pos(S):
    s = strip_punctuation(S)
    li = s.lower().split()
    ct = 0
   # print(li)
    for lo in li:
        if lo in positive_words:
            ct += 1
    return ct

def get_neg(S):
    s = strip_punctuation(S)
    li = s.lower().split()
    ct = 0
   # print(li)
    for lo in li:
        if lo in negative_words:
            ct += 1
    return ct

with open('csv_data/project_twitter_data.csv', 'r') as csv:
    ab_csv = csv.readlines()
   # print(ab_csv)
    p_list = []
    n_list = []
    for tweet in ab_csv[1:]:
        pos = get_pos(tweet)
        p_list.append(pos)
        neg = get_neg(tweet)
        n_list.append(neg)
with open('csv_data/resulting_data.csv', 'w') as w:
    w.write('{}, {}, {}, {}, {}'.format('Number of Retweets', 'Number of Replies', 'Positive Score', 'Negative Score', 'Net Score'))
    w.write('\n')
    count = 0
    kcsv = csv.readlines()
    notuse = kcsv.pop(0)
    print(kcsv)
    for r in kcsv:
        lio = r.strip().split(',')
        w.write('{}, {}, {}, {}, {}'.format(lio[1], lio[2], p_list[count], n_list[count], p_list[count] - n_list[count]))
        w.write('\n')
        count += 1
