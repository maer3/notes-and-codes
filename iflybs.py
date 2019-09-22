import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab
import dask.dataframe as dd
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn import model_selection,linear_model
from sklearn.decomposition import IncrementalPCA
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns


#显示中文 
pylab.mpl.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['font.sans-serif']=['SimHei']  # 用来正常显示中文标签  
plt.rcParams['axes.unicode_minus']=False  # 用来正常显示负号

#读取csv文件
f=pd.read_table(r'C:\Users\24218\python files\iflytek\traindata.txt')
test=pd.read_table(r'C:\Users\24218\python files\iflytek\testdata_feature.txt')

'''
#####################################
print(np.array(f).shape) ##查看形状

#pkgname
     
len(f['pkgname'].unique()) ##查看数据多少
f.groupby(['pkgname']).size()['empty']#查看空值
f['pkgname'].value_counts()#查看出现次数

#ver
len(f['ver'].unique()) ##查看数据多少
f['ver'].isnull().sum()#查看空值
f['ver'].value_counts()#查看出现次数

#adunitshowid
len(f['adunitshowid'].unique()) ##查看数据多少
f.groupby(['adunitshowid']).size()['empty']#查看空值
f['adunitshowid'].value_counts()#查看出现次数
a=f[f['adunitshowid'].isin(['empty']).astype("bool")].head(100) ##查看adunitshouid下空值时，整个数据的情况

#mediashowid
len(f['mediashowid'].unique()) ##查看数据多少
f.groupby(['mediashowid']).size()['empty']#查看空值
f['mediashowid'].value_counts()#查看出现次数

#apptype
len(f['apptype'].unique()) ##查看数据多少
f.groupby(['apptype']).size()[-1]#查看空值
f['apptype'].value_counts()#查看出现次数

#ip
len(f['ip'].unique()) ##查看数据多少
f['ip'].isnull().sum()#查看空值
f['ip'].value_counts()#查看出现次数

#city
len(f['city'].unique()) ##查看数据多少
f['city'].isnull().sum()#查看空值
f['city'].value_counts()#查看出现次数

#province
len(f['province'].unique()) ##查看数据多少
f.groupby(['province']).size()[-1]#查看空值
f['province'].value_counts()#查看出现次数

#reqrealip
len(f['reqrealip'].unique()) ##查看数据多少
f['reqrealip'].isnull().sum()#查看空值
f['reqrealip'].value_counts()#查看出现次数

#adidmd5 
len(f['adidmd5'].unique()) ##查看数据多少
f.groupby(['adidmd5']).size()['empty']#查看空值
f['adidmd5'].value_counts()#查看出现次数

#imeimd5
len(f['imeimd5'].unique()) ##查看数据多少
f.groupby(['imeimd5']).size()['empty']#查看空值
f['imeimd5'].value_counts()#查看出现次数

#idfamd5
len(f['idfamd5'].unique()) ##查看数据多少
f.groupby(['idfamd5']).size()['empty']#查看空值
f['idfamd5'].value_counts()#查看出现次数

#openudidmd5
len(f['openudidmd5'].unique()) ##查看数据多少
f.groupby(['openudidmd5']).size()['empty']#查看空值
f['openudidmd5'].value_counts()#查看出现次数

#macmd5
len(f['macmd5'].unique()) ##查看数据多少
f.groupby(['macmd5']).size()['empty']#查看空值
f['macmd5'].value_counts()#查看出现次数

#dvctype
len(f['dvctype'].unique()) ##查看数据多少
f['dvctype'].value_counts()#查看出现次数

#model
len(f['model'].unique()) ##查看数据多少
f['model'].isnull().sum()#查看空值
f['model'].value_counts()#查看出现次数

#make
len(f['make'].unique()) ##查看数据多少
f['make'].isnull().sum()#查看空值
f['make'].value_counts()#查看出现次数
 
#f.isnull().sum()    ##查看空值
#pd.value_counts(f['city'])

####################################################
'''
#plt.subplots(figsize=(10,8))
#sns.distplot(
#sns.barplot(x=f['ip'],y=f['label'])







#特征工程

def chuli(f): 
    
    f['ip'] = f['ip'].replace('.','')
    f['ip_city'] = int(f['ip']) // 100
    f['ip_city'] = pd.Categorical(f['ip_city']).codes


    df = f.drop(['city','province','os','openudidmd5'], axis=1)
  
#    df['openudidmd5'].loc[df['openudidmd5'] != 'empty'] = 1  
 #   df['openudidmd5'].loc[df['openudidmd5'] == 'empty'] = 0


    df['pkgname'] = pd.Categorical(df['pkgname']).codes
    df['ver'] = pd.Categorical(df['ver']).codes
    df['adunitshowid'] = pd.Categorical(df['adunitshowid']).codes
    df['mediashowid'] = pd.Categorical(df['mediashowid']).codes
    df['apptype'] = pd.Categorical(df['apptype']).codes
    df['ip'] = pd.Categorical(df['ip']).codes
    df['reqrealip'] = pd.Categorical(df['reqrealip']).codes
    df['adidmd5'] = pd.Categorical(df['adidmd5']).codes
    df['imeimd5'] = pd.Categorical(df['imeimd5']).codes
    df['macmd5'] = pd.Categorical(df['macmd5']).codes
    df['dvctype'] = pd.Categorical(df['dvctype']).codes
    df['model'] = pd.Categorical(df['model']).codes
    df['make'] = pd.Categorical(df['make']).codes
    df['osv'] = df['osv'].fillna(df['osv'].mode())
    df['osv'] = pd.Categorical(df['osv']).codes
    df['lan'].loc[df['lan'] != 'cn']=1
    df['lan'].loc[df['lan'] == 'cn']=0
    df['carrier'] = pd.Categorical(df['carrier']).codes
    df['h'] = pd.Categorical(df['h']).codes  
    df['w'] = pd.Categorical(df['w']).codes  
    df['idfamd5'].loc[df['idfamd5'] != 'empty'] = 1  
    df['idfamd5'].loc[df['idfamd5'] == 'empty'] = 0
    df['orientation'] = pd.Categorical(df['orientation']).codes 
    df['nginxtime'] = pd.Categorical(df['nginxtime']).codes  
    
    return df

######################

#模型
y_train = f['label']
f = f.drop(['label','sid'],axis=1)

test_sid = test['sid']
test_nosid = test.drop(['sid'],axis=1)

train_all = pd.concat([f,test_nosid],axis = 0)

train_all = chuli(train_all)

x_train = train_all[0:1000000]
test_nosid = train_all[1000000:1100000]
test = pd.concat([test_sid,test_nosid],axis = 1)


#x_train = x_train.drop(['ip','adidmd5'],axis=1)

train1,test1,train2,test2=model_selection.train_test_split(x_train,y_train,test_size=0.01,random_state=0,stratify=y_train)
#逻辑回归

#regr = linear_model.LogisticRegression()
#regr.fit(train1,train2)


#随机森林
clf = RandomForestClassifier(n_estimators=18,max_depth=20,min_samples_split=6)
clf.fit(train1,train2)



#knn
#knn = KNeighborsClassifier(n_neighbors=5)

#xgboost
#xg = XGBClassifier()


#xg.fit(train1,train2)


print('Score:%f'%clf.score(train1,train2)) 
#print('Score:%.2f'%knn.score(test1,test2)) 
fpr,tpr,thresholds = metrics.roc_curve(test2,clf.predict(test1),pos_label=1)
print(metrics.auc(fpr,tpr))

###########
#结果
#test = chuli(test)
jieguo = test['sid']
test = test.drop(['sid'],axis= 1)

result = clf.predict(test)

result = pd.DataFrame(result,columns=['label'])

jieguo = pd.concat([jieguo,result],axis = 1)

jieguo.to_csv(r"C:\Users\24218\python files\iflytek\result10.csv",index = None)

