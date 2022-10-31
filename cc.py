from dis import pretty_flags
import json
from lib2to3.pgen2 import token 
import os
import shutil
from traceback import print_tb 
from PIL import Image
from numpy import append



# set your metefile sorce 
source_metadata = './output_v4.json'

# set go pic path  
Alist = []   # for 41 - 428 range(41,429)
Slist = []# for 429-440 range(429,441)

for x in os.listdir('./Kifu/A'):
    Alist.append('./Kifu/A/'+x)
for s in os.listdir('./Kifu/S'):
    Slist.append('./Kifu/S/'+s)

f = open(source_metadata, 'r', encoding='utf-8')
data = json.load(f) 
version_number = int (source_metadata.split('.')[1].split('_')[1][1:])




# this is progress bar 
def progress_bar(current, total, bar_length=100):
    fraction = current / total

    arrow = int(fraction * bar_length - 1) * '█' 
    padding = int(bar_length - len(arrow)) * ' '

    ending = '\n' if current == total else '\r'

    print(f'Progress: [{arrow}{padding}] {int(fraction*100)}%', end=ending)


# Add go id and go level in the metadata 
def addGoID(tokenId,goid,level):
    data[tokenId-1]['Go_id']=goid[9:]
    new = {
        "trait_type": "Level",
        "value": level
      }
    data[tokenId-1]['attributes'].append(new)


def pastego(file,gopic):
    img  = Image.open(gopic)
    a = img.resize((355,355))
    new_img = a.rotate(16.418,expand = True,fillcolor=(0,0,0,0))
    im2 = Image.open(file)
    im2.paste(new_img,(46,608),new_img)
    im2.save ('./FinalOutput/'+gopic[7:])


#--------- Main ---- Remember to update the go level and the range count 

startNumber = 41   #starting token ID
endNumber = 428  #ending token ID
level = 'A'
goidlist = Alist   # set Aslit to the gopic folder 

tokenList =range(startNumber,endNumber+1)
total =0

for count in tokenList:
    newname  ='./1-440 image/'+str(count)+'.png'
    goid= goidlist[count-startNumber]
    #pastego (newname,goid)
    addGoID(count,goid,level)
    total +=1
    progress_bar(total,len(tokenList))

print ('total process =', total )



# Save Json Output 
out_name = str(version_number+1)
with open('output_v'+out_name+'.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)








    

# for i in data:
#     picName = str(i['edition'])+'.png'
#     newName = i['attributes'][3]['value']
#     shutil.copy('./new1-40/'+picName,'./Foutput/'+newName)
#     i['attributes'].pop(3)
#     i['Go_id']=newName[:-4]
#     print(i)

# def paste(file,gopic):
#     im1  = Image.open(file)
#     im2 = Image.open(gopic)
#     im1.paste(im2,(0,0),im2)
#     im1.save ('./FinalOutput/'+gopic[7:])

