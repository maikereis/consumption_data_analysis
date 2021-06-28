# Power consumption data analysis

This repository is part of my undergraduate monograph. The objectives of the work were:
 * Data collection using IoT nodes
 * Analyze the consumption of electricity in a home and correlate them with environmental variables 

The data collection was made using IoT nodes based on ESP32 ([Node program](https://github.com/XxKavosxX/iot_node)), and a Python MQTT client ([MQTT client](https://github.com/XxKavosxX/mqtt_client)) to persist data in a AWS database.

The data collected was cleaned and analysed using python scripts and jupyter notebooks presented in this repository.

__Repository structure:__
 * **src** :where python functions to treat and analyse data
 * **database** : contains database from AWS and databases treatments steps separed by folders(raw, pre_formatted, formatted, fixed etc.).
 * **data_processing**: 
    * *EDA* : Notebooks to exploratory data analysis
    * *TREATER* : Notebooks to transform data
* **data_analysis**: data analysis like, mean, load consumption compositivion, correlations.
* **img** : contains figures, plots and graphics exported from the analysis notebooks

 
