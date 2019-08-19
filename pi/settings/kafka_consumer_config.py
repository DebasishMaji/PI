import yaml
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

with open(BASE_DIR +"/config/kafka_consumer_config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

for section in cfg:
    print(section)
print(cfg['kafka'])
