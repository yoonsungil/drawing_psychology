import os, json
from const import NAMOO
import yaml

def json_to_df(data_path, img_w, img_h, type):
    for j in os.listdir(data_path):
        if j.endswith('.json'):
            with open(os.path.join(data_path, j ), 'r', encoding='utf8') as jf:
                data = json.loads(jf.read())
            file_name = os.path.join(data_path, j).replace('.json','.txt')
            for i in data['annotations']['bbox']:
                label = type[i['label']]
                x = (i['x'] + i['w'] / 2) / img_w
                y = (i['y'] + i['h'] / 2) / img_h
                w = i['w'] / img_w
                h = i['h'] / img_h
                data = f"{label} {x} {y} {w} {h}\n"
                if not os.path.exists(file_name):
                    with open(file_name, 'w') as f:
                        f.write(data)
                else:
                    with open(file_name, 'a') as f:
                        f.write(data)
        
if __name__ == "__main__":
    json_to_df('data/train/tree',1280,1280,NAMOO)

    data_yaml = {
        'train':'./266.AI_기반_아동_미술심리_진단을_위한_그림_데이터_구축/01-1.정식개방데이터/Training/01.원천데이터/나무',
        'val':'./266.AI_기반_아동_미술심리_진단을_위한_그림_데이터_구축/01-1.정식개방데이터/Validation/01.원천데이터/나무',
        'test':'./266.AI_기반_아동_미술심리_진단을_위한_그림_데이터_구축/01-1.정식개방데이터/Validation/01.원천데이터/나무',
        'nc':len(list(NAMOO.keys())),
        'names':list(NAMOO.keys())
    }

    with open(f'./test.yaml', 'w') as outfile:
        yaml.dump(data_yaml, outfile, default_flow_style=True)
