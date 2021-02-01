class Group:
    name_of_group = 'None'
    prepod = 'None'
    type_ = 'None'
    name = 'None'

    def __init__(self, name_of_group, prepod, type_, name, cabinet):
        self.name_of_group = name_of_group
        self.prepod = prepod
        self.type_ = type_
        self.name = name
        self.cabinet = cabinet
    
    

isp301201 = Group('AS','AU','AT','AS','AV')
isp202 = Group('AA','AC','AB','AA','AD')

mass_of_group = [isp301201,isp202]


