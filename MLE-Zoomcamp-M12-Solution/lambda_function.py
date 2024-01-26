#!/usr/bin/env python
# coding: utf-8

# !pip install -U https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl
import requests
import numpy as np
import tflite_runtime.interpreter as tflite
import json  # Import the json module
# Disable TensorFlow warnings, before you import tensorflow
import os; os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import gc; gc.collect()
from transformers import AutoTokenizer
# Use a tokenizer appropriate for your model (replace "bert-base-uncased" with your model name)
tokenizer = AutoTokenizer.from_pretrained('celik-muhammed/all-mpnet-base-v2-finetuned-dtc-zoomcamp')

# Load the TFLite model in TFLite Interpreter and allocate tensors.
interpreter = tflite.Interpreter(model_path='mpnet-dtc-zoomcamp_tfmodel.tflite')
interpreter.allocate_tensors()
infer  = interpreter.get_signature_runner("serving_default")

def query(payload):
    # Replace this random input with your actual question and answers
    question = payload['question']
    answers  = payload['answers']
    
    # Tokenize the question and answers
    tokenized_question = tokenizer(question, return_tensors="np", padding=True, truncation=True, max_length=128)
    output = infer(
        input_ids      = np.array(tokenized_question['input_ids'], dtype=np.int32), 
        attention_mask = np.array(tokenized_question['attention_mask'], dtype=np.int32)
    )['last_hidden_state'].squeeze()
    # Get the output data
    q_embedding = np.mean(output, axis=0)

    # Replace this with your actual processing of each answer
    a_embeddings = []
    for i, answer in enumerate(answers):
        # Process each answer with your model and obtain the embedding
        tokenized_answers  = tokenizer(answer, return_tensors="np", padding=True, truncation=True, max_length=128)
        output = infer(
            input_ids      = np.array(tokenized_answers['input_ids'], dtype=np.int32),
            attention_mask = np.array(tokenized_answers['attention_mask'], dtype=np.int32)
        )['last_hidden_state'].squeeze()
        a_embedding = np.mean(output, axis=0)

        # Calculate cosine similarity between the question and the current answer
        similarity = np.dot(q_embedding, a_embedding) / (np.linalg.norm(q_embedding) * np.linalg.norm(a_embedding))
        a_embeddings.append({"answer": answer, "similarity": f"{similarity:.3f}"})

    # Convert the result to a JSON-formatted string
    result_json = json.dumps({"question": question, "results": a_embeddings}, indent=2)
    return result_json

def lambda_handler(event, context):
    payload = event['inputs']
    result = query(payload)
    return result
