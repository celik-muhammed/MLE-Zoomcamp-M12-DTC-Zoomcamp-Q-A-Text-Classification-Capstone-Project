# public image for Lambda
FROM public.ecr.aws/lambda/python:3.10

# Copy the Pipfile and Pipfile.lock into the container
# COPY ["requirements.txt", "./"]
# RUN pip install -r requirements.txt

# recompiled with the lambda image
RUN pip install --upgrade pip
RUN pip install -U https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl
RUN pip install -U transformers
RUN pip install -U numpy

# Copy function code and model into the container
COPY ["lambda_function.py", "mpnet-dtc-zoomcamp_tfmodel.tflite", "./"]

# Set the CMD to your handler 
CMD [ "lambda_function.lambda_handler" ]
