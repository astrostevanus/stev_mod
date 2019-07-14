import os
import numpy as np
#molid=np.array(['46Ti-16O__Toto', '48Ti-16O__Toto', '50Ti-16O__Toto'])
molid=np.array(["23Na-1H__Rivlin", "27Al-16O__ATP", "40Ca-16O__VBATHY", "51V-16O__VOMYT","46Ti-16O__Toto", "47Ti-16O__Toto", "48Ti-16O__Toto", "49Ti-16O__Toto", "50Ti-16O__Toto"])
#molid=np.array(["48Ti-16O__Toto", "49Ti-16O__Toto", "50Ti-16O__Toto"])
for i in range(len(molid)):
    os.system('./heliosk -name kelt20b-2500K_'+str(molid[i])+' -T 2500 -P 0.01 -M '+str(molid[i])+' -numin 10000 -numax 30000 -path ./data/exomol/ -cut 1e8 -dnu 0.01')
