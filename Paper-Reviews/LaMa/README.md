## [LaMa] Resolution-robust Large Mask Inpainting with Fourier Convolutions (CVPR 22)
### Abstract
Inpainting system struggle with  
1. large missing areas 2. complex geometric structures 3. high-resolution images  
Reasons: the lack of an effective receptive field in both the inpainting network and the loss function  
  
-> Suggests: large mask inpainting (LaMa)  
1) a new inpainting network architecture that uses fast Fourier convolutions (FFCs), which have the image-wide receptive field  
2) a high receptive field perceptual loss  
3) large training masks, which unlocks the potential of the first two components  
### 1. Introduction
Details of three main components of LaMa  
1) the high receptive field architecture using FFC  
FFCs allow for a receptive field that covers an entire image even in the early layers of the network.  
The inductive bias of FFC allows the network to generalize to high resolutions that are never seen during training.  
2) the high receptive field loss function "Perceptual loss"  
promotes the consistency of global structures and shapes  
3) the aggressive algorithm of training masks generation  

### 2. Method
#### 2.1 Global context within early layers
Fast Fourier convolution (FFC) is the operator that allows to use global context in early layers.  
FFC splits channels into two parallel branches  
1) local branch uses conventional convolutions  
2) global branch uses real FFT to account for global context  
  
FFCs allow the generator to account for the global context starting from the early layers.  
FFCs are well suited to capture periodic structures.
...