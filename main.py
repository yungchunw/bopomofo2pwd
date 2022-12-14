from pypinyin import Style, pinyin
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-t", "--text", type=str,
                    help="請輸入需要轉換的中文", required=True)
args = parser.parse_args()

# 注音對照表
BOPOMOFO_TABLE = dict(zip(
    'ㄇㄖㄏㄎㄍㄑㄕㄘㄛㄨㄜㄠㄩㄙㄟㄣㄆㄐㄋㄔㄧㄒㄊㄌㄗㄈㄅㄉˇˋㄓˊ˙ㄚㄞㄢㄦㄤㄝㄡㄥ',
    'abcdefghijklmnopqrstuvwxyz1234567890-;,./'
))

def bopomofo_convert(raw_input):

    bopomofo_list = pinyin(raw_input, style=Style.BOPOMOFO)
    password = ''

    for bopomofo in bopomofo_list:
        for data in bopomofo:
            password += ''.join(BOPOMOFO_TABLE.get(x, x) for x in data)
    
    return password

if __name__ == '__main__':
    # '我的密碼' -> 'ji32k7au4a83'
    print(bopomofo_convert(args.text)) 