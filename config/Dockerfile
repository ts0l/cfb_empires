FROM jupyter/scipy-notebook

USER root

LABEL Name=cfb_empires Version=0.0.1
EXPOSE 3000

WORKDIR /app
ADD . /app

RUN wget https://github.com/plotly/orca/releases/download/v1.1.1/orca-1.1.1-x86_64.AppImage -P /home
RUN chmod 777 /home/orca-1.1.1-x86_64.AppImage 

# To avoid the need for FUSE, extract the AppImage into a directory (name squashfs-root by default)
RUN cd /home && /home/orca-1.1.1-x86_64.AppImage --appimage-extract
RUN printf '#!/bin/bash \nxvfb-run --auto-servernum --server-args "-screen 0 640x480x24" /home/squashfs-root/app/orca "$@"' > /usr/bin/orca
RUN chmod 777 /usr/bin/orca

RUN conda install pylint geopy autopep8 rope plotly geopandas pyshp
RUN conda install -c plotly plotly-geo plotly-orca
RUN pip install CFBScrapy
