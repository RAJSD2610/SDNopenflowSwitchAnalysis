#cd ~/Desktop/ece671/pro/u_ow/
ls | tee nf.txt 
no=`cat nf.txt | tr -s ' ' '\n'|grep -c 'newfl'`
p=1
  while [  $p -lt $no ]; do
            # echo The counter is $p
	     o=`expr $p - 1`
	     echo "p:" $p "o:" $o
	     sudo diff newfl.0.csv newfl.$p.csv | tee ~/Desktop/ece671/pro/u_ow/snaps/total.$p.csv
             sudo diff newfl.$o.csv newfl.$p.csv | tee ~/Desktop/ece671/pro/u_ow/snaps/new_persec.$p.csv
	     let p=p+1
done
