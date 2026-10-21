import pandas as pd
df= pd.read_csv("can_log.csv")
print("形状:",df.shape)
print("列名:",df.columns.tolist())
print("\n前5行：")
print(df.head())
print("\n前10行:")
print(df.head(10))\
#选择列
cols = ["timestamp","can_id","data","dlc"]
df_sel = df[cols]
print(df_sel.head())
print(df_sel.shape)
#条件筛选
#1.筛选指定cam_id
df_filter1 = df_sel[df_sel["can_id"].isin(["0x0c9","0x18F"])]
print(df_filter1.head())
print("筛选后行数：",len(df_filter1))
#2.筛选dlc=8
df_filter2 = df_sel[df_sel["dlc"] == 8]
print(df_filter2.head())
print("dlc=8 行数:", len(df_filter2))
#3.筛选时间范围
df_filter3 = df_sel[(df_sel["timestamp"] >= 1.0)&(df_sel["timestamp"]<=5.0)]
print(df_filter3.head())
print("1-5秒行数:",len(df_filter3))
#按can_id计数并排序
count_by_id = df_sel["can_id"].value_counts()
print("按 can_id 计数：")
print(count_by_id)

count_sorted = df_sel.groupby("can_id").size().sort_values(ascending=False)
print("\ngroupby 计数并降序:")
print(count_sorted)

print("\nTop3 :")
print(count_sorted.head(3))
