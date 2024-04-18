from typing import Any

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics
import shap
from sklearn.metrics import confusion_matrix

import streamlit as st
from streamlit.hello.utils import show_code