reviewData = []
Keywords = ['응급실']

reviewData.clear()
reviewData.append(("응급실 다녀왔네요",80,"Noraml"))
reviewData.append(("임박 합니다",90,"Noraml"))
reviewData.append(("구토 했어요",90,"Noraml"))
reviewData.append(("장엽 입니다",90,"Noraml"))


for i in range(len(reviewData)):            
    print(any(keyword in reviewData[i][0] for keyword in Keywords))
    if(any(keyword in reviewData[i][0] for keyword in Keywords)==True):        
        temp = list(reviewData[i])
        temp[1] = 100
        reviewData[1] = temp

print(reviewData)