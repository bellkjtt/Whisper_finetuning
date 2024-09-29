import os

def get_file_names_without_extension(directory, extension):
    # 주어진 폴더에서 특정 확장자를 가진 파일의 이름만 추출 (확장자 제외)
    file_names = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                # 파일 이름에서 확장자를 제거한 후 저장
                file_name_without_ext = os.path.splitext(file)[0]
                file_names.add(file_name_without_ext)
    return file_names

def compare_label_and_source(label_folder, source_folder):
    # 라벨 폴더에서 json 파일 이름 목록 가져오기
    label_files = get_file_names_without_extension(label_folder, '.json')
    # 원천 폴더에서 wav 파일 이름 목록 가져오기
    source_files = get_file_names_without_extension(source_folder, '.wav')

    # 라벨 폴더에만 있는 파일
    missing_in_source = label_files - source_files
    # 원천 폴더에만 있는 파일
    missing_in_label = source_files - label_files
    missing_in_source = sorted(missing_in_source)
    missing_in_label = sorted(missing_in_label)
    # 결과 출력
    if missing_in_source:
        print(f"Files missing in [원천] but present in [라벨]: {len(missing_in_source)}")
        for file in missing_in_source:
            print(f"  Missing in [원천]: {file}.json")
    else:
        print("No files missing in [원천] that are present in [라벨].")

    if missing_in_label:
        print(f"Files missing in [라벨] but present in [원천]: {len(missing_in_label)}")
        for file in missing_in_label:
            print(f"  Missing in [라벨]: {file}.wav")
    else:
        print("No files missing in [라벨] that are present in [원천].")

# 사용 예시
label_folder_path = './[라벨]2.음성수집도구'  # 라벨 폴더 경로
source_folder_path = './[원천]2.음성수집도구'  # 원천 폴더 경로

compare_label_and_source(label_folder_path, source_folder_path)