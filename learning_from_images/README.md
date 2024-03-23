
# Learning from Images project

## Idea
...

[color feedback frame for MacOs](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/frame_MacOs2.py)

## Presentation Slides
...

## Dataset 

For this project we set up our own [dataset](https://drive.google.com/drive/folders/1Y0OnUDHBActc6P7XW9Hmb9VlPYdpXWmq?usp=sharing) with 120 images, that were manually annotated with regards of ergonomic posture. The postures are labeled with according to the [RULA worksheet](https://ergo-plus.com/wp-content/uploads/RULA.pdf).


## Code

### Keypoint Visualization 

To gain a first glimpse into the functionalities and possibilities of pose estimation, we put up a [notebook to visualize keypoints](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/visualize_keypoints_example.ipynb) on our own dataset.

### Model Inspection and Expermiments

We needed to find out where to cut the YOLOv8 Pose Layers for our fine-tuning.
This turned out to be quite complicated, since the YOLO models seem to come with
an ultralytics wrapper, whose source code is not open. After some experiments, we managed to cut the model after the pose head but before the final keypoints are outputted.  
You can find our model inspection notebook [here](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/pytorch_model_inspection.ipynb) and our YOLO model slicing notebook [here](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/yolo_model_slicing.ipynb).

### Hyperparameter Optimization

To find the best hyperparameters, we used the optuna framework.
Finally, we only used a grid search algorithm, but it is easy to just switch the
search algorithm, to take advantage of all the possibilities that optuna offers.
Take a look at our HPO setup in our notebooks for [YOLO HPO](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/yolo_hpo.ipynb) and for [MMPose](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/mmpose_hpo.ipynb) if you like.


### Model Training and Evaluations

(YOLOv8 Pose and MMPose - rtm wholebody)

After putting up notebooks for every single pipeline, we set up one singular clean notebook with our main training and evluation setup for an [all model comparison](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/all_model_comparison.ipynb). Please use this notebook as the main reference for our project.


### Final results
...

### Sources

We collected some links for our [sources](learning_from_images/sources.md), as well as links for our
Base-Model's documentation:
- [YOLOv8 documentation](https://docs.ultralytics.com/tasks/pose/#models)
- [MMPose documentation](https://mmpose.readthedocs.io/en/latest/overview.html)
