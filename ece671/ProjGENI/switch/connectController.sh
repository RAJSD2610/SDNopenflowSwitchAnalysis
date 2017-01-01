sudo ovs-vsctl list-ports br-switch
sudo ovs-vsctl set-fail-mode br-switch secure
sudo ovs-vsctl set-controller br-switch tcp:66.104.96.107:6633

