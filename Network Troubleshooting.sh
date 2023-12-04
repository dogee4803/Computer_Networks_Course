!/bin/bash

# PART 1: PING
# Basic ping
echo "Basic ping: "
ping -c 4 google.com
echo ""

# Ping with Custom Timeout of 2 seconds
echo "Ping with Custom Timeout of 2 seconds: "
ping -c 4 -W 2 google.com
echo ""

# Ping with a Packet Size of 100 bytes
echo "Ping with a Packet Size of 100 bytes:"
ping -c 4 -s 100 google.com
echo ""

# Ping to a specific Interface
ping "Ping through the eth0 Interface: "
ping -c 4 -I eth0 google.com
echo ""

# Ping with a Continous Output
echo "Performing a continous ping"
ping google.com
echo ""

# PART 2: TRACEROUTE
# Basic Traceroute
ping "Basic Traceroute: "
traceroute google.com
echo ""

# Traceroute with a maximum of 5 hops
echo "Traceroute with a maximum of 5 hops: "
traceroute -m 5 google.com
echo ""

# Traceroute using ICMP
echo "Traceroute using ICMP: "
traceroute -I google.com
echo ""

# Traceroute with a timeout of 2 seconds
echo "Traceroute with a timeout of 2 seconds: "
traceroute —wait=2 google.com
echo ""

# Tracerout to port 80
echo "Tracerout to port 80: "
traceroute -p 80 google.com
echo ""

# PART 3: NETSTAT
# Display all listenning ports
echo "isplay all listenning ports: "
netstat -1
echo ""

# Displaying all tcp ports
echo "Displaying all tcp ports: "
netstat -lt
echo ""

# Displaying numeric adresses
echo "Displaying numeric adresses: "
netstat -n
echo ""

# Displaying Program Name
echo "Displaying Program Name: "
netstat -p
echo ""

# Displaying Statistic by Protocol
echo "Displaying Statistic by Protocol: "
netstat -s
echo ""

# PART 4: SS
# Displaying Socket Summary
echo "Displaying Socket Summarys: "
ss -s
echo ""

# Displaying Listening Sockets
echo "Displaying Listening Sockets"
ss -l

# Displaying All UDP Sockets
echo "Displaying All UDP Sockets"
ss -u -a

# Displaying Summary Statistics
echo "Displaying summary statistics"
ss -s

# Displaying Sockets in Listening State
echo "Displaying Sockets in Listening State"
ss -l