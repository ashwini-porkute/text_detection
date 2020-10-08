import sys
import os
import csv

test_img_dir = "/home/ashwini/TextDetection_MobilenetSSD/Final_Text_Dataset/test"
test_img_list = os.listdir(test_img_dir)
test_csv_to_read = "/home/ashwini/TextDetection_MobilenetSSD/Final_Text_Dataset/Final_mixed.csv"

train_ph1_img_dir = "/home/ashwini/TextDetection_MobilenetSSD/Final_Text_Dataset/train_Ph1"
train_ph1_img_list = os.listdir(train_ph1_img_dir)
train_ph1_csv_to_read = "/home/ashwini/TextDetection_MobilenetSSD/Final_Text_Dataset/Final_mixed.csv"

train_ph2_img_dir = "/home/ashwini/TextDetection_MobilenetSSD/Final_Text_Dataset/train_Ph2"
train_ph2_img_list = os.listdir(train_ph2_img_dir)
train_ph2_csv_to_read = "/home/ashwini/TextDetection_MobilenetSSD/Final_Text_Dataset/Final_mixed.csv"

column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']

def bboxes_from_csv(train_ph2_csv_to_read, search_with_image_name):
  with open(train_ph2_csv_to_read) as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    fields = []
    field = []
 
    for row in data:    
      if row[0] == search_with_image_name :
        field = [row[0], int(row[1]), int(row[2]), 'text' ,int(row[4]), int(row[5]), int(row[6]), int(row[7])]
        fields.append(field)
  return fields


with open('train_Ph2_labels.csv', 'a') as f:
  writer = csv.writer(f)
  writer.writerow(column_name)

  for image in train_ph2_img_list :
    #print(image)
    #sys.exit()

    fields = bboxes_from_csv(train_ph2_csv_to_read, image) 

    for field in fields:
      writer.writerow(field)

print("Done...!!!")
