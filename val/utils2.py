def split_whole_data(self, target_file:str) -> None:
        '''전체 데이터 파일 (train.trn)을 그룹별로 구분
        For example, in train.trn file
            KsponSpeech_01/KsponSpeech_0001/KsponSpeech_000001.pcm :: 'some text'
                -> this file will be stored in train_KsponSpeech_01.trn
            KsponSpeech_02/KsponSpeech_0001/KsponSpeech_000002.pcm :: 'some text'
                -> this file will be stored in train_KsponSpeech_02.trn
        '''
        with open(target_file, 'rt') as f:
            lines = f.readlines()
            data_group = set()
            for line in lines:
                data_group.add(line.split('/')[0])
        data_group = sorted(list(data_group))
        data_dic = { group: [] for group in data_group} # dict comprehension
        for line in lines:
            data_dic[line.split('/')[0]].append(line)
        # Save file seperately
        # target_file: data/info/train.trn -> ['data', 'info', 'train.trn']
        save_dir = target_file.split('/')[:-1]
        save_dir = '/'.join(save_dir)
        for group, line_list in data_dic.items():
            file_path = os.path.join(save_dir, f'train_{group}.trn')
            with open(file_path, 'wt', encoding='utf-8') as f:
                for text in line_list:
                    f.write(text)
                print(f'File created -> {file_path}')
        print('Done!')