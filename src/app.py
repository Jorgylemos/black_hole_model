import os
import sys
import torch
from load_dataset import LoadDataset

def main():
    # Show current using device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device {device}")

    # Use command: python3 src/app.py ./dataset
    if len(sys.argv) > 1:
        data_root = sys.argv[1]
    else:
    # Dataset folder (in root)
        data_root = './dataset'

    if not os.path.exists(data_root):
       print(f"Creating folder {data_root}.")
       os.makedirs(os.path.join(data_root, "black_hole"), exist_ok=True)
       os.makedirs(os.path.join(data_root, "neutron_star"), exist_ok=True)
       os.makedirs(os.path.join(data_root, "quasar"), exist_ok=True)

    dataset_full = LoadDataset(data_root)

    if len(dataset_full) == 0:
        dataset_full = LoadDataset(data_root)
    
    if len(dataset_full) == 0:
        print("Images not found. Finishing...")
        return

if __name__ == "__main__":
    main()
