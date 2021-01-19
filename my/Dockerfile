#ubuntu  python3.7
FROM tensorflow/tensorflow:1.13.2-py3
RUN apt-get update
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata mc
#RUN apt-get install python3-venv -y
RUN apt-get install -y mongodb -y

RUN pip3 install --upgrade pip
RUN pip3 install wheel

RUN pip3 install numpy==1.16.3
RUN pip3 install arctic==1.74.0
RUN pip3 install gym==0.12.1
RUN pip3 install h5py==2.9.0
RUN pip3 install Keras==2.2.4
RUN pip3 install Keras-Applications==1.0.7
RUN pip3 install Keras-Preprocessing==1.0.9
RUN pip3 install keras-rl==0.4.2
RUN pip3 install more-itertools==6.0.0
RUN pip3 install pandas==0.24.1
RUN pip3 install pymongo==3.7.2
RUN pip3 install pytest==4.3.0
RUN pip3 install python-dateutil==2.8.0
RUN pip3 install pytz==2018.9
RUN pip3 install requests==2.21.0
RUN pip3 install scipy==1.2.1
RUN pip3 install sortedcontainers==2.1.0
RUN pip3 install tensorboard==1.13.1
RUN pip3 install tensorflow-estimator==1.13.0
RUN pip3 install tzlocal==1.5.1
RUN pip3 install urllib3==1.24.2
RUN pip3 install websockets==7.0
RUN pip3 install Cython==0.29.21
RUN pip3 install matplotlib
RUN pip3 install scikit-learn


