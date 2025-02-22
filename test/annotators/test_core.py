import cv2
import numpy as np
import pytest

from supervision.annotators.core import (
    BoxAnnotator,
    CompositeAnnotator,
    LabelAnnotator,
    MaskAnnotator,
    TraceAnnotator,
)
from supervision.detection.core import Detections


@pytest.fixture
def sample_image():
    return np.zeros((500, 500, 3), dtype=np.uint8)


@pytest.fixture
def sample_detections():
    return Detections(
        xyxy=np.array([[50, 50, 100, 100], [150, 150, 200, 200]]),
        confidence=np.array([0.9, 0.8]),
        class_id=np.array([1, 2]),
    )


def test_composite_annotator(sample_image, sample_detections):
    composite_annotator = CompositeAnnotator(
        annotators=[
            BoxAnnotator(),
            LabelAnnotator(),
            MaskAnnotator(),
            TraceAnnotator(),
        ]
    )

    annotated_image = composite_annotator.annotate(
        scene=sample_image.copy(),
        detections=sample_detections,
    )

    assert annotated_image is not None
    assert annotated_image.shape == sample_image.shape
    assert annotated_image.dtype == sample_image.dtype
