import pandas as pd
import os

def get_info(name):
    temp = pd.read_csv(r"../Capstone temp/temperature.csv")
    ids = pd.read_csv(r"../Capstone Data/ids.csv")

    last,first,id = "unknown","unknown","unknown"
    i = 0
    for item in ids['Last Name']:
        if (name == ids['First Name'][i].lower() + '_' + item.lower()):
            id = str(ids['ID'][i])
            last = name.split('_')[1].capitalize()
            first = name.split('_')[0].capitalize()
        i += 1
        
    data = pd.DataFrame({
                        'Date':[temp['Date'].iloc[-1]],
                        'Time':[temp['Time'].iloc[-1]],
                        'Last Name': [last], 
                        'First Name': [first],
                        'ID':[id],
                        'Temperature':[temp['Temperature'].iloc[-1]],
                        'Photo':['images/'+id+'.jpg']
                        })
    
    os.remove(r"../Capstone temp/temperature.csv")
    return data, id

def get_occ():
    temp = pd.read_csv(r"../Capstone temp/occupancy.csv")
    temp['Final occupancy'] = ''
    temp['Final occupancy'].iloc[0] = str(int(temp[temp.columns[2]].iloc[-1])) 
    temp.to_csv(r'C:/inetpub/wwwroot/occupancy.csv',index=False)
    os.remove(r"../Capstone temp/occupancy.csv")