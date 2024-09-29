import os

def count_files_in_folder(directory):
    file_count = 0
    # 디렉토리 내의 모든 파일과 폴더를 순회
    for root, dirs, files in os.walk(directory):
        # 현재 폴더에 있는 파일의 수를 계산
        file_count += len(files)
    
    return file_count

def count_files_in_multiple_folders(parent_directory):
    # 상위 폴더 내 모든 하위 폴더를 순회
    for folder in os.listdir(parent_directory):
        folder_path = os.path.join(parent_directory, folder)
        # 폴더인 경우에만 파일 개수 세기
        if os.path.isdir(folder_path):
            file_count = count_files_in_folder(folder_path)
            print(f"Folder '{folder}' contains {file_count} files.")

# 사용 예시
parent_directory = "./"  # 하위 폴더들이 있는 상위 폴더 경로
count_files_in_multiple_folders(parent_directory)
