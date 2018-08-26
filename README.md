# 2018_diantou_PhotovoltaicPowerStation
[电投_光伏电站人工智能运维大数据处理分析：比赛链接](https://www.datafountain.cn/competitions/303/details)  
团队成员：  
[@jlinbb](https://github.com/jlinbb)  
[@wanlida](https://github.com/wanlida)  
[@ouc16020021031](https://github.com/ouc16020021031)  
[@Troysps](https://github.com/Troysps)  

# 最好的版本    
|                 location                        | score           | rank | detail                       |
| ----------------------------------------------- | --------------- | --- | ---------------------          |
|    McDonald/McDonald_v4.ipynb                   |  0.84609425068  | 30  |一个完整的版本1.数据预处理 2.第一层xgboost gbdt rf lgbm knn 五个模型融合  3.第二层模型融合选择SVR|
| code_version_save/wan_8月4号22点11分.ipynb       |  0.84751743     | 22  | 增加一个强特 历史平均功率，knn模型不太好，选择xgboost gbdt rf lgbm四个模型，测试过单独增加列 用ID%205 没有效果，分数反而降低至0.846
| code_version_save/wan_8月16号  0.84770610000.ipynb | 0.84770610000 | * | 增加四列 历史平均功率 历史功率A 历史功率B 历史功率C


# 比赛的详细细节 detail_1.png
![image](https://github.com/wanlida/2018_diantou_PhotovoltaicPowerStation/raw/master/pictures/competition.png)      
![image](https://github.com/wanlida/2018_diantou_PhotovoltaicPowerStation/raw/master/pictures/detail_1.png)   
![image](https://github.com/wanlida/2018_diantou_PhotovoltaicPowerStation/raw/master/pictures/detail_2.png)     
## a榜排名  
![image](https://github.com/wanlida/2018_diantou_PhotovoltaicPowerStation/raw/master/pictures/rank.png)
## b榜排名
![image](https://github.com/wanlida/2018_diantou_PhotovoltaicPowerStation/raw/master/pictures/end_rank.png)
## 备注
保密工作没有做好，很多队伍在github上检索到了我们的代码，已知的某队伍，部分使用我们的代码最终B榜11名
需要在github上使用英文书写相关信息
对于特征处理方面没有做好，暴力特征+特征选择 初赛A榜预计能到 前10
A榜过拟合比较严重
## 向大佬咨询的强特

![image](https://github.com/wanlida/2018_diantou_PhotovoltaicPowerStation/raw/master/pictures/cat.png)  

XX选用的模型是 xgboost gbdt catboost lgbm，我也试了试catboost 感觉使用很不熟练，a榜分数也不高，主要是catboost ；类别型特征需要特殊处理  

![image](https://github.com/wanlida/2018_diantou_PhotovoltaicPowerStation/raw/master/pictures/catboost.png)

![image](https://github.com/wanlida/2018_diantou_PhotovoltaicPowerStation/raw/master/pictures/xgboost.png)

![image](https://github.com/wanlida/2018_diantou_PhotovoltaicPowerStation/raw/master/pictures/强特.png)
