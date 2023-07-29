# Fake-Job-detection (BERT model)
The BERT model is applied for Fake-job detection and successfully fine-tuned with three different loss functions which are:
* Cross Entropy loss
* Cross Entropy loss with class weights integration to handle an unbalanced set that is obvious in the chosen dataset
* Sadice loss

  
After successful training, the trained model is packaged into a container using Dockerfile a flask to create endpoint access. GitHub Actions is integrated to facilitate Continuous Integration with the help of Makefile while the continuous delivery will be implemented in AWS using AWS Elastic Container Registry and AppRunner. For the model inference in real-time, only the *url* of the job post will be provided by the client, the model will scrap the website and obtain the required information that will be used to determine if the job post is real or fake.
