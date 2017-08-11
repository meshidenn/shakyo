
# -*- conding: utf-8 -*-
# コロケーションKWIC検索

import os
#folder = '/Users/hiroki/program/python/intro_for_lang_resarch/ch15'
folder = './text'
context_width = 10

words = []

# ファイルを読み込んで単語リストを作成
filenames = os.listdir(folder)
print(filenames)
for filename in filenames:
    header = True
    datafile = open(folder + '/' + filename, encoding='utf-8')
    for line in datafile:
        line = line.rstrip()

        if header:
            header = False
            keys = line.split('\t')
            continue

        values = line.split('\t')
        word = dict(zip(keys, values))

        words.append(word)

    # 検索
    for i in range(len(words)):
        # 最後の単語はチェックしない
        if i + 1 >= len(words):
            continue

    # 検索条件にマッチしたら

        if words[i]['品詞'].startswith('動詞') and words[i + 1]['語彙素読み'] == 'ニクイ' and words[i + 1]['品詞'] == '接尾辞-形容詞的':

            # 左側文脈を作成
            left_context = ''
            for j in range(i - context_width, i):
                if j < 0:
                    continue
                left_context += words[j]['書字形']

            # 右側文脈を作成
            right_context = ''
            for j in range(i + 1, i + 1 + context_width):
                if j >= len(words):
                    continue
                right_context += words[j]['書字形']

            # 出力
            output = '\t'.join([
                words[i]['出典'],
                left_context,
                words[i]['書字形'],
                right_context])
            print(output)
datafile.close()
