
# Project Documentation: Ergonomic Pose Detection

Vipin Singh and Ari Wahl

## 1. Idea

Since desk jobs require long hours of sitting on each workday, ergonomic sitting can help prevent chronic backpain. Especially for remote work, where ergonomic furniture is often missing and people can work on their couch, ergonomic posture detection for the workplace can make a difference. 

## 2. Presentation Slides

We presented our project and its results with these [slides](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/pr%C3%A4si/ergo_posture_pr%C3%A4si.pdf).
In these we explain the problem, our approaches and the challenges we faced.

## 3. Dataset 

### 3.1 Dataset Curation
For this project we set up our own [dataset](https://drive.google.com/drive/folders/1Y0OnUDHBActc6P7XW9Hmb9VlPYdpXWmq?usp=sharing) with 118 images, that were manually annotated with regards of ergonomic posture. The postures are labeled with according to the RULA worksheet. We used all deskwork related scorings from the rulesheet. 

 <img src="https://github.com/7AtAri/ergonomic_pose_detect/blob/report/learning_from_images/präsi/RULA_2.png" width="600px"/>


### 3.2 Splitting the Dataset

To be able to do a final evaluation, as well as a hyperparameter optimization, we needed to do a train, validation and test set split. Since we used a 5-fold cross validation, first only split into the training and testing set. Therefore we used an 80% to 20% split, with 80% being used for training and 20% used for testing the model. The HPO was then done with only the 80% of training data, further split into training and validation set.

## 4. Code

**Disclaimer:** All the training had to be done on a local machine, because the university cluster is not accessible at the moment due to a cyber attack. This puts heavy computational restraints on our work, especially with regard to model fine-tuning.

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
  - KeypointClassifier:\
  ```{'lr': 0.0001, 'h1': 512, 'h2': 1024, 'batch_size': 4, 'num_epochs': 300, 'seed' : 1986}```
  - KeypointScorer:\
  ```{'lr': 0.001, 'h1': 256, 'h2': 256, 'batch_size': 16, 'num_epochs': 200, 'seed' : 13}```

- RTMpose-Wholebody:
  - KeypointClassifier:\
  ```{'lr': 0.001, 'h1': 1024, 'h2': 512, 'batch_size': 16, 'num_epochs': 100, 'seed': 23}```
  - KeypointScorer:\
  ```{'lr': 5e-05, 'h1': 512, 'h2': 1024, 'batch_size': 4, 'num_epochs': 200, 'seed': 1986}```

For the YOLOv8-pose model fine-tuning approach, we could not do any HPO due to computational restraints.
We picked a few of the formerly good hyperparameters and took an educated guess on the others.

### 4.4 Model Training 

(YOLOv8 Pose and RTMpose-wholebody)

After putting up notebooks for every single pipeline, we set up one singular clean notebook with our main training and evluation setup for an [all model comparison](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/all_model_comparison.ipynb). Please use this notebook as the main reference for our project.

#### 4.4.1 Feature Extraction

Our first appraoch was to use the pretrained models just for inference and to extract the keypoints from the images.
The extracted keypoints would then be used as input data with our labels.
As a first step we defined two tasks for the feature extraction approach.
- **Scoring Task:**\
We use the 7 scores of the RULA worksheet directly to get a scoring/regression model.
This is possible because the RULA score is an ordinary discrete scale that can be interpreted as a continous scale.
The hypothesis was, that this would be a fine grained insight into the egronomics of a posture.
- **Classification Task:**\
We group the 7 scores of the RULA worksheet into three classes. This is done to get a more general insight into the ergonomics of a posture.
The hypothesis was, that this would be a more robust approach, since the RULA scores are quite subjective and the classes are more general.
The first class, we call it the "green" class, it describes a good posture, that can be kept for a long(er) period of time.
This class consists of RULA's score 1 and score 2. For the second class, we subsume the RULA scores 3 to 5. This class, we encode as "yellow" class and holds postures that should not be kept over longer periods of time.
Finally, the "red" class signals that the posture should be changed soon, even better immediately.
It groups the RULA scores 6 and 7.

With the tasks defined, we agreed on Neural Network architectures for the feature extraction.
For both tasks our architecture consists of three hidden layers.
The number of nodes in the first two hidden layers are configured as hyperparameters *h1* and *h2* that were optimized with [optuna](https://optuna.org).
The number of nodes in the third hidden layer are the half of the nodes in the second hidden layer.
After the first two layers we add a dropout layer with a dropout rate of 50%.
This is done to prevent overfitting.
The activation function for all three hidden layers is ReLU.
Finally we have one output layer that linearly transforms the output of the last hidden layer into the desired output space.
For the scoring task, we use a single output node, since we want to predict a single score.
For the classification task, we use three output nodes, since we want to predict three classes.

##### YOLOv8-Pose
The first model we used for feature extraction was the YOLOv8-Pose model.
This model outputs 17 keypoints on the whole body:
<p align="center">
  <img src="https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/output_images_mock_up/vipin_red2_kps.jpg" width="300px"/>
</p>

The best hyperparameter for our Scoring / Classification models were:
- KeypointClassifier:\
```{'lr': 0.0001, 'h1': 512, 'h2': 1024, 'batch_size': 4, 'num_epochs': 300, 'seed' : 1986}```
- KeypointScorer:\
```{'lr': 0.001, 'h1': 256, 'h2': 256, 'batch_size': 16, 'num_epochs': 200, 'seed' : 13}```

##### YOLOv8-Pose + Self calculated angles
For the next training approach we calculated specific angles that are important for ergonomic posture (according to RULA).
We calculated the angles between the following keypoints:

TODO: Add angle images to repo and paste here

After calculating the angles we concatenated them with the keypoints as input data.
We did not perform a separate Hyperparameter Optimization for this model, but used the best hyperparameters from the YOLOv8-Pose model.

##### RTMpose-wholebody
The second model we used to compare against YOLOv8-Pose is the RTMpose-wholebody model.
This model outputs 133 keypoints on the whole body:
<p align="center">
  <img src="https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/output_images_mock_up/rtmw_kp_vipin.png" width="300px"/>
</p>
Compared to YOLO it has a lot more keypoints especially in the face and the hand area.
Our hypothesis was that more keypoints would benefit the model to better capture the structure of the human pose.

The best hyperparameter for our Scoring / Classification models were:
- KeypointClassifier:\
  ```{'lr': 0.001, 'h1': 1024, 'h2': 512, 'batch_size': 16, 'num_epochs': 100, 'seed': 23}```
- KeypointScorer:\
  ```{'lr': 5e-05, 'h1': 512, 'h2': 1024, 'batch_size': 4, 'num_epochs': 200, 'seed': 1986}```

#### 4.4.2 Fine-Tuning 

Like we explained before, the fine-tuning approach on the local machine only worked for the YOLOv8-pose model. To make it work, we needed to reduce the size of input images to 256 x 352 pixels as well as the number of episodes to 50 and we also needed to discard the HPO. As hyperparameters we used a learning rate of $1e^{-4}$, a first hidden layer with 2048 nodes, a second one with 1024 nodes and a third one with 512 nodes and a seed of 13. 

### 4.5 Evaluation

#### 4.5.1 Classification Models

Since our 3 classes are balanced we used accuracy as a final metric. These are the confusion matrices for our four classification models: 

 <img src="https://github.com/7AtAri/ergonomic_pose_detect/blob/main/learning_from_images/src/plots/confusion_matrices.png" width="600px"/>

#### 4.5.2 Scoring Models
TODO Vipin

## 5. Final results
...

## 6. Sources

We collected some links for our [sources](learning_from_images/sources.md), as well as links for our
Base-Model's documentation:
- [YOLOv8 documentation](https://docs.ultralytics.com/tasks/pose/#models)
- [MMPose documentation](https://mmpose.readthedocs.io/en/latest/overview.html)
- [fine-tuning MMPose Models](https://mmpose.readthedocs.io/en/latest/advanced_guides/implement_new_models.html)
