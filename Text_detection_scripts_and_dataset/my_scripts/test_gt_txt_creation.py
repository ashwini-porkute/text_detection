import sys,os
import cv2
import csv

dest_op_folder = "/home/ashwini/TextDetection_MobilenetSSD/Final_Text_Dataset/test_txt_anno_gt/"
test_csv_to_read = "/home/ashwini/TextDetection_MobilenetSSD/Final_Text_Dataset/test_labels.csv"
image_dir = "/home/ashwini/TextDetection_MobilenetSSD/Final_Text_Dataset/test"


def read_csv(csv_file_path, search_with_image_name):
  with open(csv_file_path) as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    fields = []

    for row in data:    
      if row[0] == search_with_image_name :
        field = (row[3], int(row[4]), int(row[5]), int(row[6]), int(row[7]))
        fields.append(field)
  return fields

for image in os.listdir(image_dir):
  txt_file_name = image.split('.')[0] + ".txt"
  txt_file_loc = os.path.join(dest_op_folder + txt_file_name)

  fields = read_csv(test_csv_to_read,image)

  with open(txt_file_loc, "w") as fd:
    for field in fields:
      line = ""
      line = str(field[0]) + " " + str(field[1]) + " " +  str(field[2]) + " " + str(field[3]) + " " + str(field[4]) + "\n"
      #print("line - ",line)
      fd.write(line)


