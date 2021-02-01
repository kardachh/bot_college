class Group:
    name_of_group = 'None'
    prepod = 'None'
    type_ = 'None'
    name = 'None'
    
    def __init__(self, name_of_group, time, name, type_, prepod, cabinet):
        mass_of_group.append(self)
        self.time = time
        self.name_of_group = name_of_group
        self.prepod = prepod
        self.type_ = type_
        self.name = name
        self.cabinet = cabinet

mass_of_group = []
isp102 = Group('I','H','I','J','K','L')
