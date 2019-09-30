# Precancerous-Tumer-Image-Detection-by-Deep-Learning-
<img src="demo.png">

This model was built on [Pytorch-UNet](https://github.com/milesial/Pytorch-UNet). Image data is available here: [data](https://polyp.grand-challenge.org/CVCClinicDB/).

This model implemented image segmentation with U-Net(convolutional networks for biomedical image segmentation) and was trained from scratch with 5000 images with data augmentation because originally there were only 500 images.

## Process
Augment the data to get 5000 images from 500 images (pip install Augmentor).
``
python imgaug.py
``
Normalize file name of image.
```
python normalize_id.py
```
Train the model
```
python train.py -g True -e 100 -b 32 -s 0.8
```
Predict a mask
```
python predict.py -i image1.jpg
```
## Performance
The model scored [dice coefficient](https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient) of 0.645.

###Confusion Matrix

| n=604  | Predicted: No  | Predicted: Yes  |
|---|---|---|
| **Predicted: No**  | 0  | 8 |
| **Predicted: Yes**  | 181  | 423  |

| Rate | Score |
| ------------- | ------------- |
| Accuracy:  | 0.69  |
| Presicion:  | 0.97  |
| Recall:  | 0.7  |
| F-Score:  | 0.81  |


