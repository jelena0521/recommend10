# 仅用于学习日记，不可用于任何商业用途
#基于地域和热度的排序
#1、初始化时预留地域和热度接口 self.addr=addr self.type=type1
#2、加载数据 并筛选出上面addr指定的数据
#3、进行推荐
#如果在关心单个因素 则按单个因素推荐，单个因素值相等时按价格从低到高，推荐前k个
#如果进行综合推荐 则需对所有数据按列做归一化 (data[col]-data[col].min())/(data[col].max()-data[col].min())
#对每列即每个type指定权重并相乘
#按照综合得分推荐前K个
#过滤出打印项目 data.filter(items=['name',self.type]).values)
#在main中指定区域和type
