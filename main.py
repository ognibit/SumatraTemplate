import sys
import yaml
from tasks.TaskCheck import check
from tasks.TaskTraining import train

config_file = sys.argv[1]
configuration = {}

with open(config_file, 'r') as stream:
    configuration = yaml.load(stream)

# save the configuration to the output in order to get all the information
with open('./Data/config.yaml','w') as outconf:
    yaml.dump(configuration, outconf)

task = configuration['task']

if task == 'check':
    print('Running checks...')
    check(configuration['check'])
elif task == 'training':
    print('Running training...')
    train(configuration['training'])
else:
    raise ValueError('Task not found: %s' % task)

print('DONE')
