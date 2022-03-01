FROM pytorch/pytorch:1.8.0-cuda11.1-cudnn8-devel
RUN apt-get update
RUN apt-get install -y --no-install-recommends graphviz
RUN conda install --channel defaults conda python=3.8 --yes
RUN conda update --channel defaults --all --yes
RUN conda update -n base -c defaults conda
RUN conda install -c anaconda pandas  ipykernel
RUN conda install dask cudatoolkit=11.3 pytorch torchvision torchaudio -c pytorch
COPY ./pykg2vec ./
RUN python setup.py install
