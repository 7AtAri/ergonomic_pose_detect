
# Project Documentation: Ergonomic Pose Detection

Vipin Singh and Ari Wahl

## 1. Idea

Since desk jobs require long hours of sitting on each workday, ergonomic sitting can help prevent cronic backpain. Especially for remote work, where ergonomic furniture is often missing and people can work on their couch, ergonomic posture detection for the workplace can make a difference. 

## 2. Presentation Slides
...

## 3. Dataset 

### 3.1 Dataset Curation
For this project we set up our own [dataset](https://drive.google.com/drive/folders/1Y0OnUDHBActc6P7XW9Hmb9VlPYdpXWmq?usp=sharing) with 118 images, that were manually annotated with regards of ergonomic posture. The postures are labeled with according to the RULA worksheet. We used all deskwork related scorings from the rulesheet. 

 <img src="https://github.com/7AtAri/ergonomic_pose_detect/blob/report/learning_from_images/präsi/RULA_2.png" width="600px"/>


### 3.2 Splitting the Dataset

To be able to do a final evaluation, as well as a hyperparameter optimization, we needed to do a train, validation and test set split. Since we used a 5-fold cross validation, first only split into the training and testing set. Therefore we used an 80% to 20% split, with 80% being used for training and 20% used for testing the model. The HPO was then done with only the 80% of training data, further split into training and validation set.

## 4. Code

Disclaimer: All the training had to be done on a local machine, because the university cluster is not accessible at the moment due to a cyber attack. This puts heavy computational restraints on our work, especially with regard to model fine-tuning.

### 4.1 Keypoint Visualization 

For the start of the project we needed to get a first glimpse into the functionalities and possibilities of pose estimation. Therefore we created a [notebook to visualize the keypoints](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/visualize_keypoints_example.ipynb) on our own dataset with Ultralytics' YOLOv8-Pose.

RTMpose-wholebody vs YOLOv8-Pose:

<p align="center">
  <img src="https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/output_images_mock_up/rtmw_kp_vipin.png" width="300px"/>
  <img src="https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/output_images_mock_up/vipin_red2_kps.jpg" width="300px"/>
</p>

### 4.2 Model Inspection and Experiments

To fine-tune YOLOv8-pose, it is necessary to find a good point to cut the YOLOv8-Pose Layers from the original model and to add our classification head. Unfortunately for the YOLOv8 model family this turned out to be quite complicated, since the YOLO models seem to come with an ultralytics wrapper, whose source code is not open. After some experiments, we managed to cut the model after the pose head but before the final keypoints are outputted. It is in general also possible to cut the YOLO model at any other point. But then the YOLO wrapper will be lost, and this results in the model not working properly anymore. So, after model inspection, we decided to take the only possible option to cut the YOLOv8-pose model.
For the task of fine-tuning the RTMpose-wholebody model, we printed a model summary and realized it has a size of >30 million parameters. Since the fine-tuning of YOLOv8 already took almost all V-RAM, we then knew, that we were not able to fine-tune the model on the local machine. But in general it seems to be a lot easier to cut with the model instact, since it has two final linear layers, that are probably used to calculate the keypoints. The MMPose framework, where we got the RTMpose-wholebody model from, also has implemented backbone, neck and head methods, which make the MMPose models quite accessible for fine-tuning. This is not the case with YOLOv8 pose, which oddly ends with a convolutional layer whose output is then probably processed in a (non-accessible) wrapper method, that comes with the ultralytics package.
You can find our model inspection notebook [here](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/pytorch_model_inspection.ipynb) and our YOLO model slicing notebook [here](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/yolo_model_slicing.ipynb). 

### 4.3 Hyperparameter Optimization

To find the best hyperparameters, we used the optuna framework. Finally, we only used a grid search algorithm, but it is easy to just switch the search algorithm, to take advantage of all the possibilities that optuna offers. Take a look at our HPO setup in our notebooks for [YOLO HPO](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/yolo_hpo.ipynb) and for [MMPose](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/mmpose_hpo.ipynb) if you like.
After an initial HPO of our models, we realized that setting a seed heavily influenced our results. Due to computational restraints we then didn't rerun our HPO including the seed, which would be the better approach, but resided to now just do another HPO on the seed for all the models while keeping the initial other best parameters fixed. You will find this seed optimization notebook [here](https://github.com/7AtAri/ergonomic_pose_detect/blob/report/learning_from_images/src/hpo_model_seeds.ipynb).

#### Best Hypeparameter:
- YOLOv8-Pose:
  - KeypointClassifier: ```{'lr': 0.0001, 'h1': 512, 'h2': 1024, 'batch_size': 4, 'num_epochs': 300, 'seed' : 1986}```
  - KeypointScorer: ```{'lr': 0.001, 'h1': 256, 'h2': 256, 'batch_size': 16, 'num_epochs': 200, 'seed' : 13}```

- RTMpose-Wholebody:
  - KeypointClassifier: ```{'lr': 0.001, 'h1': 1024, 'h2': 512, 'batch_size': 16, 'num_epochs': 100, 'seed': 23}```
  - KeypointScorer: ```{'lr': 5e-05, 'h1': 512, 'h2': 1024, 'batch_size': 4, 'num_epochs': 200, 'seed': 1986}```

### 4.4 Model Training 

(YOLOv8 Pose and RTMpose-wholebody)

After putting up notebooks for every single pipeline, we set up one singular clean notebook with our main training and evluation setup for an [all model comparison](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/all_model_comparison.ipynb). Please use this notebook as the main reference for our project.

#### 4.4.1 Feature Extraction

As a first step we used the 7 scores of the RULA worksheet directly to get a scoring/regression model. 
This is possible because the RULA scores is an ordinary discrete scale that can be interpreted as a continous scale. The hypothesis was, that this would be a fine grained insight into the egronomics of a posture. We tried this approach for the YOLOv8-pose model as well as for the RTMpose-wholebody model. 

#### 4.4.1 Fine-Tuning
...

### 4.5 Evaluation
...

## 5. Final results
...

## 6. Sources

We collected some links for our [sources](learning_from_images/sources.md), as well as links for our
Base-Model's documentation:
- [YOLOv8 documentation](https://docs.ultralytics.com/tasks/pose/#models)
- [MMPose documentation](https://mmpose.readthedocs.io/en/latest/overview.html)
- [fine-tuning MMPose Models](https://mmpose.readthedocs.io/en/latest/advanced_guides/implement_new_models.html)
