import torch
import torchvision
import torchaudio

def arr():
    ar = torch.rand(5, 5)
    return ar


def main():
    ver1 = torch.__version__
    ver2 = torchvision.__version__
    ver3 = torchaudio.__version__
    print(f"Hello, PyTorch({ver1})!")
    print("\t" + f"Hello, TorchVision({ver2})!")
    print("\t" * 2 + f"Hello, TorchAudio({ver3})!")
    print("~" * 30)
    ar = arr()
    print("下面这是我使用torch创建的第一个张量：")
    print(ar)
    return None

if __name__ == "__main__":
    main()
