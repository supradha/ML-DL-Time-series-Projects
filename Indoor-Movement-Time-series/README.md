# Indoor-movement-Time-series

The Indoor Movement Time-series data from https://archive.ics.uci.edu/ml/datasets/Indoor+User+Movement+Prediction+from+RSS+data
UCI repository. This dataset represents a real-life benchmark in the area of Ambient Assisted Living applications.

Input data 
Input RSS streams are provided in files named MovementAAL_RSS_SEQID.csv, where IDSEQ is the progressive numeric sequence ID. 
In each file, each row corresponds to a time step measurement (temporal order) and contains the following information: 
RSS_anchor1, RSS_anchor2, RSS_anchor3, RSS_anchor4 

- Target data 
Target data is provided in the file MovementAAL_target.csv 
Each row in this file contains: sequence_ID, class_label 

- Dataset grouping 
Data is grouped in 3 sets,MovementAAL_DatasetGroup.csv, provides information about such data grouping. 
Each row in this file contains: sequence_ID, dataset_ID 

- Path grouping 
Users' movements are divided in 6 prototypical paths.MovementAAL_Paths.csv provides information about data grouping based on path type. 
Each row in this file contains: sequence_ID, path_ID


The sensor reading here identifies the position of the person. Sensors were placed in three pairs of two connected rooms containing office furniture. Two sensors were placed in the corners of each of the two rooms and the subject walked one of six predefined paths through the rooms. Predictions are made at a point along each path that may or may not lead to a change of room.

If a person walks on path 2, 3, 4 or 6, he moves within the room. On the other hand,if the person walks in path 1 or path 5 then he chnages the room.

Example : ‘dataset/MovementAAL_RSS_1.csv‘, which has the output target ‘1’ (transition occurred), from group 1 (first pair of rooms) and is the path 1 (from left to right between the rooms).

#IDEA :

The idea which was tried was using LSTM. As the problem involves sequence classification task, using recurrent neural networks which supports variable length multivariate time-series data would be a better match.
