import os
import shutil

def move_files_to_target(folders, target_folder):
    # 폴더 리스트에 있는 각 폴더 순회
    for folder in folders:
        # 각 폴더 내의 파일들을 순회
        for root, dirs, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                target_path = os.path.join(target_folder, file)
                
                # 파일을 타겟 폴더로 이동
                shutil.move(file_path, target_path)
                print(f"Moved: {file_path} -> {target_path}")

# 사용 예시
folder_list = ['./[원천]2.음성수집도구_5']  # 파일들을 옮길 폴더 리스트
target_directory = './[원천]2.음성수집도구'  # 모든 파일들을 옮길 타겟 폴더

# 타겟 폴더가 없으면 생성
if not os.path.exists(target_directory):
    os.makedirs(target_directory)

move_files_to_target(folder_list, target_directory)
