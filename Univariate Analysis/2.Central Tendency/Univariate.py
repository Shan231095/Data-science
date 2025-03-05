class Univariate():
    def quanQual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            #print(columnName)
            if (dataset[columnName].dtype=='O'):
                #print('qual')
                qual.append(columnName)
            else:
                #print('quan')
                quan.append(columnName)
        return quan, qual

    def Findingoutlier_columnnames():
        lesser=[]
        greater=[]
        
        for columnname in quan:
            if (descriptive[columnname]["Min"]<descriptive[columnname]["Lesser"]):
                lesser.append(columnname)
            if (descriptive[columnname]["Max"]>descriptive[columnname]["Greater"]):
                greater.append(columnname)
        return lesser, greater

    def Replacing_outliers():
        for columnname in lesser:
            dataset[columnname][dataset[columnname]<descriptive[columnname]["Lesser"]]=descriptive[columnname]["Lesser"]
        for columnname in greater:
            dataset[columnname][dataset[columnname]>descriptive[columnname]["Greater"]]=descriptive[columnname]["Greater"]
        return dataset
        
    def Univariate(dataset,quan):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%",
                                        "Q4:100%","IQR","1.5rule","Lesser","Greater","Min","Max"],columns=quan)
        for columnname in quan:
            descriptive[columnname]["Mean"]=dataset[columnname].mean()
            descriptive[columnname]["Median"]=dataset[columnname].median()
            descriptive[columnname]["Mode"]=dataset[columnname].mode()[0]
            descriptive[columnname]["Q1:25%"]=dataset.describe()[columnname]["25%"]
            descriptive[columnname]["Q2:50%"]=dataset.describe()[columnname]["50%"]
            descriptive[columnname]["Q3:75%"]=dataset.describe()[columnname]["75%"]
            descriptive[columnname]["99%"]=np.percentile(dataset[columnname],99)
            descriptive[columnname]["Q4:100%"]=dataset.describe()[columnname]["max"]
            descriptive[columnname]["IQR"]=descriptive[columnname]["Q3:75%"]-descriptive[columnname]["Q1:25%"]
            descriptive[columnname]["1.5rule"]=1.5*descriptive[columnname]["IQR"]
            descriptive[columnname]["Lesser"]=descriptive[columnname]["Q1:25%"]-descriptive[columnname]["1.5rule"]
            descriptive[columnname]["Greater"]=descriptive[columnname]["Q3:75%"]+descriptive[columnname]["1.5rule"]
            descriptive[columnname]["Min"]=dataset[columnname].min()
            descriptive[columnname]["Max"]=dataset[columnname].max()
            descriptive[columnname]["kurtosis"]=dataset[columnname].kurtosis()
            descriptive[columnname]["skewness"]=dataset[columnname].skew()
            descriptive[columnname]["Var"]=dataset[columnname].var()
            descriptive[columnname]["Std"]=dataset[columnname].std()
        return descriptive

    def freqTable(columnname,dataset):
        freqTable=pd.DataFrame(columns=["Unique_values","Frequency","Relative_Frequency","Cumsum"])
        freqTable["Unique_values"]=dataset[columnname].value_counts().index
        freqTable["Frequency"]=dataset[columnname].value_counts().values
        freqTable["Relative_Frequency"]=(freqTable["Frequency"]/103)
        freqTable["Cumsum"]=freqTable["Relative_Frequency"].cumsum()
        return freqTable

    
        