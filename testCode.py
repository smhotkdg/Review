import re
text = "이렇게 먹으면ㅋㅋㅋㅋ 살걱정없어욧"
pattern = '([ㄱ-ㅎㅏ-ㅣ])'
repl = ''
result = re.sub(pattern=pattern,repl=repl,string=text)
print(result)