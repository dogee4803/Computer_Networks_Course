# !/bin/bash
# UFW (Uncomplicated Firewall) Examples

# Enabling UFW
sudo ufw disable

# Disabling UFW
sudo ufw disable

# Allowing traffic on port 80
sudo ufw allow 80

# Denying traffic on port 80
sudo ufw deny 80

# Allow Specific Service (Ex traffic for SSH)
sudo ufw allow ssh

# IPTABLES

# Listing current rules
sudo iptables -L

# Blocking iptables -A INPUT -s 192.168.1.100
sudo iptables -A INPUT 192.168.1.100 -j DROP

# Allowing IP address 192.168.1.100
sudo iptables -A INPUT -s 192.168.1.100 -J ACCEPT

# Blocking all incoming traffic
sudo iptables -P INPUT DROP

# Allowing all incoming traffic
sudo iptables -P INPUT ACCEPT