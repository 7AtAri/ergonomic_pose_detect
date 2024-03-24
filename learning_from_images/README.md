
# Project Documentation: Ergonomic Pose Detection

Vipin Singh and Ari Wahl

## 1. Idea
...

[color feedback frame for MacOs](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/frame_MacOs2.py)

## 2. Presentation Slides
...

## 3. Dataset 

For this project we set up our own [dataset](https://drive.google.com/drive/folders/1Y0OnUDHBActc6P7XW9Hmb9VlPYdpXWmq?usp=sharing) with 118 images, that were manually annotated with regards of ergonomic posture. The postures are labeled with according to the [RULA worksheet](https://ergo-plus.com/wp-content/uploads/RULA.pdf). We used all deskwork related scorings from the rulesheet. 


## 4. Code

Disclaimer: All the training had to be done on a local machine, because the university cluster is at the moment not accessible due to a cyber attack. This puts heavy computational restraints on our work, especially with regard to the fine-tuning.

### 4.1 Keypoint Visualization 

We started the project by gaining a first glimpses into the functionalities and possibilities of pose estimation. Therefore we created a [notebook to visualize the keypoints](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/visualize_keypoints_example.ipynb) on our own dataset with Ultralytics' YOLOv8-Pose.

RTMpose-wholebody vs YOLOv8-Pose:

<p align="center">
  <img src="https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/output_images_mock_up/rtmw_kp_vipin.png" width="300px"/>
  <img src="https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/output_images_mock_up/vipin_red2_kps.jpg" width="300px"/>
</p>

### 4.2 Model Inspection and Expermiments

We needed to find out where to cut the YOLOv8 Pose Layers for our fine-tuning.
This turned out to be quite complicated, since the YOLO models seem to come with
an ultralytics wrapper, whose source code is not open. After some experiments, we managed to cut the model after the pose head but before the final keypoints are outputted. There is a way to cut the YOLO model at any other point. But then the YOLO wrapper will be lost, and the model does not work anymore. 
We also looked inside the RTMpose-wholebody model and realized it has a size of >30 million parameters.
Since the fine-tuning of YOLOv8 already took almost all V-RAM, we then knew, that we were not able to fine-tune the model on the local machine.
But in general it seemed to be easier to cut with the model instact, since it has two final linear layers, that are probably used to calculate the keypoints. This is not the case with YOLOv8 pose, which oddly ends with a convolutional layer whose output is then probably processed in a (non-accessible) Wrapper.
You can find our model inspection notebook [here](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/pytorch_model_inspection.ipynb) and our YOLO model slicing notebook [here](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/yolo_model_slicing.ipynb). 

### 4.3 Hyperparameter Optimization

To find the best hyperparameters, we used the optuna framework.
Finally, we only used a grid search algorithm, but it is easy to just switch the
search algorithm, to take advantage of all the possibilities that optuna offers.
Take a look at our HPO setup in our notebooks for [YOLO HPO](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/yolo_hpo.ipynb) and for [MMPose](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/mmpose_hpo.ipynb) if you like.
After an initial HPO of our models, we realized that setting a seed heavily influenced our results.

### 4.4 Model Training and Evaluations

(YOLOv8 Pose and MMPose - rtm wholebody)

After putting up notebooks for every single pipeline, we set up one singular clean notebook with our main training and evluation setup for an [all model comparison](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/all_model_comparison.ipynb). Please use this notebook as the main reference for our project.


## 5. Final results
...

## 6. Sources

We collected some links for our [sources](learning_from_images/sources.md), as well as links for our
Base-Model's documentation:
- [YOLOv8 documentation](https://docs.ultralytics.com/tasks/pose/#models)
- [MMPose documentation](https://mmpose.readthedocs.io/en/latest/overview.html)
