'''
analyse the content
'''
import os, re, shutil
from tqdm import tqdm
import pandas as pd
import paddlehub as hub
from collections import defaultdict

def clean_duplication(text):
    left_square_brackets_pat = re.compile(r'\[+')
    right_square_brackets_pat = re.compile(r'\]+')
    punct = [',', '\\.', '\\!', '，', '。', '！', '、', '\\?', '？']

    def replace(string, char):
        pattern = char + '{2,}'
        if char.startswith('\\'):
            char = char[1:]
        string = re.sub(pattern, char, string)
        return string

    text = left_square_brackets_pat.sub('', text)
    text = right_square_brackets_pat.sub('', text)
    for p in punct:
        text = replace(text, p)
    return text

def emoji2zh(text, inverse_emoji_dict):
    for emoji, ch in inverse_emoji_dict.items():
        text = text.replace(emoji, ch)
    return text

def clean_emotion(data_path, emoji2zh_data, save_dir, train=True):
    data = defaultdict(list)
    filename = os.path.basename(data_path)
    with open(data_path, 'r', encoding='utf8') as f:
        texts = f.readlines()
        for line in tqdm(texts, desc=data_path, leave=False):
            if train:
                id_, text, label = line.strip().split('\t')
            else:
                id_, text = line.strip().split('\t')
            data['id'].append(id_)
            text = emoji2zh(text, emoji2zh_data)
            text = clean_duplication(text)
            data['text_a'].append(text)
            if train:
                data['label'].append(label)
    df = pd.DataFrame(data)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    df.to_csv(os.path.join(save_dir, filename), index=False,
              encoding='utf8', header=False, sep='\t')
    return df


preDir = os.path.dirname(os.path.realpath(__file__))
inclDir = os.path.join(preDir, 'incl')

labelList=['难过', '愉快', '喜欢', '愤怒', '害怕', '惊讶', '厌恶']
labelMap = {
    idx: label_text for idx, label_text in enumerate(labelList)
}

model = hub.Module(
    name='ernie_tiny',
    task='seq-cls',
    num_classes=7,
    load_checkpoint=os.path.join(inclDir, 'model.pdparams'),
    label_map=labelMap)

def Analyse(res, data = []):
    results = model.predict(data, max_seq_len=128, batch_size=1, use_gpu=False)
    for idx, text in enumerate(data):
        res[idx] = 'Data: {} \t Lable: {}'.format(text[0], results[idx])
    return