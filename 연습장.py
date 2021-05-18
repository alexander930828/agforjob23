array = [("carry", 2), ("amy", 3), ("ben", 1)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
#sort 와 sorted 함수의 가장 큰 차이점은 sort 함수는 원래의 데이터에서 내부 변화를 만들어주는것이고
#sorted 함수는 정렬한 새로운리스트를 만들어주는 것이다 튜플일 경우에는 변형이 불가능하기 때문에,

print(result)