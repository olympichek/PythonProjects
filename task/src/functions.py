from .dataset import Dataset

def read_dataset(filename):
    try:
        file = open('./datasets/' + filename, 'r')
        dataset = Dataset()
        dataset.label = ''.join(filename.split('.')[:-1])
        lines = []
        for line in file:
            lines.append(line)
        e1_message = 'Wrong input file format!'
        try:
            step = float(lines[4].split(':')[1])
            dataset.step = step
        except ValueError:
            raise ValueError(e1_message)
        lines = lines[6:-4]
        for line in lines:
            parts = line.split()
            if len(parts) != 2:
                raise ValueError(e1_message)
            try:
                length, absorption = map(float, parts)
                dataset.add_length(length)
                dataset.add_absorption(absorption)
            except ValueError as e:
                e2_message = 'Wrong data format!\n' + str(e) 
                raise ValueError(e2_message)
        return dataset
    except FileNotFoundError as e:
        e3_message = 'File not Found!\n' + str(e)
        raise FileNotFoundError(e3_message)

def filter_dataset(dataset):
    length, absorption = [], []
    for length_, absorption_ in\
    zip(dataset.length, dataset.absorption):
        if length_ >= 450 and length_ <= 800:
            length.append(length_)
            absorption.append(absorption_)
    dataset.length = length
    dataset.absorption = absorption
    return dataset

def compare_floats(f1, f2):
    precision = 0.000001
    if abs(f1 - f2) < precision:
        return True
    return False

def check_wavestep(steps):
    step0 = steps[0]
    return all([
        compare_floats(step, step0)
        for step in steps
    ])

def normalize_wavestep(max_step, dataset):
    length = [dataset.length[0]]
    absorption = [dataset.absorption[0]]
    length_t = dataset.length[0]
    for length_, absorption_ in\
    zip(dataset.length, dataset.absorption):
        if length_ - length_t >= max_step:
            length.append(length_)
            absorption.append(absorption_)
            length_t = length_
    dataset.length  = length
    dataset.absorption = absorption
    dataset.step = max_step
    return dataset

def get_max_absorption(dataset):
    max_a  = dataset.absorption[0] # max absorption
    max_al = dataset.length[0]     # max absorption length 
    for length_, absorption_ in\
    zip(dataset.length, dataset.absorption):
        if absorption_ > max_a:
            max_a = absorption_
            max_al = length_
    return (max_al, max_a)

def get_integral_absorption(dataset):
    integral_sum = 0
    for i in range(len(dataset.length) - 1):
        avg_a = (dataset.absorption[i] + dataset.absorption[i + 1]) / 2
        integral_sum += avg_a * dataset.step
    return integral_sum
