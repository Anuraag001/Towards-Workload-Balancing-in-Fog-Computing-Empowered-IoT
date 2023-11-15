# Towards-Workload-Balancing-in-Fog-Computing-Empowered-IoT

## Verify Python Installation:
```bash
python --version
```

## Verify Pip installation
```bash
pip --version
```

## setup python pip for the project:
```bash
pip install numpy
```

```bash
pip install pandas
```

```bash
pip install matplotlib
```

## Steps to run the normal code:
```bash
python main.py
```

## Features of Code:
- Variable Declarations:Various parameters and variables are declared at the beginning of the code. These include counts of Fog Nodes (FN_Count), Base Stations (BS_Count), and IoT devices (IOT_count).
Parameters such as frequencies, distances, data sizes, power levels, and thresholds are initialised with random or predefined values.

- Node and Base Station Location Initialization:Locations of Fog Nodes, Base Stations, and IoT devices are initialised randomly within specified ranges.

- The code uses matplotlib to visualise the locations of Fog Nodes, Base Stations, and IoT devices in a 2D coordinate space.

- Nearest Node Finding:Functions are defined to calculate the distance between two points and find the nearest node (Fog Node or Base Station) for each Base Station and each IoT device.

- Dataframe Printing:Pandas dataframes are created and printed to display information about Fog Nodes and IoT devices, including their locations, computing power, transmission power, quotas, and other parameters.

- Local Execution Time Calculation:Local execution time for each IoT device is calculated based on its computing demand and Arduino frequency.

- Traffic Load Model:The code models the uplink data rate, transmission time, traffic load density, and other parameters for IoT devices communicating with Base Stations.

- Computing Load Model:The computing capacity, average service time, computing load density, and other parameters for Fog Nodes are modelled.

- Latency and Time Calculation:Latency and total time for each IoT device are calculated considering communication with the nearest Base Station and Fog Node. These calculations involve transmission times, computing times, and communication latencies.

- Visualisation:The code uses matplotlib to plot graphs showing the total time for each IoT device, and it compares the time taken for computing in Fog with local execution.

- Printed Outputs:The code prints various calculated values and parameters for each IoT device and Fog Node, providing insights into the network's performance.

- Explanation Output:The code prints explanations for various calculated values, such as average traffic load, communication latency ratio, computing latency ratio, and average latency of processing data flows.

## Contact

For questions or feedback, please contact 
- [Anuraag](mailto:anuraagbv1@gmail.com)
- [Harshith Reddy](mailto:paturuharshithreddy004@gmail.com)
- [Nishchal Mayur](mailto:mayur2003rn@gmail.com)
