import numpy as np
from PIL import ImageDraw
from PIL import Image
from matplotlib import gridspec, pyplot as plt

add_patient_history = {
      "patient_id": 1,
      "comment": "test-comment",
      "date": "test_date",
      "history_neutral_network": {
         "photo_original": "dddd",
         "photo_predict": "sdfsdfsdf",
         "annotations": [
            {
               "area": 264.0,
               "bbox": "213,123,123,33",
               "segmentation": "[1,2,3,4,5,6,11,22,fff]",
               "category_id": 2
            }
         ]
      }
}

polygon = [76.0, 196.0, 143.0, 68.0, 208.0, 202.0, 76.0, 196.0]
train_mask = np.zeros((512, 512, 3), dtype=np.uint8)
img = Image.fromarray(train_mask)
ImageDraw.Draw(img).polygon(polygon, fill="#ffffff", outline='white')
plt.imshow(img)
plt.show()

