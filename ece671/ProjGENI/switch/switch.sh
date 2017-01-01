ti=`date --rfc-3339=seconds`
t=$ti
cd ~/SwitchAnalysis/FlowDump
while true
do
sudo echo `date +"%H:%M:%S"`
sudo ls |tee sw_no.txt #store file names
sudo no=`cat sw_no.txt | tr -s ' ' '\n' | grep -c 'flow'` #count flow
sudo echo $ti|tee flow.$no.csv|ovs-ofctl dump-flows br-switch |tee -a flow.$no.csv
sudo chmod 777 flow.$no.csv
#ni=`cat no.txt | tr -s ' ' '\n' | grep -c 'ftable'`
#echo $ti|tee ftable.$ni.csv|ovs-ofctl dump-tables s1|tee -a ftable.$ni.csv
#chmod 777 ftable.$ni.csv
#tee flow.${t//[[:blank:]]/}.csv
sudo bash sed_duration_itm_sans.sh
#python panda_test.py
sudo sleep 1;
done

