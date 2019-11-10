volume_global = 22_810 #volume in km3
area_global = 8_080_454.3 #area in km2

def calculate_dept(volume_local, area_local):
    ''' take at volume and area return dept'''

    ##claculate dept
    height_local = volume_local /area_local
    return round(height_local,4)

h = calculate_dept(volume_global, area_global)

##display result
print('the dept will be',h,'km')
