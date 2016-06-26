from collections import OrderedDict


class Report:
    def __init__(self, plate_id):
        self.plate_id = plate_id
        self.car_parts = OrderedDict()

    def add_check(self, test_name, status):
        self.car_parts[test_name] = status

    def passed(self):
        return all(self.car_parts.values())\

    def render(self):

        report = '\nResults for car #{}\n'.format(self.plate_id)
        for test_name in self.car_parts:
            if self.car_parts[test_name]:
                report += '* {}: OK\n'.format(test_name)
            else:
                report += '* {}: Failed\n'.format(test_name)
        if self.passed():
            report += 'PASSED\n'
        else:
            report += 'NOT PASSED\n'
        return report.strip()

