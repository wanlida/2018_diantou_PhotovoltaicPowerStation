# 2018_diantou_PhotovoltaicPowerStation
电投_光伏电站人工智能运维大数据处理分析
[比赛链接](https://www.datafountain.cn/competitions/303/details)  
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

