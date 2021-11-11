from os import strerror

def fileMake():
    Negative_equal = open('../Negative_equal.txt', 'r',encoding='UTF8')
    Positive_equal = open('../Positive_equal.txt', 'r',encoding='UTF8')

    File_TrainNegative = open('../equalTrain/Negative.txt', 'at',encoding='UTF8')
    File_TrainPositive = open('../equalTrain/Positive.txt', 'at',encoding='UTF8')

    lines = Negative_equal.readlines()
    count =0
    for line in lines:    
        count+=1    
        strLine =line.replace("\t","")    
        strLine = strLine.replace("\n","")
        strLine = strLine.lstrip()
        strLine = str(count)+"\t"+strLine+"\t0\n"        
        File_TrainNegative.write(strLine)

    lines = Positive_equal.readlines()
    for line in lines:    
        count+=1    
        strLine =line.replace("\t","")    
        strLine = strLine.replace("\n","")
        strLine = strLine.lstrip()
        strLine = str(count)+"\t"+strLine+"\t1\n"    
        File_TrainPositive.write(strLine)

    File_TrainNegative.close()
    File_TrainPositive.close()
    Negative_equal.close()
    Positive_equal.close()
    
def main():
    Negative_equal = open('../Negative_equal.txt', 'r',encoding='UTF8')
    lines = Negative_equal.readlines()

    File_TrainNegative = open('../equalTrain/Negative.txt', 'at',encoding='UTF8')
    strtemp = lines[0]
    strLine =strtemp.replace("\t","")    
    strLine = strLine.lstrip()
    strtemp = "123"+"\t"+strLine+"\t0"
    print(strtemp)
    File_TrainNegative.write(strtemp)
    File_TrainNegative.close()

if __name__ == '__main__':
    #main()
    fileMake()