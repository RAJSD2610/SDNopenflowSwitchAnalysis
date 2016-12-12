#cd ~/Desktop/ece671/pro/u_ow/
cd ~/Desktop/ece671/SwitchAnalysis/ModDump
touch nfd.txt
chmod 777 nfd.txt
ls | tee nf.txt 
no=`cat nf.txt | tr -s ' ' '\n'|grep -c 'ModFl'`
echo $no
p=1
  while [  $p -lt $no ]; do
            # echo The counter is $p
	     o=`expr $p - 1`
	     echo "p:" $p "o:" $o
	     sudo diff ModFl.0.csv ModFl.$p.csv | tee ~/Desktop/ece671/SwitchAnalysis/FinDump/total.$p.csv
	     sudo chmod 777 ~/Desktop/ece671/SwitchAnalysis/FinDump/total.$p.csv
	     sudo sed -e 's/[0-9]c[0-9]//' -e 's/<//' -e 's/>//' -e 's/---//' -e '/^\s*$/d' -e 's/ //'<~/Desktop/ece671/SwitchAnalysis/FinDump/total.$p.csv> ~/Desktop/ece671/SwitchAnalysis/PlotDump/ftotal.$p.csv 
	  #   sed -i '1s/^/ 0x0,0,1,42,65535,arp,,,in_port=1,vlan_tci=0x0000,dl_rc=5e:cf:a4:58:20:1a,dl_dst=26:d4:b7:0f:b0:21,arp_spa=10.0.0.1,arp_tpa=10.0.0.2,arp_op=2 actions=output:2\n/' ~/Desktop/ece671/SwitchAnalysis/PlotDump/ftotal.$p.csv	    
             echo 0x0,0,1,42,65535,arp,,,in_port=1,vlan_tci=0x0000,dl_rc=5e:cf:a4:58:20:1a,dl_dst=26:d4:b7:0f:b0:21,arp_spa=10.0.0.1,arp_tpa=10.0.0.2,arp_op=2 actions=output:2 | tee -a ~/Desktop/ece671/SwitchAnalysis/PlotDump/ftotal.$p.csv
	     sudo chmod 777 ~/Desktop/ece671/SwitchAnalysis/PlotDump/ftotal.$p.csv   
##
	     sudo diff ModFl.$o.csv ModFl.$p.csv | tee ~/Desktop/ece671/SwitchAnalysis/FinDump/persec.$p.csv
	     sudo chmod 777 ~/Desktop/ece671/SwitchAnalysis/FinDump/persec.$p.csv
 	     sudo sed -e 's/[0-9]c[0-9]//' -e 's/<//' -e 's/>//' -e 's/---//' -e '/^\s*$/d' -e 's/ //'<~/Desktop/ece671/SwitchAnalysis/FinDump/persec.$p.csv> ~/Desktop/ece671/SwitchAnalysis/PlotDump/fpersec.$p.csv 
	     sed -i '1s/^/ 0x0,0,1,42,65535,arp,,,in_port=1,vlan_tci=0x0000,dl_rc=5e:cf:a4:58:20:1a,dl_dst=26:d4:b7:0f:b0:21,arp_spa=10.0.0.1,arp_tpa=10.0.0.2,arp_op=2 actions=output:2\n/' ~/Desktop/ece671/SwitchAnalysis/PlotDump/fpersec.$p.csv
	     echo 0x0,0,1,42,65535,arp,,,in_port=1,vlan_tci=0x0000,dl_rc=5e:cf:a4:58:20:1a,dl_dst=26:d4:b7:0f:b0:21,arp_spa=10.0.0.1,arp_tpa=10.0.0.2,arp_op=2 actions=output:2 | tee -a ~/Desktop/ece671/SwitchAnalysis/PlotDump/fpersec.$p.csv
	     sudo chmod 777 ~/Desktop/ece671/SwitchAnalysis/PlotDump/fpersec.$p.csv 
	#     sudo chmod 777 ~/Desktop/ece671/pro/u_ow/snaps/new_persec.$p.csv
	#     sudo sed -e 's/[0-9]c[0-9]//' -e 's/<//' -e 's/>//' -e 's/-//' <~/Desktop/ece671/pro/u_ow/snaps/new_persec.$p.csv>
	     let p=p+1
done
no=0
