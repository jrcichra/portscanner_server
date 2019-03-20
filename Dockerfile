FROM ubuntu:latest

MAINTAINER Justin Cichra

RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    git \
    gcc \
    clang \
    g++ \
    libegl1-mesa \ 
    libgl1-mesa-dev \
    libglu1-mesa \
    libglu1-mesa-dev \
    libsfml-dev \
    libgtest-dev \
    binutils-dev \
    libtool \
    lua5.2 \
    liblua5.2-dev \
    liblua5.2-0 \
    graphviz \
    doxygen

ADD main.cpp /
EXPOSE 5555
RUN g++ main.cpp -o main -lsfml-system -lsfml-network
CMD ["./main"]
