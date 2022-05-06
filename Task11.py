import os


class NewClass:
    def __init__(self, path, bool_value, my_str, new_obj):
        self.path = path
        self.bool_value = bool_value
        self.my_str = my_str
        self.new_obj = new_obj
        self.list_dir = self.create_dict()
        self.sort_dir = self.create_dict()

    def create_dict(self):
        list_dir = os.listdir(self.path)
        dirs_list = []
        files_list = []
        for filename in list_dir:
            filepath = os.path.join(self.path, filename)
            if os.path.isdir(filepath):
                dirs_list.append(filename)
            elif os.path.isfile(filepath):
                files_list.append(filename)
        return {'filenames': files_list, 'dirnames': dirs_list}

    def sort_dict(self):
        for key in self.sort_dir:
            self.sort_dir[key].sort(reverse=not self.bool_value)
        return self.sort_dir

    def update_dict(self):
        key = 'filenames' if "." in self.my_str else 'dirnames'
        self.list_dir[key].append(self.my_str)
        return self.list_dir


worker = NewClass("test_dir", True, "str.txt", 'new_dir')
result1 = worker.create_dict()
result2 = worker.sort_dict()
result3 = worker.update_dict()

print(f'\n#1\n{result1}\n\n#2\n{result2}\n\n#3\n{result3}\n\n')
