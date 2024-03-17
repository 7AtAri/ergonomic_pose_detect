# ergonomic posture detection

- for learning from images

- [important links](learning_from_images/todo.md)

## todo checklist

- [x] set up own dataset

- [x] add additional images into the dataset class folders

- [x] add drive link to the [dataset](https://drive.google.com/drive/folders/1Y0OnUDHBActc6P7XW9Hmb9VlPYdpXWmq?usp=sharing)

- [x] split our dataset into training/testing dataset

- [x] implement fine-tuning pipeline for yolo as feature extractor

- [ ] adapt fine-tuning pipeline for frozen yolo with keypoint layer cut off and only classification head (Ari)

- [x] keypoint angle calculation + rula rule assessment of ergonomic status

- [ ] implement mediapipe in our fine-tune pipeline (Fallback)

- [ ] implement sota models - Whole Body Keypoints(mmpose) (Vipin)

- [x] evaluation set up with metrics (see idea presentation)

- [ ] experiment with additional ordinal loss

- [ ] yolo keypoint model training

- [ ] yolo keypoint angle model training

- [ ] yolo finetuning

- [ ] mmpose sota model keypoint model training

- [ ] mmpose sota model finetuning

- [ ] prepare keynote/ppt presentation

## Out created dataset

You can find the dataset we created for posture estimation on [BHT cloud](https://cloud.bht-berlin.de/index.php/s/3HTdw2MXqFR5SJy).
The postures are labeled with respect to the [RULA worksheet](https://ergo-plus.com/wp-content/uploads/RULA.pdf)

## Model documentations

- [YOLOv8 documentation](https://docs.ultralytics.com/tasks/pose/#models)

## Business Model proposal

- [presentation](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/business%20values/presentation/PoseFix.pdf)
- [report](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/business%20values/report/main.pdf)
