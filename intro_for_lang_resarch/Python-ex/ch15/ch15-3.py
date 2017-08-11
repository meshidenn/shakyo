# -*- conding: utf-8 -*-
# コロケーションKWIC検索

conditions = [
    {'position': 0, 'key': '品詞', 'value': '動詞'},
    {'position': 1, 'key': '語彙素読み', 'value': 'ニクイ'},
    {'position': 1, 'key': '品詞', 'value': '接尾辞-形容詞的'}]


context_width = 10

words = []
header = True

# ファイルを読み込んで単語リストを作成

datafile = open('w2.txt', encoding='utf-8')
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

    # 検索条件がコーパスの範囲ないでない時はスキップ
    positions = []
    for cond in conditions:
        positions.append(cond['position'])
    if i + min(positions) < 0 or len(words) < i + max(positions):
        continue

    # 条件をすべて満たすかどうかチェック
    matched = True
    for cond in conditions:
        if cond['key'] in ['品詞', '活用形']:
            if not words[i + cond['position']][cond['key']].startswith(cond['value']):
                matched = False
                break
        else:
            if not words[i + cond['position']][cond['key']] == cond['value']:
                matched = False
                break

    # 検索条件にマッチしたら
    if matched:

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
