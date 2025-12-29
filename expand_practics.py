s = "a\tb\tc"
s.expandtabs()
print(s.expandtabs(10))
#탭간격을 8칸으로 설정 한것 까진 알겠는데
# 8칸 이상을 넣어도 왜 칸이 달라지질 않을까?

a = "hello\tworld
print(a.expandtabs(9))

import re

m = re.match(r"(\w+)-(\w+)", "foo-bar")
m.expand(r"\1 \2")
m.expand(r"\2:\1")

text = "x\ty"
result = text.expandtabs(2)

def expand_text(s):
    return s.expandtabs(4)

#match.expand("문자열")
#바로 위의 match.expand는 expandtabs()의 문법 형태
import re

m = re.match(r"(\w+) (\w+)", "Hello World")
print(m.expand(r"\2 \1"))
#예제
# \w+가 단어라는 뜻인가?





