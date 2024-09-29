import os
import shutil

def move_files_to_parent(directory, exclude_folder):
    # 상위 폴더 내 모든 하위 폴더를 순회
    for root, subdirs, files in os.walk(directory, topdown=False):
        # venv_include 폴더를 제외
        if exclude_folder in root:
            continue

        # 현재 폴더에 있는 파일들을 상위 폴더로 이동
        for file in files:
            file_path = os.path.join(root, file)
            parent_dir = os.path.dirname(root)
            new_path = os.path.join(parent_dir, file)
            
            # 파일을 상위 디렉토리로 이동
            shutil.move(file_path, new_path)
            print(f"Moved: {file_path} -> {new_path}")
        
        # 파일을 이동한 후 하위 폴더가 비었으면 폴더 삭제
        if not os.listdir(root):
            os.rmdir(root)
            print(f"Deleted empty folder: {root}")

# 사용 예시
root_directory = "./"  # 파일을 상위 폴더로 이동할 루트 디렉토리 설정
exclude_folder_name = "venv_include"  # 제외할 폴더 이름 설정
move_files_to_parent(root_directory, exclude_folder_name)
