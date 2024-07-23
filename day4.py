import matplotlib.pyplot as plt
import streamlit as st
#randint 함수를 이용해 10개의 정수를 가지는 리스트를 작성
#그 리스트를 plt.plot()에 인자로 넘겨줘 봅시다.
#리스트 2개 작성 : range() 함수로 나온 변수를 list 로 강제 형변환
#list()
#치아 파일에서 데이터를 가공

#plt.plot(x)
#plt.bar()
#   파일을 열고
f = open("C:/Users/DSU/Desktop/치아.txt")
#   파일을 읽고
str = f.read()
#   포멧에 맞게 split() 하고
splittedStr = str.split("\n")
#   클래스를 제작해서
class dataClass:
    def __init__(self,id,age,gender,psu,edu,dt):
        self.id = id
        self.age = age
        self.gender = gender
        self.psu = psu
        self.edu = edu
        self.dt = dt
#   정렬
#        비어있는 값에 대해 예외처리
index = 0
dataLst = []
for i in splittedStr:
    tmpDat = i.split("\t")
    if index != 0:
        #tmpCl = dataClass(tmpDat[0], tmpDat[1],tmpDat[2],tmpDat[3],tmpDat[4],tmpDat[5])
        #dataLst.append(tmpCl)
        tf = False
        for j in tmpDat:
            if j == '':
                tf = True
            #j 중에 비어있는 값이 있다면 건너뛰기
        if tf == False:
            id = int(tmpDat[0])
            age = int(tmpDat[1])
            gender = int(tmpDat[2])
            psu = int(tmpDat[3])
            edu = int(tmpDat[4])
            dt = int(tmpDat[5])
            tmpCl = dataClass(id,age,gender,psu,edu,dt)
            dataLst.append(tmpCl)
    index += 1
print(len(dataLst),"개 데이터")

ageDic = {}
for i in range(0,100):
    for j in dataLst:
        keyExist = False
        for k in ageDic.keys():
            if k == i:
                keyExist = True
                break
        if(j.age == i):
            if keyExist == True:
                ageDic[i] += 1
            else:
                ageDic[i] = 1
print(ageDic)
fig = plt.bar(ageDic.keys(), ageDic.values())
st.pyplot(plt.gcf())