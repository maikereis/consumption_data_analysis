<h1 align='center'> Power consumption data analysis</h1>

![](https://img.shields.io/github/license/xxkavosxx/consumption_data_analysis)

# What this repo contains?
---

This repository is part of my **undergraduate monograph**. The work was:
 - Data collection using IoT nodes.
 - Analyze the consumption of electricity in a home and correlate them with environmental variables.

The data collection was made using IoT nodes based on ESP32 ([Node program](https://github.com/XxKavosxX/iot_node)), and a Python MQTT client ([MQTT client](https://github.com/XxKavosxX/mqtt_client)) to persist data in a AWS database.

The data collected was cleaned and analysed using python scripts and jupyter notebooks presented in this repository.

<br>

# Achievements
----

### The daily average Power demand

<div style="background-color:white;"><img src=img/results/lines.png></div>

### The correlation between Power demand and the TDI (Thermal Discomfort Index)

<div style="background-color:white;"><img src=img/results/heatmap.png></div>

### The consumption by device

<div style="background-color:white;"><img src=img/results/donut.png></div>


<br>

# Nodes
----
The data collection was made using IoT nodes based on ESP32 as a microcontroler.


<img width=200px src=img/nodes/esp32.jpg>

The nodes were equiped with; a **temperature and humidity** sensor, a **electrical current** sensor, **voltage sensor** and a **battery**.



<div class="row">
  <div class="column">
    <img width=200px src=img/nodes/shtc3.jpg>
    <img width=200px src=img/nodes/sct013.jpg>
    <img width=200px src=img/nodes/zmpt101b.jpg>
    <img widht=200px height= 267px src=img/nodes/battery.jpg>
  </div>  
</div>

Following the scheme 

<img src=img/results/diagram.png>

Below you can see the nodes assembled

<div class="row">
  <div class="column">
    <img height=200px src=img/nodes/node.jpg>
    <img height=200px src=img/nodes/node1.jpg>
    <img height=200px src=img/nodes/node2.jpg>

  </div>  
</div>

<br>

# How to use?

1. Clone this repo

    ```
    git clone link
    ```

2. Open a terminal inside the cloned folder and type:

    ```sh
    make create_enviroment
    workon iot
    make requirements
    make get_data
    ```

3. Run the notebooks 

    The you should run all the notebooks inside [data_processing/TREATER](data_processing/TREATER/) in the numeric order.

    Each notebook will apply a transformation in the data and save the result in the corresponding [database folder](database/).

    If you're insterested, you can see the [EDA](data_processing/EDA/).

4. See the analysis

    Go to data_analysis and see the [Descritive Data Analysis](data_analysis/DDA) notebooks.

5. See the article and full work here

    - [Article](paperwork/iot_ctda.pdf)


    





# Project Structure
----

    ├──src                                        <- Python functions to treat and analyse data.
    |
    ├──database                                   <- Datasets separed by folders(raw, pre_formatted, formatted, fixed etc.)
    |   ├──raw
    |   |
    |   └──...
    |
    ├──data_processing: 
    |   ├──EDA                                    <- Notebooks to exploratory data analysis
    |   |
    |   └──TREATER                                <- Notebooks to transform data
    |
    ├──data_analysis                              <- Data analysis like, mean, load consumption compositivion, correlations.
    |    └──DDA                                    <- Descritive data analysis
    |
    └──img                                        <- Figures genetared in analysis notebooks

 
