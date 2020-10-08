import pandas as pd
import csv
import glob
import os
path = '/home/ashwini/TextDetection_MobilenetSSD/Text_dataset/csvs'
files_in_dir = [f for f in os.listdir(path) if f.endswith('csv')]
for filenames in files_in_dir:
  #df = pd.read_csv(filenames)
  df = pd.read_csv(os.path.join(path,filenames))
  df.to_csv('merged_svt_kaist_with_corrected_faulty12.csv', mode='a')
