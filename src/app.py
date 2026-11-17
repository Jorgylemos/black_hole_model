import os
import torch

def main():

    # Show current using device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device {device}")

    # Dataset folder (in root)
    data_root = "./dataset"

    if not os.path.exists(data_root):
       print(f"Creating folder {data_root}.")
       os.makedirs(os.path.join(data_root, "black_hole"), exist_ok=True)
       os.makedirs(os.path.join(data_root, "neutron_star"), exist_ok=True)
       os.makedirs(os.path.join(data_root, "quasar"), exist_ok=True)

if __name__ == "__init__":
    main()
