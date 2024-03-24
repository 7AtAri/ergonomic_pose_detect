# ergonomic posture detection

- for learning from images ([documentation](https://github.com/7AtAri/ergonomic_pose_detect/tree/main/learning_from_images))
- for business values 

## Idea

Since desk jobs require long hours of sitting on each workday, ergonomic sitting can help prevent cronic backpain. Especially for remote work, where ergonomic furniture is often missing and people can work on their couch, ergonomic posture detection for the workplace can make a difference.

## Sources

- [sources](learning_from_images/sources.md)

## todo checklist / Steps 

- [x] set up our own [dataset](https://drive.google.com/drive/folders/1Y0OnUDHBActc6P7XW9Hmb9VlPYdpXWmq?usp=sharing)

- [x] implement fine-tuning pipeline for yolo as feature extractor

- [x] find yolo with cut off point and add classification head
    
- [x] implement yolo fine-tuning

- [x] keypoint angle calculation + rula rule assessment of ergonomic status

- [x] implement sota model - Whole Body Keypoints(mmpose) 

- [x] evaluation set up with metrics (see idea presentation)

- [x] yolo keypoint model training

- [x] yolo keypoint angle model training

- [x] yolo finetuning training

- [x] mmpose sota model keypoint model training

- [x] mmpose sota model finetuning (discarded, because of too large model size for local computing)

- [x] prepare keynote/ppt presentation

## Out created dataset

You can find the dataset we created for posture estimation on [BHT cloud](https://cloud.bht-berlin.de/index.php/s/3HTdw2MXqFR5SJy).
The postures are labeled with respect to the [RULA worksheet](https://ergo-plus.com/wp-content/uploads/RULA.pdf)

## Base-Model documentations

- [YOLOv8 documentation](https://docs.ultralytics.com/tasks/pose/#models)
- [MMPose documentation](https://mmpose.readthedocs.io/en/latest/overview.html)

## Business Model proposal for the final presentation of the "Business Values" module

- [presentation](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/business%20values/presentation/PoseFix.pdf)
- [report](https://github.com/7AtAri/ergonomic_pose_detect/blob/main/business%20values/report/main.pdf)
