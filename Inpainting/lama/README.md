# 🦙 LaMa: Resolution-robust Large Mask Inpainting with Fourier Convolutions

[[Original Github Link](https://github.com/advimman/lama)] Edit by Chaea Kim

<p align="center" "font-size:30px;">
  <br>
  <b>
We reconstructed the image using lama, one of the inpainting models.</br>
When comparing the four inpainting models, lama performed the best.</br>
Generate a mask through yolo or user input, and apply dilation to various scales. </br>
Put the input images into the lama with the generated masks. </br>
A detailed operation method will be described below.</b>
</p>

<p align="center">
  <img src="https://github.com/2018007956/HYU-Capstone-Project/assets/48304130/52fb4064-1bb4-42af-bcac-01171576957d" weight="500">
</p>
<p align="center">
  <img src="https://github.com/2018007956/HYU-Capstone-Project/assets/48304130/650ee66e-72e6-49dd-954d-5eaabc4483b3" height="400">
</p>
<p align="center">
  <img src="https://github.com/2018007956/HYU-Capstone-Project/assets/48304130/ba0ec29e-e1f8-4458-9120-37d51c64fe1c" height="300">
</p>


# Environment setup

Clone the repo:
`git clone https://github.com/advimman/lama.git`

There are three options of an environment:

1. Python virtualenv:

    ```
    virtualenv inpenv --python=/usr/bin/python3
    source inpenv/bin/activate
    pip install torch==1.8.0 torchvision==0.9.0
    
    cd lama
    pip install -r requirements.txt  <----------!!!!!!!!!
    ```

2. Conda
    
    ```
    % Install conda for Linux, for other OS download miniconda at https://docs.conda.io/en/latest/miniconda.html
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda
    $HOME/miniconda/bin/conda init bash

    cd lama
    conda env create -f conda_env.yml
    conda activate lama
    conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch -y
    pip install pytorch-lightning==1.2.9
    ```
 
3. Docker: No actions are needed 🎉.

# Inference <a name="prediction"></a>
```
cd lama
pip install -r requirements.txt 
```
**1. Download pre-trained models**

Install tool for yandex disk link extraction:

```
pip3 install wldhx.yadisk-direct
```

The best model (Places2, Places Challenge):
    
```    
curl -L $(yadisk-direct https://disk.yandex.ru/d/ouP6l8VJ0HpMZg) -o big-lama.zip
unzip big-lama.zip
```

All models (Places & CelebA-HQ):

```
curl -L $(yadisk-direct https://disk.yandex.ru/d/EgqaSnLohjuzAg) -o lama-models.zip
unzip lama-models.zip
```

Setting environments:
```
pip install --upgrade pip
pip install pytorch_lightning 
pip install kornia --no-dependencies
pip install hydra
pip install omegaconf
pip install webdataset
pip install hydra-core --upgrade

python -m pip install git+https://github.com/facebookresearch/detectron2.git
```

**2. Prepare images and masks**

Prepare your data:
1) Create masks named as `[images_name]_maskXXX[image_suffix]`, put images and masks in the same folder `./lama/input_data`. 
- You can use the [yolov5](https://github.com/ultralytics/yolov5) or [UserInput](mask generation/UserInput/UserInputGenerationMask.ipynb) for masks generation. 
- Check the format of the files:
    ```    
    image1_mask001.png
    image1.png
    image2_mask001.png
    image2.png
    ```
2) Specify `image_suffix`, e.g. `.png` or `.jpg` or `_input.jpg` in `configs/prediction/default.yaml`.  

3) Apply the dilation:
    ```
    Python /HYU-CAPSTONE-PROJECT/mask generation/Dilation.py'
    ```
    You can change the parameter in that file.


**3. Predict with Refinement**

On the host machine:

    python3 bin/predict.py refine=True model.path=$(pwd)/big-lama indir=$(pwd)/LaMa_test_images outdir=$(pwd)/output
