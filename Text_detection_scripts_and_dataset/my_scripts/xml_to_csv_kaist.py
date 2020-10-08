import os,sys
import glob
import pandas as pd
import xml.etree.ElementTree as ET

def parse_xml_folder(xmls_folder_path):
  xml_list = []
  for xml in os.listdir(xmls_folder_path):
    name = xml.split('.')[0]
    tree = ET.parse(os.path.join(xmls_folder_path + xml))
    root = tree.getroot() ###images

    for member in root:
      image_name = member.find('imageName').text

      if image_name.startswith('image'):		### DUE TO PROBLEM IN NAMES TO WRITE IN CSV.
        image_name = image_name.split("\\")[-1]
      #print(image_name)
  
      resolution_x = int(member.find('resolution').get('x'))
      resolution_y = int(member.find('resolution').get('y'))
      for ele in member.find('words'):
        print(image_name,ele.get('x'),ele.get('y'),ele.get('width'),ele.get('height'))
        xmin = int(ele.get('x'))
        ymin = int(ele.get('y'))
        xmax = int(ele.get('x')) + int(ele.get('width'))
        ymax = int(ele.get('y')) + int(ele.get('height'))

        value = (image_name,resolution_x,resolution_y,'text',xmin,ymin,xmax,ymax)
        xml_list.append(value)
      print("\n")
  
  return xml_list
     

print(' *** script started...!!!\n')

xmls_folder_path = '/home/ashwini/Downloads/Text_Detection_Dataset/KAIST/xmls/'

xml_list = parse_xml_folder(xmls_folder_path)
print("# Total instances : ",len(xml_list))
column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
xml_df = pd.DataFrame(xml_list, columns=column_name)

xml_df.to_csv('KAIST' + '_labels.csv', index=None)

print('\n *** script executed...!!!')

