import pandas as pd
from torch import nn, optim
import torch.nn.functional as F
import torch.utils.data as data
import torch
import numpy as np
import io


def feat (dict):
  list = ["Age","Gender","Height","ICUType","Weight","GCS","HR","NIDiasABP","NIMAP","NISysABP","RespRate","Temp","Urine","HCT","BUN","Creatinine","Glucose","HCO3","Mg","Platelets","K","Na","WBC","pH","PaCO2","PaO2","DiasABP","FiO2","MAP","MechVent","SysABP","SaO2","Albumin","ALP","ALT","AST","Bilirubin","Lactate","Cholestrol","Troponinl","TropininT"]
  arr= np.empty(41,dtype='float')
  for i in range(41):
    feature=list[i]
    if feature in dict:
      arr[i]=(dict[feature])
  return arr

def test (dict):
  x=feat(dict)
  classifier = joblib.load('model.pkl')  
  y_pred = classifier.predict_proba(x_test)
  return y_pred