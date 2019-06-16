import pandas as pd

df = pd.read_csv('crimepow.csv',sep ='\t')

# =============================================================================
# sp = df['text'].iloc[0].split()
# text =[]
# for i in range (9,len(sp)):
#     if 'Ⓒ' == sp[i]:
#         break
#     text.append(sp[i])
# 
# 
# text =' '.join(text)
# =============================================================================

def clean(sent):
    sp = sent.split()
    text =[]
    for i in range (9,len(sp)):
        if 'Ⓒ' == sp[i]:
            break
        text.append(sp[i])
    
    
    text =' '.join(text)
    return text

df['text'] = df['text'].apply(lambda x: clean(x))

df['text'].iloc[0]

df.to_csv('crime_clean.csv',sep='\t',index=False)

