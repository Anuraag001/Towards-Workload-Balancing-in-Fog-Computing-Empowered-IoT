# Importing required modules

import random
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Variable Declarations

FN_Count = 7
BS_Count=6
IOT_count=10
arduino_frequency= np.array([random.randrange(14000000,16000000,1) for x in range(IOT_count)]) #Mhz
FN_array=np.array([i for i in range(FN_Count)])
channel_frequency=10000000 #Mhz bandwidth
distance=2000 #km
task_input=random.randrange(300,600) *1000 #kb
task_output=random.randrange(10,20) * 1000 #kb
compu_demand=random.randrange(210,480) *1000000 # million cycles
noise_power= math.pow(10,-10) #w
IOT_TP= np.array([random.random() for x in range(IOT_count)]) #w
FN_TP=np.array([random.random()*2 for x in range(FN_Count)]) #w
FN_compu_power=np.array([random.randrange(350,550) * math.pow(10,-3) for x in range(FN_Count)])#w
task_deadline= random.randrange(30,60) #s
FN_quota=np.array([random.randrange(50,500) for x in range(FN_Count)])
avg_arrival_rate=0.5 #flows/sec
avg_traffic_size=0.005 *math.pow(10,6) #Mbits
data_compu_size=5000 #CPU cycles
BS_traffic_threshold=0.99
FN_compu_threshold=0.99
FN_compu_rate=np.array([random.randrange(6000,10000)*math.pow(10,6) for x in range(FN_Count)]) #ghz
SOL=3*10**8 #m/s

# Function to find the nearest node
def distance(A,B):
    dist=math.sqrt(math.pow((A[0]-B[0]),2)+math.pow((A[1]-B[1]),2))
    return dist
    
def nearest_find(Locations,X,Y,Count):
    dist=np.arange(Count)
    node_num=np.arange(1,Count+1)
    for i in range(Count):
        dist[i]=math.sqrt(math.pow((Locations[i][0]-X),2)+math.pow((Locations[i][1]-Y),2))
        node_num[i]=i+1
    
    node_pair=list(zip(dist,node_num))
    node_pair.sort()
    filtered=[ x[1] for x in node_pair ]
    return filtered

if __name__ == "__main__":

# Nodes and base station location initialization
    FN_Locations=np.zeros((FN_Count,2))
    BS_Locations=np.zeros((BS_Count,2))
    IOT_Locations=np.zeros((IOT_count,2))
    for i in range(FN_Count):
        FN_Locations[i][0]=random.randrange(20,1800)
        FN_Locations[i][1]=random.randrange(20,1800)

    for i in range(BS_Count):
        BS_Locations[i][0]=random.randrange(20,1800)
        BS_Locations[i][1]=random.randrange(20,1800)

    for i in range(IOT_count):
        IOT_Locations[i][0]=random.randrange(20,1800)
        IOT_Locations[i][1]=random.randrange(20,1800)

    plt.figure(figsize=(10, 10))
    plt.scatter(FN_Locations[:,0],FN_Locations[:,1],color='red',marker='o',label='Fog Node')
    plt.scatter(BS_Locations[:,0],BS_Locations[:,1],color='blue',marker='x',label='Base Station')
    plt.scatter(IOT_Locations[:,0],IOT_Locations[:,1],color='green',marker='*',label='IOT Device')
    plt.legend()
    plt.title('Fog Node and Base Station Locations')
    plt.xlabel('X-Coordinate')
    plt.ylabel('Y-Coordinate')
    plt.xlim(0, 2000)
    plt.ylim(0, 2000)
    plt.show()

#finding the nearest fog node for each base station
    print("Nearest Fog node for each Base station:",end='\n\n')
    BS_nearest_FN=np.zeros((BS_Count,FN_Count),dtype=int)
    for i in range(BS_Count):
        BS_nearest_FN[i]=nearest_find(FN_Locations,BS_Locations[i][0],BS_Locations[i][1],FN_Count)
        print(f'for Base station {i+1}:{BS_nearest_FN[i]}',end='\n')

    print('\n')

#finding the nearest base station for each iot device
    print("Nearest Base station for each Fog node:",end='\n\n')
    IOT_nearest_BS=np.zeros((IOT_count,BS_Count),dtype=int)
    for i in range(IOT_count):
        IOT_nearest_BS[i]=nearest_find(BS_Locations,IOT_Locations[i][0],IOT_Locations[i][1],BS_Count)
        print(f'for IOT device {i+1}:{IOT_nearest_BS[i]}',end='\n')

    print('\n')

#printing dataframe for fog nodes data
    data={'Fog Node':range(1,FN_Count+1),'X':FN_Locations[:,0],'Y':FN_Locations[:,1],'Computing Power':FN_compu_power,'Transmission Power':FN_TP,'Quota':FN_quota,'Threshold':FN_compu_threshold,'Computing Rate':FN_compu_rate}
    dataset=pd.DataFrame(data)
    print(dataset,end='\n')

    print('\n')

#printing dataframe for IOT device
    data={'IOT Device':range(1,IOT_count+1),'X':IOT_Locations[:,0],'Y':IOT_Locations[:,1],'Arduino Frequency':arduino_frequency,'Transmission Power':IOT_TP}
    dataset=pd.DataFrame(data)
    print(dataset,end='\n')

    print('\n')

# Local execution time 
    local_time=compu_demand/arduino_frequency
    print(f'Local Time execution time = {local_time}sec')
    plt.scatter(np.array([i for i in range(1,IOT_count+1)]),local_time,marker='*',color="red")#second graph
    plt.title("Local Execution Time")
    plt.xlabel('X-Coordinate')
    plt.ylabel('Y-Coordinate')
    plt.show()


# Traffic Load Model
    
#IOT device uplink data rate and transmission time
    SNR=IOT_TP*1/noise_power
    uplink_data_rate=channel_frequency*(np.array([math.log(1+SNR[i],2) for i in range(IOT_count)])) #math.log(1+SNR,2)
    print(f'uplink data link of each IOT towards BS j= {uplink_data_rate} Mhz',end='\n')

    uplink_transmmision_time=task_output/uplink_data_rate
    print(f'uplink transmission time for each IOT associated to BS j={uplink_transmmision_time *1000} milliseconds',end='\n') #millisecond

# average traffic load Density of IOT device
    avg_TL_Density=avg_arrival_rate*task_output*1/uplink_data_rate
    print(f'average traffic load density of each IOT at BS j= {avg_TL_Density *1000} milliseconds',end='\n') #millisecond

    avg_traffic_load=0
    for i in range(IOT_count):
        avg_traffic_load+=avg_TL_Density[i]

    avg_traffic_load=avg_traffic_load/IOT_count
    print(f'avg Traffic Load for the BS j= {avg_traffic_load *1000} milliseconds',end='\n') #millisecond

    avg_service_time=uplink_transmmision_time
    print(f'average Service Time = {avg_service_time*1000} milliseconds',end='\n')

    avg_del_time=avg_service_time/(1-avg_traffic_load)
    print(f'average delivery time = {avg_del_time*1000} milliseconds',end='\n')

    avg_waiting_time=avg_del_time*avg_traffic_load # WT=DL-ST
    print(f'average waiting time = {avg_waiting_time*1000000} microseconds',end='\n')


    communication_LR=avg_traffic_load/(1-avg_traffic_load)
    print(f'communication latency ratio of BS j = {communication_LR*1000} * 10^-3',end='\n\n\n')

# Computing load model
    FN_computing_capacity=FN_compu_rate/FN_quota
    print(f'FN computing capacity={FN_computing_capacity*1000} * 10^-3 cycles/sec',end='\n')

    FN_avg_service_time=data_compu_size/FN_computing_capacity
    print(f'average service time at FN through location x= {FN_avg_service_time*1000} milliseconds',end='\n')

    FN_avg_compu_LD=FN_avg_service_time*avg_arrival_rate*1
    print(f'average computing load density at FN  through location x= {FN_avg_compu_LD *1000} milliseconds',end='\n')

    FN_aggregate_CL=0
    for i in range(FN_Count):
        FN_aggregate_CL+=FN_avg_compu_LD[i]
    print(f'Computing load at FN j = {FN_aggregate_CL} milliseconds',end='\n')

    FN_avg_WT=FN_aggregate_CL*FN_avg_service_time/(1-FN_aggregate_CL)
    print(f'average waiting time for fog node j = {FN_avg_WT*1000000} microseconds',end='\n')

    FN_CLR=FN_aggregate_CL/(1-FN_aggregate_CL)
    print(f'Computing latency ratio of fog node j = {FN_CLR}',end='\n\n')

    avg_LR=FN_CLR+communication_LR
    print(f'average latency of processing data flows via the pair of BS j and fog node j = {avg_LR}',end='\n')


# For each IOT device
    total_time_arr=[]
    for i in range(IOT_count):
        best_BS=IOT_nearest_BS[i][0]
        best_FN=BS_nearest_FN[best_BS-1][0]
        best_BS_coor=BS_Locations[best_BS-1]
        best_FN_coor=FN_Locations[best_FN-1]
        IOT_coor=IOT_Locations[i]
        IOT_latency_time=avg_del_time[best_BS] + FN_avg_WT[best_BS]*1000
        total_time= (IOT_latency_time + FN_avg_service_time[best_BS]+distance(IOT_coor,best_BS_coor)/SOL + distance(best_BS_coor,best_FN_coor)/SOL +avg_LR)*1000
        print(f'For IOT device {i+1}: {total_time} seconds',end='\n')
        total_time_arr.append(total_time)
    total_time_arr=np.array(total_time_arr)

# Plotting graph for total time
    plt.scatter(np.array([i for i in range(IOT_count)]),total_time_arr,marker='*',color="green",label="Computing in fog")
    plt.legend()
    plt.ylim(0,2)
    plt.xlabel('IOT count ->')
    plt.ylabel('Total Time computing in fog (Seconds) ->')
    plt.yticks(np.arange(0,2.25,0.25))
    plt.title("Total Time computed in fog")
    plt.show()

#comparing time in fog and local
    plt.figure(figsize=(10, 10))
    plt.plot(np.array([i for i in range(IOT_count)]),total_time_arr,marker='*',color="green",label="Computing in Fog")
    plt.plot(np.array([i for i in range(IOT_count)]),local_time,marker='+',color="red",label="Computing Locally")
    plt.legend()
    plt.title('Comparing Time in Fog and Local')
    plt.xlabel('IOT count ->')
    plt.ylabel('Total Time (Seconds) ->')
    plt.ylim(0, 50)
    plt.show()

# Values for each IOT
    print("For each IOT device values calculated:",end='\n\n')
    for i in range(IOT_count):
        print(f"For IOT device {i+1}:")
        print(f"Local Execution Time:{uplink_data_rate[i]} seconds")
        print(f"Uplink Transmission Time:{uplink_transmmision_time[i]} milliseconds")
        print(f"average traffic load density at BS j:{avg_TL_Density[i]} milliseconds")
        print(f"average service time :{avg_service_time[i]} milliseconds")
        print(f"average delivery time:{avg_del_time[i]} milliseconds")
        print(f"average waiting time:{avg_waiting_time[i]} microseconds")
        print('\n')
    print('\n')
    print(f'avg Traffic Load for the BS j= {avg_traffic_load *1000} milliseconds',end='\n')
    print(f'communication latency ratio of BS j = {communication_LR*1000} * 10^-3',end='\n\n\n')

#values for each fog node
    print("For each Fog Node Values calculated:",end='\n\n')
    for i in range(FN_Count):
        print(f"For Fog Node {i+1}:")
        print(f"Computing capacity:{FN_computing_capacity[i]} * 10^-3 cycles/sec")
        print(f"average service time at FN through location x:{FN_avg_service_time[i]} milliseconds")
        print(f"average computing load density at FN  through location x:{FN_avg_compu_LD[i]} milliseconds")
        print(f"average waiting time for fog node j:{FN_avg_WT[i]} microseconds")
        print('\n')
    print('\n')
    print(f"Computing latency ratio of fog node j:{FN_CLR}")
    print(f'Computing load at FN j = {FN_aggregate_CL} milliseconds',end='\n')
    print(f'average latency of processing data flows via the pair of BS j and fog node j = {avg_LR}',end='\n')


