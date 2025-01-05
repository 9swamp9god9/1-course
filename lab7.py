class Employee:
    def __init__(self, name, id_of):
        self.name = name
        self.id_of = id_of

    def get_info(self):
        return f'Имя сотрудника: {self.name}, ID сотрудника: {self.id_of}'


class Manager(Employee):
    def __init__(self, name, id_of, projects, department):
        Employee.__init__(self, name, id_of)
        self.projects = projects
        self.department = department

    def manage_project(self):
        return f'Менеджер {self.name} ID: {self.id_of}. управляет проектом: {self.projects}, Отдел работы менеджера: {self.department}'


class Technician(Employee):
    def __init__(self, name, id_of, specialization):
        super().__init__(name, id_of)
        self.specialization = specialization

    def perform_maintenance(self):
        return f'Техник: {self.name} ID: {self.id_of}. Специализируется на {self.specialization}'


class TechManager(Manager, Technician):
    def __init__(self, name, id_of, department, specialization):
        super().__init__(name, id_of, department, specialization)
        self.s = []

    def add_employee(self, empl):
        self.s.append(empl.name)
        self.s.append(empl.id_of)

    def get_team_info(self):
        return f'Состав комманды: \n{self.s}'


empl = Employee('ВАНЕК', '1')
mng = Manager('АЛЕКСЕЙ', '2', 'Разработка ПО', 'Связь')
tech = Technician('ОЛЕГ', '3', 'техническом обслуживании')
techmng = TechManager('СЕРЕГА', '4', 'CCC', 'технический менеджер')

print(empl.get_info())
print(mng.manage_project())
print(tech.perform_maintenance())
techmng.add_employee(empl)
techmng.add_employee(mng)
techmng.add_employee(tech)
techmng.add_employee(techmng)
print(techmng.get_team_info())
