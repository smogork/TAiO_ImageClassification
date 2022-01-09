#! /bin/bash

./main.py training data/AsphaltObstacles/AsphaltObstacles_TRAIN.arff data/AsphaltObstacles/AsphaltObstacles_TEST.arff -o results/asphalt.keras | tail -20 > results/asphalt.out
./main.py training data/EthanolLevel/EthanolLevel_TRAIN.arff data/EthanolLevel/EthanolLevel_TEST.arff -o results/ethanol.keras | tail -20 > results/ethanol.out
./main.py training data/AbnormalHeartbeat/AbnormalHeartbeat_TRAIN.arff data/AbnormalHeartbeat/AbnormalHeartbeat_TEST.arff -o results/heartbeat.keras | tail -20 > results/heartbeat.out
./main.py training data/Ham/Ham_TRAIN.arff data/Ham/Ham_TEST.arff -o results/ham.keras | tail -20 > results/ham.out
./main.py training data/InlineSkate/InlineSkate_TRAIN.arff data/InlineSkate/InlineSkate_TEST.arff -o results/skate.keras | tail -20 > results/skate.out