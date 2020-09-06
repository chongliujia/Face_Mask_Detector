# -*- coding:utf-8 -*-

from tensorflow.keras.applications.mobilent_v2 import perprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

import numpy as np
import argparse
import cv2
import os


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
        help="path to input image")
ap.add_argument("
