import random
import time
import numpy as np
from matplotlib import pyplot as plt



MAX_GREEN_TIME = 10
density = []                 #this is defined as number of cars being added to queue per second
for i in range(4):
    density.append(random.random()*0.75)
    i=i+1
print("Traffic Density of each lane = ", density)

tvehi=np.zeros(4, dtype=float)
lane_queue = []
for i in range(4):
    lane_queue.append(random.randint(1,10))
    tvehi[i]=lane_queue[i]

alpha = 0.5     #queue-time constant
#green_time = alpha * lane_queue[0]

print("Updated Lane Queues: ", lane_queue)
print("one iteration is over now we again look at the traffic scenario and decide which lane to pick")
time.sleep(3)
wt = []
wait_time=np.zeros(4, dtype=float)
static_wt = np.zeros(4, dtype=float)
cnt=100
size=cnt
while(cnt):
    cnt=cnt-1
    next_queue = lane_queue.index(max(lane_queue))
    print("Lane number {} is picked next".format(next_queue+1))
    green_time = alpha * lane_queue[next_queue]

    if green_time>MAX_GREEN_TIME:
        green_time=MAX_GREEN_TIME
    
    for i in range(4):
        if i!= next_queue:
            wait_time[i] += (green_time * lane_queue[i])
            static_wt[i] += (MAX_GREEN_TIME * lane_queue[i])
    
    print("Lane {} is GREEN! for {} seconds".format(next_queue+1, green_time))
    #time.sleep(green_time)
    beta = 1.25      #number of vehicles that move per unit of time #######outflow
    vehicles_moved = beta * green_time

    for i in range(4):
        if i != next_queue:
            lane_queue[i] += int(density[i]*green_time)
        else:
            lane_queue[i] += int(density[i]*green_time)
            lane_queue[i] = max(int(lane_queue[i]-vehicles_moved),0)
        
    for i in range(4):
        tvehi[i] += lane_queue[i]
    
    print("Updated Lane Queues: ", lane_queue)

    density.clear()
    for i in range(4):
        density.append(random.random() * 0.75)
    print("Density = ", density)
    
avg_wt = np.zeros(4)
savg_wt = np.zeros(4)
for i in range(4):
    avg_wt[i] = wait_time[i] / tvehi[i]
    savg_wt[i] = static_wt[i] / tvehi[i]


labels = ['lane 1', 'lane 2', 'lane 3', 'lane 4']
values1 = avg_wt.tolist()
values2 = savg_wt.tolist()
for i in range(4):
    print(avg_wt[i] / savg_wt[i])
x = np.arange(len(labels))  # the label locations

# Width of the bars
width = 0.35

fig, ax = plt.subplots()

# Plot bars for the first array
rects1 = ax.bar(x - width/2, values1, width, label='Adaptive WT')

# Plot bars for the second array
rects2 = ax.bar(x + width/2, values2, width, label='Static WT')

# Add labels, title, and legend
ax.set_xlabel('Categories')
ax.set_ylabel('Values')
ax.set_title('Comparison')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# Show plot
plt.show()