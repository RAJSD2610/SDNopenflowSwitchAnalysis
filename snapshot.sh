#cd ~/Desktop/ece671/pro/u_ow/
touch nf.txt
chmod 777 nf.txt
ls | tee nf.txt 
no=`cat nf.txt | tr -s ' ' '\n'|grep -c 'ModFl'`
echo $no
p=1
  while [  $p -lt $no ]; do
            # echo The counter is $p
             o=`expr $p - 1`
             echo "p:" $p "o:" $o
             sudo diff ModFl.0.csv ModFl.$p.csv | tee ~/Desktop/ece671/pro/u_ow/snaps/total.$p.csv
             sudo chmod 777 ~/Desktop/ece671/pro/u_ow/snaps/total.$p.csv
             sudo sed -e 's/[0-9]c[0-9]//' -e 's/<//' -e 's/>//' -e 's/---//' -e '/^\s*$/d' -e 's/ //'<~/Desktop/ece671/pro/u_ow/snaps/total.$p.csv>~/Desktop/ece671/pr$
             sudo diff ModFl.$o.csv ModFl.$p.csv | tee ~/Desktop/ece671/pro/u_ow/snaps/new_persec.$p.csv
             sudo chmod 777 ~/Desktop/ece671/pro/u_ow/snaps/new_persec.$p.csv
        #     sudo sed -e 's/[0-9]c[0-9]//' -e 's/<//' -e 's/>//' -e 's/-//' <~/Desktop/ece671/pro/u_ow/snaps/new_persec.$p.csv>
             let p=p+1
done
no=0
