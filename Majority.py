listtest = [1,4,5,5,5,1,5]

def majority():
    listtest.sort()
    major = len(listtest)//2
    countmajor = 0
    for i in listtest :
        if i == listtest[major] :
            countmajor +=1

    if countmajor >= major:
        print('majority')
    else:
        print('no majority')


majority()