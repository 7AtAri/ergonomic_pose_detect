# ergonomic posture detection

- for learning from images

- [important links](learning_from_images/todo.md)

## todo checklist

- [x] set up own dataset

- [x] add additional images into the dataset class folders

- [x] split our dataset into training/testing dataset

- [x] implement fine-tuning pipeline for yolo as feature extractor

- [ ] adapt fine-tuning pipeline for frozen yolo with keypoint layer cut off and only classification head

- [x] keypoint angle calculation + rula rule assessment of ergonomic status

- [ ] ?implement simple pytorch model as baseline (may not be useful)

- [ ] (implement mediapipe in our fine-tune pipeline)

- [ ] implement fine-tuning pipeline for other state-of-the-art (SOTA) model

- [x] evaluation set up with metrics (see idea presentation)

- [ ] experiment with additional ordinal loss

- [ ] train our models

- [ ] prepare keynote/ppt presentation

## Out created dataset

You can find the dataset we created for posture estimation on [BHT cloud](https://cloud.bht-berlin.de/index.php/s/3HTdw2MXqFR5SJy).
The postures are labeled with respect to the [RULA worksheet](https://ergo-plus.com/wp-content/uploads/RULA.pdf)

## Model documentations

- [YOLOv8 documentation](https://docs.ultralytics.com/tasks/pose/#models)

## Business Model proposal

- [presentation](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/business%20values/presentation/PoseFix.pdf)
- [report](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/business%20values/report/main.pdf)
