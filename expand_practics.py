s = "a\tb\tc"
s.expandtabs()
print(s.expandtabs(4))
#탭간격을 8칸으로 설정 한것 까진 알겠는데
# 8칸 이상을 넣어도 왜 칸이 달라지질 않을까?
# 8칸을 설정하면 7칸으로 들어가는데 왜그러지?
a = "hello\tworld"
print(a.expandtabs(9))
print(a.expandtabs(16))

import re
m = re.match(r"(\w+)-(\w+)", "foo-bar")
m.expand(r"\1 \2")
m.expand(r"\2:\1")
print(m.expand(r"\2:\1"))

text = "x\ty"
result = text.expandtabs(8)
print(result)

def expand_text(s):
    return s.expandtabs(4)
print(expand_text("hello\tworld"))

#match.expand("문자열")
#바로 위의 match.expand는 expandtabs()의 문법 형태
import re
m = re.match(r"(\w+) (\w+)", "Hello World")
print(m.expand(r"\2 \1"))
print(m.expand(r"greeting: \1"))

#예제
# \w+가 단어라는 뜻인가?





