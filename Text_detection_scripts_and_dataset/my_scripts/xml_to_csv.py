import os,sys
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    print("xml_list - ",xml_list)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
#    for folder in ['train','test']:
#        image_path = os.path.join(os.getcwd(), ('text_images/text_xml' ))
        image_path = "/home/ashwini/TextDetection_MobilenetSSD/Text_dataset/MANUAL/xmls_19"
        print("image_path - ",image_path)
#	sys.exit()
        xml_df = xml_to_csv(image_path)
#        xml_df.to_csv(( folder + '_labels.csv'), index=None)
        xml_df.to_csv(( 'faulty19_labels.csv'), index=None)
        print('Successfully converted xml to csv.')


main()
