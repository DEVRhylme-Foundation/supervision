
# Supervision
[![version](https://badge.fury.io/py/supervision.svg)](https://badge.fury.io/py/supervision)
[![downloads](https://img.shields.io/pypi/dm/supervision)](https://pypistats.org/packages/supervision)
[![snyk](https://snyk.io/advisor/python/supervision/badge.svg)](https://snyk.io/advisor/python/supervision)
[![license](https://img.shields.io/pypi/l/supervision)](https://github.com/roboflow/supervision/blob/main/LICENSE.md)
[![python-version](https://img.shields.io/pypi/pyversions/supervision)](https://badge.fury.io/py/supervision)
[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/roboflow/supervision/blob/main/demo.ipynb)
[![gradio](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/Roboflow/Annotators)
[![discord](https://img.shields.io/discord/1159501506232451173?logo=discord&label=discord&labelColor=fff&color=5865f2&link=https%3A%2F%2Fdiscord.gg%2FGbfgXGJ8Bk)](https://discord.gg/GbfgXGJ8Bk)
[![built-with-material-for-mkdocs](https://img.shields.io/badge/Material_for_MkDocs-526CFE?logo=MaterialForMkDocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)



</div>


## Introduction
Welcome to **Supervision**! We provide reusable computer vision tools designed to simplify your workflow, from dataset management to object detection and video annotation. Whether you need to load datasets, draw detections, or count objects in a zone, **Supervision** has you covered! 🤝

## Features

Model Agnostic: Works with any classification, detection, or segmentation model.

Prebuilt Annotators: Easily visualize and label objects in images and videos.

Dataset Management: Load, split, merge, and save datasets in multiple formats.

Beginner Friendly: Simple API with powerful utilities for computer vision tasks.
---

## Installation
Supervision requires Python >= 3.8. You can install it using **pip**:
```sh
pip install supervision
```
For additional installation options, including **conda**, **mamba**, and installing from source, refer to our [installation guide](#).

---

Read more about conda, mamba, and installing from source in our [guide](https://roboflow.github.io/supervision/).

## Quickstart
### Model Integration
Supervision is **model-agnostic**, allowing you to integrate it with any classification, detection, or segmentation model. We offer built-in connectors for popular libraries like **Ultralytics YOLO**, **Transformers**, and **MMDetection**.

#### Example: Object Detection with YOLO
```python
import cv2
import supervision as sv
from ultralytics import YOLO

image = cv2.imread("your_image.jpg")
model = YOLO("yolov8s.pt")
result = model(image)[0]
detections = sv.Detections.from_ultralytics(result)

print(len(detections))  # Output: Number of detected objects
```


### Annotators
Supervision provides customizable **annotators** to enhance object visualizations.

#### Example: Annotating Objects in an Image
```python
import cv2
import supervision as sv

image = cv2.imread("your_image.jpg")
detections = sv.Detections(...)

box_annotator = sv.BoxAnnotator()
annotated_frame = box_annotator.annotate(
    scene=image.copy(),
    detections=detections
)
```


### Dataset Management
Supervision streamlines dataset handling, allowing you to load, split, merge, and save datasets effortlessly.

#### Example: Loading a Dataset from Roboflow
```python
import supervision as sv
from roboflow import Roboflow

project = Roboflow().workspace("<WORKSPACE_ID>").project("<PROJECT_ID>")
dataset = project.version("<PROJECT_VERSION>").download("coco")

ds = sv.DetectionDataset.from_coco(
    images_directory_path=f"{dataset.location}/train",
    annotations_path=f"{dataset.location}/train/_annotations.coco.json",
)

path, image, annotation = ds[0]  # Load image dynamically
```


---


## 🔐 Environment Variables

Create a `.env` file to store sensitive configuration:

```bash
ROBOFLOW_API_KEY=your_api_key_here
LOG_LEVEL=INFO
```

Then load them in your code:
```python
from dotenv import load_dotenv

load_dotenv()  # Load before other imports
# Now use os.getenv() to access values
```

## Tutorials
Enhance your knowledge with real-world use cases:
- **[Dwell Time Analysis with Computer Vision](#)** – Analyze wait times using object tracking.
- **[Speed Estimation & Vehicle Tracking](#)** – Implement multi-object tracking and speed estimation with YOLO & ByteTrack.

📚 [Explore More Tutorials](#)

---

## Community & Contribution
🚀 Built something amazing with **Supervision**? Share your project with us!
- **Football Players Tracking** 🎥 [Watch Video](#)
- **Traffic Analysis** 🎥 [Watch Video](#)
- **Vehicle Speed Estimation** 🎥 [Watch Video](#)

Interested in contributing? Check out our [contribution guide](#) to get started! 🙏

---

## Documentation
📖 Visit our [full documentation page](#) for in-depth guides, API references, and best practices to accelerate your computer vision projects.

Happy coding! 🎉


## 💜 built with supervision

https://user-images.githubusercontent.com/26109316/207858600-ee862b22-0353-440b-ad85-caa0c4777904.mp4

https://github.com/roboflow/supervision/assets/26109316/c9436828-9fbf-4c25-ae8c-60e9c81b3900

https://github.com/roboflow/supervision/assets/26109316/3ac6982f-4943-4108-9b7f-51787ef1a69f

