FROM ghcr.io/nslythe/docker-base:latest

ARG DEBIAN_FRONTEND=noninteractive

ENV EULA=false

RUN apt-get update && apt-get install -y openjdk-16-jdk openjdk-8-jre-headless

ADD https://launcher.mojang.com/v1/objects/0a269b5f2c5b93b1712d0f5dc43b6182b9ab254e/server.jar /server.jar

COPY root /

VOLUME /config

EXPOSE 25565

