import torchvision.transforms as transforms

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