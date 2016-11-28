ti=`date --rfc-3339=seconds`
t=$ti
ls |tee no.txt #store file names
no=`cat no.txt | tr -s ' ' '\n' | grep -c 'flow'` #count flow
echo $ti|tee flow.$no.csv|ovs-ofctl dump-flows s1 |tee -a flow.$no.csv
chmod 777 flow.$no.csv
ni=`cat no.txt | tr -s ' ' '\n' | grep -c 'ftable'`
echo $ti|tee ftable.$ni.csv|ovs-ofctl dump-tables s1|tee -a ftable.$ni.csv
chmod 777 ftable.$ni.csv
#tee flow.${t//[[:blank:]]/}.csv
bash testsed.sh
python panda_test.py
