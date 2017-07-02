from queryDBfunction import qDB
import time


# 146032.645002 28527.4682605
# 146032.645002 31318.6662764
# 149239.000971 31318.6662764
# 149239.000971 28527.4682605
# 146032.645002 28527.4682605

# run with lat long coordinates


# lat1 = '31300'
# lon1 = '149000'

lat2 = '28500'
lon2 = '146000'

# lat1 = str(int(lat2)+499)
# lon1 = str(int(lon2)+499)

# lat1 = str(int(lat2)+999)
# lon1 = str(int(lon2)+999)

# lat1 = str(int(lat2)+1499)
# lon1 = str(int(lon2)+1499)

# lat1 = str(int(lat2)+1999)
# lon1 = str(int(lon2)+1999)

# lat1 = str(int(lat2)+2499)
# lon1 = str(int(lon2)+2499)

lat1 = str(int(lat2)+3999)
lon1 = str(int(lon2)+3999)

ll = lon2 + ' ' + lat2
ul = lon2 + ' ' + lat1
ur = lon1 + ' ' + lat1
lr = lon1 + ' ' + lat2

# spacingval_array = [1,3,5,10] #3 (4seconds)
# spacingval_array = [5,7,10,15] #8 (4seconds)
# spacingval_array = [18,19,20,21] #19 (4seconds)
# spacingval_array = [38,39,40,43,45,50] #40 (4seconds)
# spacingval_array = [38,39,40,43,45,50] #50 (4seconds)
# spacingval_array = [85,90,95,100,105,110] #100 (4seconds)
# spacingval_array = [120,140,160] #140 (4seconds)
spacingval_array = [180,185,190,200] #140 (4seconds)


tArray = []

for spacingval in spacingval_array:
	print 'spacingval = '+ str(spacingval)
	t = time.time()
	qDB(ll,ul,ur,lr,ll,spacingval)
	elapsed = time.time() - t
	print type(elapsed)
	tArray.append(elapsed)

print tArray
print type(tArray)
print spacingval_array
print type(spacingval_array)

import matplotlib.pyplot as plt
plt.close('all')

fig = plt.figure()
plt.scatter(spacingval_array,tArray)
plt.show()

exit()
