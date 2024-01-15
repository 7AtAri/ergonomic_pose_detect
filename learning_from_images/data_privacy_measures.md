We need to ensure that the privacy of our customers is kept safe. Therefore we propose a preprocessing of the videofeed within the app to so that only privacy-preserved data leaves the users device and ends up in the cloud where it is inserted into the machine learning model.

or federated learning approach:
run machine learning with data that remains at the source:
[PySyft](https://github.com/OpenMined/PySyft)

more federated learning approaches:
https://github.com/chaoyanghe/Awesome-Federated-Learning

Privacy-Preserving Machine Learning with Fully Homomorphic Encryption for Deep Neural Network:
https://arxiv.org/pdf/2106.07229.pdf
python implementation for homomorphic encryption: [PySeal](https://github.com/Lab41/PySEAL)

or:

* https://easyeasy.medium.com/protecting-privacy-a-comprehensive-guide-to-video-anonymization-for-ai-training-4b85fb23a61d

maybe use a GAN and do a style transfer on the user end: (probably easier to just use the pose estimation on the mobile phone and send only calculated keypoints - of closest human to the camera?)

* https://openaccess.thecvf.com/content/CVPR2023W/ECV/papers/Jia_BlazeStyleGAN_A_Real-Time_On-Device_StyleGAN_CVPRW_2023_paper.pdf
