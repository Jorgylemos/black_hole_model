import os

class LoadDataset():
    def __init__(self, root_dir): 
        self.root_dir = root_dir

        self.class_map = {"black_hole": 0, "neutron_star": 1, "quasar": 2}

        for class_name, label in self.class_map.items():
            class_dir = os.path.join(self.root_dir, class_name)
            if not os.path.exists(class_dir):
                print(f"Warning: Folder {class_dir} not Found")
                continue
