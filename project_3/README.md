# Linux Firewall Lab (SSH and FTP)
Harrison Coutee - COMP 324 - April 29, 2025

For this lab, I set up a firewall to block/allow SSH and FTP traffic. Since I'm on Kali, I used `iptables` to set up the firewall.

## Firewall Rules

I set up the following rules:

1. Block all SSH traffic

To block SSH traffic, I used the following command:

```bash
sudo iptables -A INPUT -p tcp --dport 22 -j DROP
```

2. Block all FTP traffic

To block FTP, I used the following command:

```bash
sudo iptables -A INPUT -p tcp --dport 21 -j DROP
```

3. Check the status of the firewall

To check the status of the firewall, I used the following command:

```bash
sudo iptables -L
```

The output from this command told me that the rules were set up correctly.

4. Allow all other traffic

To allow all other traffic, just removed the rules I had set up earlier:

```bash
sudo iptables -D INPUT -p tcp --dport 22 -j DROP
sudo iptables -D INPUT -p tcp --dport 21 -j DROP
```

Then I checked the status of the firewall again, and the rules were removed successfully.
