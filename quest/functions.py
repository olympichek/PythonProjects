def read_data(filename):
    file = open(filename, 'r')
    lines = []
    for line in file:
        lines.append(line)
    lines = lines[6:-4]
    data = []
    for line in lines:
        parts = line.split()
        if len(parts) != 2:
            raise ValueError("Wrong input file format!")
        try:
            length, index = map(float, parts)
            data.append([length, index])
        except ValueError as e:
            raise ValueError("Wrong data format, " + str(e) + "!")
    return data

def clean_data(data):
    def filter_function(row):
        if row[0] >= 450 and row[0] <= 800:
            return True
        return False
    data_ = list(filter(filter_function, data))
    return data_

def compare_floats(f1, f2):
    precision = 0.000001
    if abs(f1 - f2) < precision:
        return True
    return False

def get_step(data):
    return data[1][0] - data[0][0]

def check_wavestep(step1, step2, step3):
    if  compare_floats(step1, step2)\
    and compare_floats(step2, step3):
        return True
    return False

def normalize_wavestep(max_step):
    def normalize_wavestep_(data):
        data_ = [data[0]]
        acc = data[0][0]
        for i in range(1, len(data)):
            if data[i][0] - acc >= max_step:
                data_.append(data[i])
                acc = data[i]
        return data_
    return normalize_wavestep_
