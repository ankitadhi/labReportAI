def makeGraphWithWeight():


    G = {'Biratnagar': {'Rangeli': 25, 'Itahari': 22,'Biratchowk': 30},
                    
         'Rangeli': {'Biratnagar': 25,'Kanepokhari': 25,'Urlabari': 40},
                    
        'Itahari':{'Biratnagar':22,'Biratchowk':11,'Dharan':30},
    
        'Dharan':{'Itahari':22,},
    
        'Biratchowk':{'Biratnagar':30,'Itahari':11,'Kanepokhari':10},
    
        'Kanepokhari': {'Rangeli':25,'Biratchowk':10, 'Urlabari':12},
    
        'Urlabari': {'Rangeli':40,'Kanepokhari':12, 'Damak':6},
    
        'Damak': {'Urlabari':6,},
                
        }
    return G

graph = makeGraphWithWeight()
print(graph['Biratnagar'])