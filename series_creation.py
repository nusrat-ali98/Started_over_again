import pandas as pd


student = pd.Series([80,48,99,12,10] , index=["Alice","Anwar","Nusrat","Bilal","Talib"])
print(f"{student}\n")


avg_marks = student.mean()
print(f"average marks:\n{avg_marks}\n ")


bouns_marks = student * 1.1
print("Bouns marks:\n", bouns_marks)
print("\n")

data_obv_60 = student[student > 60]
print("Student whose marks are above: \n", data_obv_60)