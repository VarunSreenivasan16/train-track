import subprocess
import sys

def install(package, file_link=None):
    if file_link:
        subprocess.run([sys.executable, "-m", "pip", "install", package, "-f", file_link], stdout=True, stderr=True, capture_output=True, shell=True)
    else:
        subprocess.run([sys.executable, "-m", "pip", "install", package])
    
def main():
    
    cuda = "cpu"
    torch_version = "torch==1.8.0"+cuda
    install("torch_version", "https://download.pytorch.org/whl/torch_stable.html")
    
    try:
        import torch
        print("Imported!")
    except ModuleNotFoundError as err:
        print(err)
    
if __name__=="__main__":
    main()