#9-2 데이터 처리

""" from faker import Faker as fk
import os

temp = fk("ko-KR")
print(temp.name())

folder = "data/"
if not os.path.isdir(folder):
    os.mkdir(folder)
    
with open(folder + "fktemp.csv", "w", encoding='utf8') as f :
    f.write("name,address,postcode,company,job,phone,email,id,ip_prv,ip_pub,catch_parase,color\n")

with open(folder + "fktemp.csv", "a", newline='', encoding='utf8') as f :
    for i in range(30) :
            f.write(temp.name() + "," + 
            temp.address() + "," + 
            temp.postcode() + "," + 
            temp.company() + "," + 
            temp.job() + "," + 
            temp.phone_number() + "," + 
            temp.email() + "," + 
            temp.user_name() + "," + 
            temp.ipv4_private() + "," + 
            temp.ipv4_public() + "," + 
            temp.catch_phrase() + "," + 
            temp.color_name() + "\n")  """

import pandas as pd


folder = "data/"
target = folder + "fktemp.csv"

df = pd.read_csv(target)

""" #rank 매기기
df["ever"] = df.postcode.rank(method="average")
#print(df[["postcode", "ever"]])

df["dense"] = df.postcode.rank(method="dense")
#print(df[["postcode", "dense"]])

df["first"] = df.postcode.rank(method="first")
#print(df[["postcode", "first"]])

df["min"] = df.postcode.rank(method="min")
#print(df[["postcode", "min"]])

df["min"] = df.postcode.rank(method="min")
#print(df[["postcode", "min"]])

df["max"] = df.postcode.rank(method="max", ascending=False)
#print(df[["postcode", "max"]])

print(df[["postcode", "max", "min", "first", "dense", "ever"]])

#전처 컬럼, 로우 반환
print(df.transpose())

#누적 계산
print(df["postcode"].expanding().sum())
print(df["postcode"].expanding()) """

#내림차순 기준x
# print(df.postcode.idxmax(axis=0)) #가장 작은수
# print(df.postcode.idxmin(axis=0)) #가장 큰수

#empty 추가
# print(df.empty())
# print(df.company.empty())

#검색
""" print(df.isin([10221]))
print(df.isin(["김상호"]))

print(df.isin([48653, 64255]))

print(df.isin([48742,97162,"김은지"])) """

#기간 계산
""" period = pd.period_range(start="2023-11-10 00:00:00", end="2023-11-10 02:30:00", freq="30T")
dt = {"col1":[1,2,3,4,5,6],"col2":period}
idx = ["row1","row2","row3","row4","row5","row6"]
pf = pd.DataFrame(data=dt, index=idx)
print(pf) """

#인덱스 시간 - 간격 생성
""" # i = pd.date_range("2023-11-10", periods=10, freq="1H")
i = pd.date_range("2023-11-10", periods=10, freq="3H")
df = pd.DataFrame({"col1":[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df) """

print("\n=================================\n")
#특정 시간 찾기
""" print(df.at_time("09:00"))
print(df.at_time("03:00"))
 """
#범위 찾기
""" print(df.between_time(start_time="12:00", end_time="00:00"))

print(df.between_time(start_time="03:00", end_time="09:00"))
 """
#시간 간격 데이터 생성
""" # i = pd.date_range("2023-11-10", periods=10, freq="3D")
i = pd.date_range("2023-11-10", periods=10, freq="5D")
df = pd.DataFrame({'col1':[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)

print(df.first("5D"))

print(df.first("7D"))

print(df.last("7D")) """
          
                             
#데이터처리 활용
import FinanceDataReader as fdr

ksp = fdr.DataReader("KS11", "2023")
print(ksp)
print("\n===========================\n")

#최고가 확인    
""" print(ksp["High"].max())
print("\n===========================\n")
print(ksp["High"].idxmax())
print("\n===========================\n") """

#최저가 확인
""" print(ksp["Low"].min())
print("\n===========================\n")
print(ksp["Low"].idxmin())
print("\n===========================\n") """

#최고가 값 찾기
""" print(ksp["Volume"].nlargest(n=5))
print("\n===========================\n") """

#최저가 값 찾기
""" print(ksp["Volume"].nsmallest(n=5))
print("\n===========================\n") """

#kospi 3000 달성 최초일 찾기
""" #cond = ksp["Close"] >= 3000
cond = ksp["Close"] >= 2000
res = ksp[cond].index[0]
print(res) """

#위 값 참조 처리
""" res = ksp["Volume"] > ksp["Volume"].shift()
print(res)
print("\n========================================\n") """

# res = ksp["up"] != ksp["up"].shift().cumsum()
# print(res)
# print("\n========================================\n")

""" ksp["grp"] = ksp["up"] != ksp["up"].shift().cumsum()
print(ksp) """

""" ksp["up_cnt"] = ksp["grp"].groupby(ksp["grp"].values).cumcount() + 1
print(ksp) """

# print(ksp["up_cnt"].max())

#변환
import pandas as pd

""" target = "./data/apt.csv"
df = pd.read_csv(target, encoding="CP949")
df.to_csv("./data/conv_apt.csv",encoding="utf8")

print(df.head()) """

""" df = pd.read_csv("./data/conv_apt.csv", index_col=0)
# df = pd.read_csv("./data/apt.csv", index_col=0)
print(df.head()) """

#컬럼명 바꾸기
""" df = df.rename(columns={"분양가격(제곱미터)":"분양가"})
print(df)
print(df.dtypes) """

#컬럼 타입변경
""" df["분양가"] = df["분양가"].convert_dtypes()
print(df.dtypes) """

#array 변환
""" arr = df.to_numpy()
print(arr)
print(arr[2])
print(len(arr)) """

#요약정보
# print(df.describe())

#축변환
""" print(df.transpose())
print("\n============================================\n")
print(df.T.head()) """
