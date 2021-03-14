def compare(letter):
    vowels = ["a", "e", "i", "o", "u"]
    legal_consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "m", "n", "p", "r", "s", "t", "w", "y", "z"]

    for x in vowels:
        if x == letter:
            return "Vowel"

    for x in legal_consonants:
        if x == letter:
            return "Consonant"


def transliterate(text):
    hiragana = {"a": "あ", "i": "い", "u": "う", "e": "え", "o": "お",
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

    vowels = ["a", "e", "i", "o", "u"]
    legal_consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "m", "n", "p", "r", "s", "t", "w", "y", "z"]

    chars = [char for char in text]

    transliterated = ""

    if len(chars) == 1:
        for x in chars:
            for y in vowels:
                if x == y:
                    transliterated = hiragana[x]

    if len(chars) == 2:
        for x in chars:
            for y in legal_consonants:
                if x == y:
                    for z in vowels:
                        if chars[chars.index(x) + 1] == z:
                            transliterated = hiragana[x + chars[chars.index(x) + 1]]
                        elif chars[chars.index(x) + 1] == "n":
                            transliterated = hiragana["n"]

    elif len(chars) == 3:
        for x in chars:
            for y in legal_consonants:
                if x == y:
                    for z in legal_consonants:
                        if chars[chars.index(x) + 1] == z:
                            for q in vowels:
                                if chars[chars.index(x) + 2] == q:
                                    transliterated = hiragana[
                                        x + chars[chars.index(x) + 1] + chars[chars.index(x) + 2]]

    return transliterated