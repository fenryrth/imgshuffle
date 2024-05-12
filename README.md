# imgShuffle

This project is a simple screensaver built using the PyGame library. It displays a random sequence of images from a specified folder, fitting them to the screen while preserving their aspect ratios. The screensaver features fade transitions between images and hides the mouse cursor when active.

## Features

- Displays images from a user-specified folder.
- Scales images to fit the screen while maintaining the aspect ratio.
- Randomly shuffles images each time the screensaver starts.
- Implements fade transitions between images.
- Hides the mouse cursor during operation.
- Exits immediately on pressing the `Esc` key.


## Installation using conda

```bash
git clone https://github.com/fenryrth/imgshuffle.git
cd imgshuffle/
conda env create -f environment.yml
conda activate imgshuffle
```

### The manual way

```bash
conda create -n imgshuffle python=3.10
conda activate imgshuffle
git clone https://github.com/fenryrth/imgshuffle.git
cd imgshuffle/
pip install -r requirements.txt
```
## Edit config
You need to edit the `config.json` file before you can run the program.
Change the path to your preffered image folder.
You can also edit how long each image is shown on your screen. The default is 15 seconds.

## Run imgShuffle
```bash
python imgshuffle.py
