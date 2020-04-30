#----------------
# Getting base paperspace tenserflow image
FROM tensorflow/tensorflow:2.0.0a0-gpu-py3-jupyter

WORKDIR /app

RUN pip install bert-for-tf2
RUN pip install pandas



#ADD ./bert_model.py /app  if we use -v we don't need to add this line

#----------------------------
# happens in dockers run
CMD python bert_model.py
