string = "(SILV907) MIN GRAND DR OREWA AUCKLAND. (XStr ARRAN DR/FLAVELL DR) .POLE DOWN ACROSS ROAD . #F3602623"

x = string.split()[1]

#print(x)
roadabbr = {'RD': 'ROAD',
            'AV': 'AVENUE',
            'PL': 'PLACE',
            'CL': 'CLOSE',
            'CT': 'COURT',
            'CR': 'CRESENT',
            'DR': 'DRIVE',
            'EXP': 'EXPRESSWAY',
            'HWY': 'HIGHWAY',
            'GR': 'GROVE',
            'HTS': 'HEIGHTS',
            'LN': 'LANE',
            'ST': 'STREET',
            'WAY': 'WAY',
            'TCE': 'TERRACE',
            'MWY': 'MOTORWAY',
            'PDE': 'PARADE',
            'CNR': 'CORNER',
            'ESP': 'ESPLANADE',
            }

for key, value in roadabbr.items():
    string = string.replace(key, value)
    
print(string)