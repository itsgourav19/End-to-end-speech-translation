# End-to-end-speech-translation

<h5> The code for a novel method of translating voice from one language to another without the need for intermediary text transcriptions in the latent space is contained in this repository. Our approach, which makes use of generative models, provides a smooth and precise translation experience.</h5>

**Summary:**
 
Conventional voice translation systems usually require more than one stage, such as text translation once audio is converted to text using speech recognition. But every step along the way, this method introduces mistakes and constraints. By translating voice to speech directly, our approach aims to get around these problems and enable more precise and effective translation.

**Conditions**

You'll need the following in order to run the code in this repository:

Python 3.x (or above)

PyTorch (more than 1.8)

Hugging Face Transformers library (version >= 4.0)

Librosa (more than 0.8)

Additional dependencies listed in requirements.txt

**Usage**

Data Preparation: Make sure the source and destination languages have appropriate parallel speech datasets available to you. As needed, preprocess the data.

Model Training: Use the included scripts to train the generative models. As necessary, modify the model architectures and hyperparameters.

Evaluation: To gauge translation performance, test the trained models using held-out test data. Evaluation metrics include MOS (Mean Opinion Score), WER (Word Error Rate), and BLEU score.

Inference: Apply the learned models to fresh voice inputs in batch or real-time. Observe the translation quality and make any required adjustments.

**Citations:**
Li, J. and others (2022). Direct Translation of Speech to Speech Using Generative Models. The International Conference on Machine Learning (ICML) Proceedings


#Resources used are:---





[1.pdf](https://github.com/itsgourav19/End-to-end-speech-translation/files/14622024/1.pdf)

[2.pdf](https://github.com/itsgourav19/End-to-end-speech-translation/files/14622028/2.pdf)

[3.pdf](https://github.com/itsgourav19/End-to-end-speech-translation/files/14622027/3.pdf)

[4.pdf](https://github.com/itsgourav19/End-to-end-speech-translation/files/14622026/4.pdf)

[5.pdf](https://github.com/itsgourav19/End-to-end-speech-translation/files/14622025/5.pdf)
