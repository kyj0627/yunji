""" import pandas as pd

df = pd.DataFrame([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]])

print(df)
print("\n=======================================\n")

print(df[1])
print("\n=======================================\n")

print(df[1][1])
print("\n=======================================\n")

print(df[2][2]) """

#dataframe 출력
""" import pandas as pd

data = {
    "x" : [10, 15, 20],
    "y" : [50, 55, 60],
    "z" : [100, 110, 120]
}

idx = ["x축", "y축", "z축"]

fr = pd.DataFrame(data, index=idx)

print(fr)
print("\n=======================================\n")

print(fr["x"])
print(fr["z"])

print(fr.x)
print("\n=======================================\n")
print(fr.y)

print(fr.iloc[1])

print("\n=======================================\n")
print(fr.loc["y축"])


#열 추가
print("\n=======================================\n")
frs = pd.DataFrame(fr,columns=["x", "y", "z", "t"])
frs["t"] = [60, 120, 180]

frs["t"] = [60,120,180]
print(frs)

#행 추가
print("\n=======================================\n")
frs.loc["t축"] = [100, 200, 300, 400]
print(frs)

#행 수정
print("\n=======================================\n")
frs.loc["t축"] = [500, 600, 700, 800]
print(frs)


#행 삭제
print("\n=======================================\n")
frs.drop("x", axis=1, inplace=True)
print(frs)

# 열 삭제
print("\n=======================================\n")
frs.drop("x축", inplace=True)
print(frs)
 """
 
#컬럼 추가
""" import pandas as pd

dt = [[1,10,100],[2,20,200],[3,30,300]]
col = ["x","y","z"]
idx = ["x축","y축","z축"]

df = pd.DataFrame(data=dt,index=idx,columns=col)
print(df)
print("\n=======================================\n")

print(df["x"])
print(df["y"])
print("\n=======================================\n")

print(df.loc["x축"])
print(df.loc["y축"])
print("\n=======================================\n")

#연산
print(df + 1)
print(df.div(100))
print(df / 100)
print("\n=======================================\n")
print(df.mul(100))
print(df*100)
print("\n=======================================\n")

#두 dataframe 간 연산
# 같은 인덱스끼리 연산
dt2  = [[0],[2],[3]]
df2 = pd.DataFrame(data=dt2,index=["x축","y축","z축"],columns=["y"])

print(df2)
print("\n=======================================\n")

print(df.div(df2))
print("\n=======================================\n")

print(df.div(df2, fill_value=100))
print("\n=======================================\n")"""



## 값바꿔서
""" import pandas as pd

dt = [[1,10,100],[2,20,200],[3,30,300]]
col = ["col1","col2","col3"]
idx = ["삼성","현대","LG"]

df = pd.DataFrame(data=dt,index=idx,columns=col)
print(df)
print("\n=======================================\n")

# print(df["col1"])
# print(df["y"])
print("\n=======================================\n")

print(df.loc["현대"])
# print(df.loc["y축"])
print("\n=======================================\n")

#연산
print(df + 1)
# print(df.div(100))
# print(df / 100)
# print("\n=======================================\n")
# print(df.mul(100))
# print(df*100)
print("\n=======================================\n")

#두 dataframe 간 연산
# 같은 인덱스끼리 연산
dt2  = [[0],[2],[3]]
df2 = pd.DataFrame(data=dt2,index=["삼성","현대","LG"],columns=["col2"])

print(df2)
print("\n=======================================\n")

print(df.div(df2))
print("\n=======================================\n")

print(df.div(df2, fill_value=100)) """

#멀티인덱스 
""" import pandas as pd

idx = [('row1', 'val1'), ('row1', 'val2'), ('row2', 'val1'), ('row2', 'val2'), ('row2', 'val3'), ('row3', 'val2'),('row3', 'val3')]
dt = [ [1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18], [19,20,21]]

ind = pd.MultiIndex.from_tuples(idx)
df = pd.DataFrame(dt, columns=['col1', 'col2', 'col3'], index = ind)

print(df)
print("\n=======================================\n")

print(df.loc["row1"])
# print(df.loc["row2"])
print("\n=======================================\n")

print(df.loc[("row3", "val3")])
print("\n=======================================\n")

print(df.loc[("row3", "val3"), "col1"])
print("\n=======================================\n") """


#랜덤 data 생성
""" import numpy as np
import pandas as pd

dt = np.random.randint(10, size=(5, 5))
df = pd.DataFrame(dt)

print(dt)
print("\n=======================================\n") 
print(df[2])

print("\n=======================================\n") 
print(df.loc[2])

print("\n=======================================\n") 
print(df.loc[3][1])

print("\n=======================================\n") 
print(df.head(2))

print("\n=======================================\n") 
print(df.tail(3)) 

print("\n=======================================\n") 
print(df.sample()) """

#파일 생성
from faker import Faker as fk
import os


temp = fk("ko-KR")
print(temp.name)

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
            temp.color_name() + "\n")
            
#파일 열기
import pandas as pd

folder = "data/"
target = folder + "fktemp.csv"

df = pd.read_csv(target)

# print(df)
# print(df.values[0])

#인덱스 설정 확인
# print(df.index)

# print(df.dtypes)

# print(type(df))


# print("\n=======================================\n") 
# df.head()

# print("\n=======================================\n") 
# df.head(3)

# print("\n=======================================\n") 
# df.tail()

# print("\n=======================================\n") 
# df.tail(3)

# print("\n=======================================\n") 
# print(df.sample())
# print(df.sample(4))

# print(df.values)

# print("\n=======================================\n") 
# print(df.values[24])
 
# for el in df.values[12] :
#     print(el)

# print(df.info())

# print(df.isnull())
# print(df.isnull().sum())

# print(df.name)
# print(df.postcode)
# print(df.job)
# print(df.phone)
# print(df.id)
# print(df.company)
# print(df.catch_parase)
# print(df.color)

# print(df["name"])
# print(df["color"])
# print(df["postcode"])
# print(df["phone"])
# print(df["id"])
# print(df["company"])

# print(df[["name","id"]])
# post = df[["name", "address","postcode"]]
# print(post)

# print(df.postcode.describe())
# print(df.color.describe())

# print(df.color.count())
# print(df.color.value_counts()) #중복값) 2 / 중복값x) 1

# temp = df.postcode.sum() / df.name.count()
# print(temp)

print(df.name == "강진우")
temp = df[df.color == "Gold"].head(1)
# temp = df[df.color == "Ivory"].head(2)
print(temp)
