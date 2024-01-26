# MLE-Zoomcamp-M12-DTC-Zoomcamp-Q-A-Text-Classification-Capstone-Project

## Dataset Description

> https://www.kaggle.com/competitions/dtc-zoomcamp-qa-challenge/data

The dataset for the DataTalks.Club Q&A Matching Challenge consists of four CSV files and an attachments folder. These files contain questions and answers from DataTalks.Club courses, along with relevant metadata. Participants are expected to use these files to develop models that can accurately match questions to their correct answers.

### train_questions.csv:

- Purpose: This file is used for training your model. It contains the questions along with metadata and the correct answer IDs.
- Columns:
    - question_id: A unique identifier for each question.
    - question: The text of the question.
    - course: The specific course from which the question was sourced.
    - year: The year in which the course was conducted.
    - candidate_answers: A list of answer IDs that are potential matches for the question.
    - answer_id: The ID of the actual correct answer for the question.

### train_answers.csv:

- Purpose: This file provides the answers for training, corresponding to the questions in train_questions.csv.
- Columns:
    - answer_id: A unique identifier for each answer.
    - answer: The text of the answer.
    - course: The specific course from which the answer was sourced.
    - year: The year in which the course was conducted.
    - attachments_files: Names of any attachment files related to the answer, including images.

### test_questions.csv:

- Purpose: Contains questions for evaluating your model's performance. It does not include the correct answer IDs.
- Columns: Same as train_questions.csv, but excluding the answer_id column.

### test_answers.csv:

- Purpose: Provides the answers for the test set. Participants need to match these answers to the questions in test_questions.csv.
- Columns: Same as train_answers.csv.


## Attachments Folder:

- Contents: Contains all the attachment files that are referenced in the answers. This includes images and potentially other types of files.
- Usage: These attachments are part of some answers and can be critical for correctly matching questions to answers, especially for questions where visual context is important.

Participants are encouraged to explore and utilize the rich information available in these files, including textual content, course context, and temporal data, to develop robust models capable of accurately matching questions and answers.


## External Data Usage

### Allowing External Data:

- Policy: In this competition, the use of external data is not only allowed but also encouraged. Participants are welcome to augment the provided dataset with additional relevant sources to enhance their models.
- Sharing Requirement: If you use external data, you are required to share the details and sources of this data with the community. This sharing should be done both on the Kaggle forum and on the DataTalks.Club (DTC) Slack channel.

### Examples of External Data:
- Slack Dump: Conversations and Q&A sessions from relevant Slack channels that pertain to data science and the topics covered in DataTalks.Club courses.
- ZoomCamp Q&A Google Documents: Documents containing Q&A sessions from ZoomCamp courses or similar educational activities.
- YouTube Videos (as text): Transcripts or textual analysis of YouTube videos that are relevant to the course content or the subject of the questions in the dataset.

### Purpose and Benefits:

- Enhancing Models: External data can provide additional context, variations in language use, and broader coverage of topics, which can be crucial for building more robust and accurate models.
- Community Learning: Sharing external data sources fosters a collaborative environment where all participants can learn from each other and build upon a diverse set of data.

Participants are encouraged to be creative and thoughtful in selecting external data that can genuinely contribute to the challenge's objective. The goal is to not only improve individual model performance but also to enrich the collective resources available to all competitors.


---


# Project Structure

The project is organized into CRISP-DM phases for effective development and documentation.

## Table of Contents

1. [Business Understanding](#business-understanding)
2. [Data Understanding](#data-understanding)
3. [Data Preparation](#data-preparation)
4. [Modeling](#modeling)
5. [Evaluation](#evaluation)
6. [Deployment](#deployment)
7. [Conclusion](#conclusion)

---

## Business Understanding

### Project Name

- **GitHub Repo:** [Car Damage Image Classification Capstone Project](https://github.com/yourusername/multiclass-classification)
- **Project Notebook:** [Car_Damage Image_Multi_Class_Classification.ipynb](path/to/your/notebook.ipynb)

### Problem Statement

The DataTalks.Club Q&A Matching Challenge aims to develop models that can accurately match questions to their correct answers within the context of DataTalks.Club courses. The challenge provides a dataset containing questions, answers, and metadata from these courses.

### Objective

The goal is to build robust models capable of accurately matching questions to answers. Participants are encouraged to utilize the rich information available in the dataset, including textual content, course context, and temporal data.

### External Data Usage

Participants are allowed and encouraged to use external data to enhance their models. The use of external data can provide additional context, variations in language use, and broader coverage of topics. Sharing details and sources of external data is a requirement to foster a collaborative learning environment.

---

## Data Understanding

### Dataset Overview

The dataset consists of four CSV files and an attachments folder:

- train_questions.csv: Training data with questions, metadata, and correct answer IDs.
- train_answers.csv: Training data with answers corresponding to the questions in train_questions.csv.
- test_questions.csv: Test data with questions for model evaluation.
- test_answers.csv: Test data with correct answers corresponding to the questions in test_questions.csv.
- Attachments Folder: Contains files referenced in answers, including images.

### Attachments

The Attachments Folder contains files referenced in answers. These attachments, including images, can be crucial for correctly matching questions to answers, especially for questions where visual context is important.

---

## Data Preparation

### Data Preprocessing

Clean and preprocess the data, handling missing values, and ensuring consistency in formats.


### Feature Engineering

Explore opportunities for feature engineering, considering the text of questions and answers, course context, and temporal data.

### External Data Integration

Participants are encouraged to use external data to enhance their models. Details and sources of external data should be shared with the community.


---

## Modeling

### Model Selection

Choose appropriate models for question-answer matching, considering the nature of the data (text, metadata, attachments).

### Hyperparameter Tuning

- Change Learning Rate
- Adding more layers
    - Different Pooling
    - Dense Layer
    - SpatialDropout2D
    - Dropout
    - BatchNormalization

### Model Development

Train models using the training data (train_questions.csv and train_answers.csv) and explore the use of external data to improve model performance.


---


## Evaluation

### Performance Metrics

Evaluate models using relevant metrics for question-answer matching. Consider both accuracy and contextual relevance.



### Evaluate models using relevant metrics for question-answer matching. Consider both accuracy and contextual relevance.

Apply models to the test set (test_questions.csv), matching questions to correct answers, and evaluate performance.


---

## Deployment

### Model Deployment

Enviroment:
  - requirements.txt
  - Pipfile.lock


```sh
transformers==4.36.2
tflite_runtime==2.14.0
numpy==1.24.3


pip install -r requirements.txt
```

#### Preparing Docker Image

- https://repost.aws/knowledge-center/lambda-container-images

Build docker image using the recommended public image for Lambda once Dockerfile has been created below:

```sh
docker build -t dtc-zoomcamp-q-a-challenge .
```

To test first run image that was built:

```sh
docker run -it --rm -p 8080:8080 dtc-zoomcamp-q-a-challenge:latest
```

#### Docker Hub

```sh
# Tag the Existing Image, username/car-insurance-model:new-tag
docker tag dtc-zoomcamp-q-a-challenge:latest developerhost/dtc-zoomcamp-q-a-challenge:latest

# Push the newly tagged image to Docker Hub:
docker push developerhost/dtc-zoomcamp-q-a-challenge:latest

# you can pull the image:
docker pull developerhost/dtc-zoomcamp-q-a-challenge:latest
```

#### test.py created per AWS documentation for testing

lambda function a function must be added as below to the lambda_function.py file:

```py
def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result
```

Run the file:

```sh
python client_to_docker_test.py
```

This is the output I recieved which clearly shows that the image was predicted as a "dent" which is correct:

```py
{
  "question": "That is a happy person",
  "results": [
    {
      "answer": "That is a happy dog",
      "similarity": "0.760"
    },
    {
      "answer": "That is a very happy person",
      "similarity": "0.971"
    },
    {
      "answer": "Today is a sunny day",
      "similarity": "0.355"
    }
  ]
}
```


#### Testing function for Lambda

output:

```sh
# python client_to_docker_test.py


{
  "question": "That is a happy person",
  "results": [
    {
      "answer": "That is a happy dog",
      "similarity": "0.760"
    },
    {
      "answer": "That is a very happy person",
      "similarity": "0.971"
    },
    {
      "answer": "Today is a sunny day",
      "similarity": "0.355"
    }
  ]
}
```


### AWS Lambda Cloud Image


<!-- 
### Monitoring

- Continuous monitoring strategies.
-->

---

## Conclusion
<!-- 
### Summary

- Recap of the project.
- Achievements and challenges.
 -->
