import os
import json
import pandas as pd

def extract_data_from_json(label_folders):
    data = []  # 데이터를 저장할 리스트

    # 각 폴더에서 JSON 파일을 찾아서 처리
    for folder in label_folders:
        label = os.path.basename(folder)  # 폴더 이름을 구분자로 사용

        for file_name in os.listdir(folder):
            if file_name.endswith('.json'):  # JSON 파일만 처리
                file_path = os.path.join(folder, file_name)

                # JSON 파일 열기
                with open(file_path, 'r', encoding='utf-8') as f:
                    json_data = json.load(f)

                    # 필요한 정보 추출
                    stt_text = json_data['발화정보']['stt']
                    audio_file = json_data['발화정보']['fileNm']

                    # 데이터 리스트에 추가 (label도 함께 추가)
                    data.append({
                        'audio_file': audio_file,
                        'stt_text': stt_text,
                        'label': label  # 폴더 이름을 label로 추가
                    })

    return data

# 라벨 폴더 리스트 (폴더 경로를 여기에 추가)
label_folders = ['./[라벨]1.AI챗봇', './[라벨]2.음성수집도구', './[라벨]3.스튜디오', './[라벨]4.AI스피커']

# 데이터 추출
data = extract_data_from_json(label_folders)

# DataFrame으로 변환
df = pd.DataFrame(data)

# CSV 파일로 저장
df.to_csv('audio_text_pairs_with_labels.csv', index=False, encoding='utf-8')

# 또는 PKL 파일로 저장
df.to_pickle('audio_text_pairs_with_labels.pkl')

print("CSV 및 PKL 파일이 생성되었습니다.")
