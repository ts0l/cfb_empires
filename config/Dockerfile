FROM jupyter/scipy-notebook

LABEL Name=cfb_empires Version=0.0.1
EXPOSE 3000

WORKDIR /app
ADD . /app

RUN conda install pylint geopy autopep8 rope
RUN pip install CFBScrapy