
# -*- conding: utf-8 -*-
# KWIC検索

target = '言う'
context_width = 10

words = []
header = True

# ファイルを読み込んで単語リストを作成
datafile = open('b2.txt', encoding='utf-8')
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
    # 検索語が見つかったら

    if words[i]['語彙素'] == target:

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
            left_context,
            words[i]['書字形'],
            right_context])
        print(output)
