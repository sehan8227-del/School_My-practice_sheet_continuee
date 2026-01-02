#실험대
contents = []
contents = {
    "title": "DeathNote",
    "category": "contents",
    "format": "comics",
    "memo": "humanity chaos fall"
}

# - append로 리스트에 넣기를 시도 적용이 안됨.왜지?
#혹시나 해서 [contents.append]의 .append뒤 (contents)를 집어넣어도 안됨.이해가 안가 막힘.
#GPT에게 말해 본 결과 그냥
#contents.append(content) 이 문법이 맞았음.너무 어렵게 및 꼬여서 생각함.
contents = []
contents1 = [{
    "title": "DeathNote",
    "category": "contents",
    "format": "comics",
    "memo": "humanity chaos fall"
}],
contents2 =[{
    "title": "강철의 연금술사",
    "category": "콘텐츠",
    "format": "만화",
    "memo": "인간이 인간 다워 질 수 있는 인간찬가",
}],
contents3 =[{
    "title": "던전밥",
    "category": "콘텐츠",
    "format": "만화",
    "memo": "상상속 식재료라도 인간의 상상을 벗어날 수 없는 요리만 나오지만 배우고 싶은 요리 레시피북",
}]
contents.append(2)
print(contents2)

