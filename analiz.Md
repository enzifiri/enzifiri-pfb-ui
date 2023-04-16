<div align=center>
<h1>Perform analysis of my Celestia node</h1>

Hello friends. I'm Halil TEKATLI from Turkey. This blog will be about celestia. I am one of the lucky users selected for celestia's incentivized testnet.
 I've been running my Celestia Light node since 29.03.2023 20:31:42. You can use the link below to see my node details.
 https://tiascan.com/light-node/12D3KooWN5KW2qdVbioDZ9jC2cYW2YW29sMLWx7LxoZUCq7BhcgN 

  
First, let's take a look at what your own node and minimum system requirements are.

### Hardware Requirements (minimum) <br>
Memory: 2 GB RAM <br>
CPU: Single Core <br>
Disk: 5 GB SSD Storage <br>
Bandwidth: 56 Kbps for Download/56 Kbps for Upload <br>
### I own node <br>
Memory: 4 GB RAM <br>
CPU: 2 vCPU <br>
Disk: 40 GB SSD Storage <br>
</div>

# How do I perform my node analyses?

  Node analysis is the examination of the nodes and connections in a network. Node analysis is often used to understand the structural properties of a network, identify important nodes, and understand their impact on the network. I use several methods to perform node analysis.

First, I analyze the topology of the network. This helps me understand how nodes are connected and the structure of the network. During this analysis, I evaluate the number of nodes, connection density, and centrality.

Next, I examine the properties and behaviors of the nodes in the network. This analysis helps me understand the influence of each node and its role in the network. In this process, I evaluate the degree, centrality, and importance of each node.

Finally, I examine the relationships between nodes in the network. This analysis helps me understand the collaborative and competitive relationships in the network. In this process, I evaluate the connectivity, density, and interaction of each node with other nodes.

Each of these methods plays an important role in analyzing the nodes and connections in the network. These analyses help me identify issues or opportunities in the network and improve its performance, efficiency, and security.

  Another method I use for system analysis is to use the tools available in the Linux operating system. These tools are very useful for detecting performance issues and other errors in the system.

Firstly, I can use the ```top``` and ```htop``` tools available in the Linux operating system to monitor CPU usage and which applications are consuming more resources. These tools allow me to quickly detect overload situations and provide me with the necessary information to intervene.

In addition, I can track RAM usage in the system using the ```free``` command. This shows how much of the RAM is being used, how much is free, and how much is being cached.

To monitor disk usage, I use the ```df``` and ```du``` commands. The ```df``` command shows how much of the disk partitions are being used and how much is free. The ```du``` command shows the size of a specific directory or specific files.

Moreover, I can monitor network traffic with the ```netstat``` and ```iftop``` commands. These commands show the network connections and which applications are consuming how much network traffic.

In conclusion, the tools available in the Linux operating system are very useful for system analysis. These tools allow me to obtain the necessary information to detect performance issues and errors in the system. This is important to provide better service to my customers and ensure that systems run in a more secure, efficient, and performant manner.

## CPU 
In general, I aim to utilize at least 5% and up to 25% of the CPU. On average, the usage fluctuates around 8%. However, if the CPU usage exceeds these expected values, I promptly intervene to identify and resolve any potential issues. This proactive approach helps ensure that the system operates optimally and minimizes the risk of any negative impacts on system performance or stability.
![image](https://user-images.githubusercontent.com/76253089/232323301-c1f6107a-0c5d-45a3-8c68-bcf61e0b7f6d.png)

## RAM
Similarly, I also monitor RAM usage in a similar manner. Currently, out of the total 4GB RAM, approximately 1.5GB is being utilized, with around 0.89GB free and 1.36GB being used for caching. By consistently monitoring the RAM usage, I can quickly identify any potential issues and take the necessary steps to optimize system performance and stability. This ensures that the system operates efficiently and minimizes the risk of any negative impact on performance or stability.
![image](https://user-images.githubusercontent.com/76253089/232323428-547f2efa-92cd-454c-8ad1-a924ec0ed049.png)

## Bandwith
Commands ```sudo apt install speedtest-cli``` ```speedtest-cli``` <br>
Testing download speed...Download: 1923.50 Mbit/s <br>
Testing upload speed...Upload: 453.12 Mbit/s <br>

## SETUP
If you wish, you can also monitor your nodes using the commands available in Linux, or alternatively, you can use other programs to achieve this. Personally, I tend to monitor my nodes using the 'netstat' program. If you are interested in using this method to monitor your nodes, I have prepared a brief guide that you can find below. By consistently monitoring your nodes, you can quickly identify any potential issues and take the necessary steps to optimize their performance and stability.
To utilize these codes, run them within your node directory.

1- Install Netdata: (UBUNTU 20.04 LTS)
```
wget -O /tmp/netdata-kickstart.sh https://my-netdata.io/kickstart.sh
sh /tmp/netdata-kickstart.sh --nightly-channel
```
2- Create a membership using NetData and paste your private code into the console.
```
wget -O /tmp/netdata-kickstart.sh https://my-netdata.io/kickstart.sh && sh /tmp/netdata-kickstart.sh --nightly-channel --claim-token YOURTOKEN --claim-url https://app.netdata.cloud
```
3- Connect Your Node
Edit the following command and connect to your server from anywhere you want.
``` http://SERVERIP:19999/```

