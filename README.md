# SuperYOLO: Enhanced Weapon Detection in Surveillance Videos

## Introduction
SuperYOLO combines Super Resolution (SR) and You Only Look Once (YOLO) object detection models to improve weapon detection in low-resolution surveillance footage. Developed by Alessandro Rongoni and Daniele Sergiacomi at the Polytechnic University of Marche, this project aims to address the challenge of identifying small-scale objects in surveillance videos, enhancing public safety.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Documentation](#documentation)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## Installation
To install SuperYOLO, clone the repository and install the required dependencies.
```
git clone https://github.com/your-repo/SuperYOLO.git
cd SuperYOLO
pip install -r requirements.txt
```

## Usage
To run SuperYOLO on your surveillance footage, follow the instructions below:
```
python super_yolo.py --input <path_to_video> --output <path_to_output>
```

## Features
- Integration of Super Resolution (SR) to enhance image quality of low-resolution videos.
- Utilization of the YOLO object detection model for real-time weapon detection.
- Custom training on a surveillance dataset for improved weapon recognition.

## Dependencies
- Python 3.8 or later
- PyTorch
- OpenCV
- NumPy

## Configuration
Adjust the `config.json` file to tune the model according to your specific needs, including input resolution, detection threshold, and more.

## Documentation
For detailed documentation on the SuperYOLO model, including the architecture, training process, and evaluation results, refer to the included project report.

## Examples
See the `examples/` directory for sample videos processed by SuperYOLO, demonstrating the enhancement in weapon detection accuracy.

## Troubleshooting
If you encounter any issues with installation or running the SuperYOLO model, please check the `troubleshooting.md` file for common problems and solutions.

## Contributors
- Alessandro Rongoni
- Daniele Sergiacomi

## License
SuperYOLO is released under the MIT License. See the LICENSE file for more details.
