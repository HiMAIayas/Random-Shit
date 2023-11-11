def permutation(s,strAns=[],index=0):
    strAnsCopied = [i for i in strAns]
    if index==0:
        strAnsCopied=[s[0]]
        index+=1

    strAnsCopied.append(s[index])
    for i in range(index+1):
        if index<len(s)-1:
            for j in permutation(s=s,strAns=strAnsCopied,index=index+1):
                yield j
        else:
            yield strAnsCopied
        strAnsCopied.append(strAnsCopied[0])
        strAnsCopied=strAnsCopied[1:]


def compute_normal(fournum:list,operatorList:list):
    index=1
    ans=fournum[0]
    for op in operatorList:
        if op=="+":ans+=fournum[index]
        elif op=="-":ans-=fournum[index]
        elif op=="*":ans*=fournum[index]
        else:
            if fournum[index]==0:ans=99999
            else:ans/=fournum[index]
        index+=1
    return ans

def compute_sp(fournum:list,opList:list,parenthesis=[0,0]):
    fournumCopied = [i for i in fournum]
    opListCopied = [i for i in opList]
    for i in parenthesis:
        fournumCopied[i+1]=compute_normal([fournumCopied[i],fournumCopied[i+1]],[opListCopied[i]])
        fournumCopied.pop(i)
        opListCopied.pop(i)
    ans=compute_normal(fournumCopied,opListCopied)
    if ans==24:
        fn=[str(i) for i in fournum]
        strAns=""
        if parenthesis==[0,0]:strAns="(("+fn[0]+opList[0]+fn[1]+")"+opList[1]+fn[2]+")"+opList[2]+fn[3]
        elif parenthesis==[0,1]:strAns="("+fn[0]+opList[0]+fn[1]+")"+opList[1]+"("+fn[2]+opList[2]+fn[3]+")"
        elif parenthesis==[1,0]:strAns="("+fn[0]+opList[0]+"("+fn[1]+opList[1]+fn[2]+"))"+opList[2]+fn[3]
        elif parenthesis==[1,1]:strAns=fn[0]+opList[0]+"(("+fn[1]+opList[1]+fn[2]+")"+opList[2]+fn[3]+")"
        elif parenthesis==[2,1]:strAns=fn[0]+opList[0]+"("+fn[1]+opList[1]+"("+fn[2]+opList[2]+fn[3]+"))"
        return strAns
    else:return None
    
    
numList = [int(i) for i in (input("Numbers: ").split())]
numListPermuted = permutation(s=numList)

opStock = ["+","-","*","/"]
opPermuted = [[i,j,k] for i in opStock for j in opStock for k in opStock]
ansList = list()
parenthesisList = [[0,0],
                   [0,1],
                   [1,0],
                   [1,1],
                   [2,1]]

for fournum in numListPermuted:
    for opList in opPermuted:
        if opList[0] in ["*","/"] or opList[1] in ["*","/"] or opList[2] in ["*","/"]:
            for parenthesis in parenthesisList:
                ansTemp=compute_sp(fournum,opList,parenthesis)
                if ansTemp!=None: ansList.append(ansTemp)
        else:
            IntansTemp=compute_normal(fournum,opList)
            if IntansTemp==24:
                ansList.append("(("+str(fournum[0])+opList[0]+str(fournum[1])+")"+opList[1]+str(fournum[2])+")"+opList[2]+str(fournum[3]))
            
SetAnsList=set(ansList)
for i in SetAnsList:
    print(i)