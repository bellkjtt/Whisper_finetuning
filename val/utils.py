import os
import pandas as pd
import json
from tqdm import tqdm

# 루트 폴더 경로
root_folder = "./"

# 라벨 폴더들을 순회하며 진행 상황 표시
label_folders = [folder for folder in os.listdir(root_folder) if os.path.isdir(os.path.join(root_folder, folder))]
print(label_folders)
# 라벨 폴더 루프
for label_folder in tqdm(label_folders, desc="Processing Label Folders"):
    label_path = os.path.join(root_folder, label_folder)
    
    # 해당 라벨 폴더 안의 모든 하위 폴더 탐색
    sub_folders = [sub for sub in os.listdir(label_path) if os.path.isdir(os.path.join(label_path, sub))]
    
    # 하위 폴더 루프
    for sub_folder in tqdm(sub_folders, desc=f"Processing Subfolders in {label_folder}", leave=False):
        sub_folder_path = os.path.join(label_path, sub_folder)
        
        # 하위 폴더 내 JSON 파일들 탐색
        json_files = [file for file in os.listdir(sub_folder_path) if file.endswith('.json')]
        
        # JSON 파일 루프
        for file_name in tqdm(json_files, desc=f"Processing JSON files in {sub_folder}", leave=False):
            json_file_path = os.path.join(sub_folder_path, file_name)

            # JSON 파일 열기
            with open(json_file_path, 'r', encoding='utf-8') as file:
                data_dic = json.load(file)

            # 평면 구조로 변환 (발화정보, 대화정보, 녹음자정보)
            flattened_data = {}
            flattened_data.update(data_dic['발화정보'])
            flattened_data.update(data_dic['대화정보'])
            flattened_data.update(data_dic['녹음자정보'])

            # DataFrame으로 변환
            data_df = pd.DataFrame([flattened_data])

            # CSV 파일로 저장할 파일명 만들기
            csv_file_name = file_name.split('.')[:-1]
            csv_file_name = ''.join(csv_file_name) + '.csv'

            # 각 라벨별로 CSV 파일을 저장할 디렉토리 생성 (필요시)
            csv_output_folder = os.path.join(root_folder, label_folder, "csv_output")
            if not os.path.exists(csv_output_folder):
                os.makedirs(csv_output_folder)
            
            # CSV 파일 경로 생성
            csv_file_path = os.path.join(csv_output_folder, csv_file_name)

            # CSV로 저장
            data_df.to_csv(csv_file_path, index=False, header=True, encoding='utf-8-sig')

            print(f"Saved CSV: {csv_file_path}")
