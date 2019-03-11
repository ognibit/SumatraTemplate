from datetime import datetime as dt

def check(configuration):
    report_file = configuration['report']
    with open(report_file, 'w') as report:
        report.write('Report at ')
        report.write(dt.now().isoformat())
        report.write('\n')

