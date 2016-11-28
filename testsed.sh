#sed s/NXST_FLOW reply (xid=0x4):/cookie, duration, table, n_packets, n_bytes, idle_age, priority, arp, in_port, vlan_tci, dl_src, dl_dst, arp_spa,arp_tpa,arp_op,actions' 
ls |tee no1.txt
no=`cat no1.txt | tr -s ' ' '\n' | grep -c 'newfl'`
sed -e 's/NXST_FLOW reply (xid=0x4):/cookie,duration,table,n_packets,n_bytes,idle_age,priority,,,,,,,,,,,,/' -e 's/arp/arp,,/' -e 's/ cookie=//' -e 's/ duration=//' -e 's/ table=//' -e 's/ n_packets=//' -e 's/ n_bytes=//' -e 's/ idle_age=//' -e 's/ priority=//' -e 's/s//' <flow.$no.csv >newfl.$no.csv
sudo chmod 777 newfl.$no.csv
