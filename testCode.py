from numpy import add

students = [
        ('홍길동', 3.9),
        ('김철수', 3.0),
        ('최자영', 4.3),]
def appendNew():
    students.append(('손지원',5))


#sorted(students, key=lambda student: student[2])
appendNew()
sortresult = sorted(students, key=lambda percnet: percnet[1],reverse=True)

def sortNum(num,_array):
    resultArray = []
    for i in range(len(_array)):
        if(_array[i][1] > num):
            resultArray.append(_array[i])
    resultArray = sorted(resultArray, key=lambda percnet: percnet[1],reverse=True)
    print(resultArray)

sortNum(4.0,students)