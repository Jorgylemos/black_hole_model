import os
import torchvision.transforms as transforms

from PIL import Image

class ConvertImage:
    def __init__(self, samples, transform=None):
        self.samples = samples
        self.transform = transform

    def __getitem__(self, idx):
        path, label = self.samples[idx]
        image = Image.open(path).convert('L')

        if self.transform:
            image = self.transform(image)
        else:
            image = transforms.Compose([
                transforms.Resize((256,256)),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.5], std=[0.5])
            ])(image)

        return image, label

class LoadDataset():
    def __init__(self, root_dir, transform=None): 
        self.root_dir = root_dir
        self.transform = transform
        self.samples = []

        self.class_map = {"black_hole": 0, "neutron_star": 1, "quasar": 2}
    
        for class_name, label in self.class_map.items():
            class_dir = os.path.join(self.root_dir, class_name)
            
            if not os.path.exists(class_dir):
                print(f"Warning: Folder {class_dir} not Found")
                continue

            for file_name in os.listdir(class_dir):
                if file_name.lower().endswith(("png", "jpg", "jpeg")):
                    self.samples.append((os.path.join(class_dir, file_name), label))
        
        self.converter = ConvertImage(samples=self.samples, transform=transform)
        print(f"Samples loaded {len(self.samples)}")
    
    def __len__(self):
        return len(self.samples)
    
    def __getitem__(self, idx):
        return self.converter[idx]

        