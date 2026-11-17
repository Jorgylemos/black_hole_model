import os
import torch

def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device {device}")

    folder_root = "./dataset"

    if not os.path.exists(folder_root):
       print(f"Creating folder {folder_root}.")
       os.makedirs(os.path.join(folder_root, "black_hole"), exist_ok=True)
       os.makedirs(os.path.join(folder_root, "neutron_star"), exist_ok=True)
       os.makedirs(os.path.join(folder_root, "quasar"), exist_ok=True)

if __name__ == "__init__":
    main()
