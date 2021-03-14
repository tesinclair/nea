

def transliterate(text):
   # While text shouldn't be more than 3 if there is not a transliterateable set in the first three, 
   # it will keep going unity there is
    while len(text) > 3: 
        text = text[1:] # removes the first letter

    # Private Constants
    HIRAGANA = {"a": "あ", "i": "い", "u": "う", "e": "え", "o": "お",
                    "ka": "か", "ki": "き", "ku": "く", "ke": "け", "ko": "こ",
                    "sa": "さ", "shi": "し", "su": "す", "se": "せ", "so": "そ",
                    "ta": "た", "chi": "ち", "tsu": "つ", "te": "て", "to": "と",
                    "na": "な", "ni": "に", "nu": "ぬ", "ne": "ね", "no": "の",
                    "ha": "は", "hi": "ひ", "fu": "ふ", "he": "へ", "ho": "ほ",
                    "ma": "ま", "mi": "み", "mu": "む", "me": "め", "mo": "も",
                    "ra": "ら", "ri": "り", "ru": "る", "re": "れ", "ro": "ろ",
                    "ya": "や", "yu": "ゆ", "yo": "よ", "wa": "わ", "wo": "を",
                    "n": "ん",
                    "ga": "が", "gi": "ぎ", "gu": "ぐ", "ge": "げ", "go": "ご",
                    "za": "ざ", "ji": "じ", "zu": "ず", "ze": "ぜ", "zo": "ぞ",
                    "da": "だ", "di": "ぢ", "du": "づ", "de": "で", "do": "ど",
                    "ba": "ば", "bi": "び", "bu": "ぶ", "be": "べ", "bo": "ぼ",
                    "pa": "ぱ", "pi": "ぴ", "pu": "ぷ", "pe": "ぺ", "po": "ぽ",
                    "tte": "って", "tta": "った",
                    "kya": "きゃ", "kyu": "きゅ", "kyo": "きょ", 
                    "sha": "しゃ", "shu": "しゅ", "sho": "しょ",
                    "cha": "ちゃ", "chu": "ちゅ", "cho": "ちょ",
                    "nya": "にゃ", "nyu": "にゅ", "nyo": "にょ",
                    "hya": "ひゃ", "hyu": "ひゅ", "hyo": "ひょ",
                    "mya": "みゃ", "myu": "みゅ", "myo": "みょ",
                    "rya": "りゃ", "ryu": "りゅ", "ryo": "りょ",
                    "gya": "ぎゃ", "gyu": "ぎゅ", "gyo": "ぎょ",
                    "ja": "じゃ", "ju": "じゅ", "jo": "じょ",
                    "bya": "びゃ", "byu": "びゅ", "byo": "びょ",
                    "pya": "ぴゃ", "pyu": "ぴゅ", "pyo": "ぴょ"
                    }

    # Private Variables

    transliterated = ""

    
    if len(text) == 1:
        if text == "n":
            return None
        for x in HIRAGANA:
            if text == x:
                transliterated = HIRAGANA[text]
    
                return transliterated

    elif len(text) == 2:
        for x in HIRAGANA:
            if text == x:
                transliterated = HIRAGANA[text]

                return transliterated

    elif (text) ==3:
        for x in HIRAGANA:
            if text == x:
                transliterated = HIRAGANA[text]

                return transliterated

    return None # If none of the if statements return anything, then return None