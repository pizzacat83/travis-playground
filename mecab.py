import MeCab
tagger = MeCab.Tagger("-Ochasen")
print(tagger.parse("すもももももももものうち"))
