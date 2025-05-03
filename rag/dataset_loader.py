def load_dataset(file_path):
    with open(file_path, 'r') as file:
        dataset = file.readlines()
    print(f'Loaded {len(dataset)} entries')
    return dataset