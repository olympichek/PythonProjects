class Dataset:

    def __init__(self):
        self.length  = []
        self.absorption = []
        self.step = .0
        self.label = ''

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length

    def add_length(self, length_):
        self.__length.append(length_)
    
    @property
    def absorption(self):
        return self.__absorption

    @absorption.setter
    def absorption(self, absorption):
        self.__absorption = absorption

    def add_absorption(self, absorption_):
        self.__absorption.append(absorption_)

    @property
    def step(self):
        return self.__step

    @step.setter
    def step(self, step):
        self.__step = step

    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label):
        self.__label = label
