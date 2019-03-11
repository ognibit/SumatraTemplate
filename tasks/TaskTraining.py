from datetime import datetime as dt

def train(configuration):
    model_file = configuration['model']
    with open(model_file, 'w') as model:
        model.write('Model at ')
        model.write(dt.now().isoformat())
        model.write('\n')

