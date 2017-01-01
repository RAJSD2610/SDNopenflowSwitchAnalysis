sudo ovs-vsctl add-br br-switch
sudo ovs-vsctl add-port br-switch eth1
sudo ovs-vsctl add-port br-switch eth2
sudo ovs-vsctl add-port br-switch eth3
sudo ovs-vsctl list-ports br-switch
sudo ovs-vsctl set-fail-mode br-switch secure
sudo ovs-vsctl set-controller br-switch tcp:66.104.96.107:6633 #controllers public ip

