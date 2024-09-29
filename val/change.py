import os
import csv

# CSV 파일에서 확장자를 바꾸는 함수
def update_audio_file_extension(csv_file, output_file):
    updated_rows = []

    # CSV 파일 읽기
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames  # 기존 CSV 파일의 열 이름을 가져옴

        for row in reader:
            audio_file = row['audio_file']

            # 'wavp' 확장자를 'wav'로 변경
            if audio_file.endswith('wavp'):
                row['audio_file'] = audio_file[:-1]  # 'wavp'에서 마지막 'p' 제거

            # 'WAV' 확장자를 'wav'로 변경
            elif audio_file.endswith('WAV'):
                row['audio_file'] = audio_file[:-3] + 'wav'  # 'WAV'를 'wav'로 대체

            updated_rows.append(row)  # 수정된 행을 리스트에 추가

    # 수정된 내용을 새로운 CSV 파일로 저장
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()  # CSV 파일에 헤더 쓰기
        writer.writerows(updated_rows)  # 수정된 행들 쓰기

# 실제 파일의 확장자를 바꾸는 함수
def update_wav_file_extensions(directory):
    for filename in os.listdir(directory):
        # 'WAV' 확장자를 가진 파일을 찾음
        if filename.endswith('.WAV'):
            # 새로운 파일 이름을 만듦 ('WAV'를 'wav'로 변경)
            new_filename = filename[:-3] + 'wav'

            # 파일 이름을 변경
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            os.rename(old_file_path, new_file_path)

            print(f"Renamed: {old_file_path} -> {new_file_path}")

# 사용 예시
csv_file = 'input.csv'  # 입력 CSV 파일 경로
output_file = 'output.csv'  # 수정된 내용을 저장할 출력 CSV 파일 경로
directory = './AI스피커'  # 실제 음성 파일이 있는 디렉토리 경로

# CSV 파일의 확장자 수정
# update_audio_file_extension(csv_file, output_file)

# 실제 파일의 확장자 수정
update_wav_file_extensions(directory)
