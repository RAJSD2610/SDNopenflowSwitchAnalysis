1.cd ~/Desktop/ece671/pro
2.sudo bash 2n_topo.sh #make the topology
3.cd ~/mininet/pox
4.sudo ./pox.py ece_switch
5.iperf -c 10.0.0.2 -t 10 //host h1
6.iperf -s//host h2
7.sudo bash switch.sh #execute per sec
7.1.sudo bash sed_duration_itm_sans.sh
7.2 sudo snapshot.sh #creates total and 1sec snapshot
7.3.sudo python panda_test.py
