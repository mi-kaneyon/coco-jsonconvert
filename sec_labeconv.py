import os
import json
import shutil
from sklearn.model_selection import train_test_split

def rename_file(file_name):
    prefix, rest = file_name.split('-', 1)
    return rest

def create_json(data, file_names, folder):
    new_data = {}
    new_data['images'] = [dict(item, file_name=rename_file(item['file_name'].split('/')[-1])) for item in data['images'] if rename_file(item['file_name'].split('/')[-1]) in file_names]
    new_data['annotations'] = [item for item in data['annotations'] if rename_file(data['images'][item['image_id']]['file_name'].split('/')[-1]) in file_names]
    new_data['categories'] = data['categories']
    new_data['info'] = data['info']

    with open(f'{folder}/cupa.json', 'w') as outfile:
        json.dump(new_data, outfile)

def main():
    with open('result.json') as json_file:
        data = json.load(json_file)

    image_data = data['images']
    original_file_names = [item['file_name'].split('/')[-1] for item in image_data]
    renamed_file_names = [rename_file(file_name) for file_name in original_file_names]

    train_data, val_data = train_test_split(renamed_file_names, test_size=0.2, random_state=42)

    if not os.path.exists('train'):
        os.makedirs('train')
    if not os.path.exists('val'):
        os.makedirs('val')

    for original, renamed in zip(original_file_names, renamed_file_names):
        if renamed in train_data:
            shutil.copy(os.path.join('images', original), os.path.join('train', renamed))
        elif renamed in val_data:
            shutil.copy(os.path.join('images', original), os.path.join('val', renamed))

    create_json(data, train_data, 'train')
    create_json(data, val_data, 'val')

if __name__ == "__main__":
    main()
