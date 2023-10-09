## About

This repository contains a set of scripts to process, save, and convert stream data for visualization.


## Installation guide

- Make sure you have Node.js installed for running the TypeScript script.
- Make sure you have Python installed for running the Python script.
- Make sure you have npm installed

1. Run installation

    ``` bash
    npm i
    ```

2. Install npx

    ``` bash
    npm i -g npx
    ```

3. Start subscriber

    ``` bash
    npm run start
    ```

## Usage

### Data Collection

The `main.ts` file contains the TypeScript code to connect to a data stream, process the data, and save specific fields (id, ambientTemp, latitude, longitude, and time) to a file named `output.txt`.

Run the TypeScript script using the following command:

``` bash
tsc main.ts && node main.js
```

### Data Conversion

The `convert_to_csv.py` file contains the Python script to convert the data saved in `output.txt` to a CSV file named `output.csv`.

Run the Python script using the following command:

``` bash
python convert_to_csv.py
```

### Data Visualization

Upload the file output.csv on https://kepler.gl/demo to see all the data points 