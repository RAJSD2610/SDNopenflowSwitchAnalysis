ti=`date --rfc-3339=seconds`
t=$ti
ls |tee no.txt #store file names
no=`cat no.txt | tr -s ' ' '\n' | grep -c 'flow'` #count flow
ovs-ofctl dump-flows s1|$ti |tee flow.$no.csv
chmod 777 flow.$no.csv
ni=`cat no.txt | tr -s ' ' '\n' | grep -c 'table'`
ovs-ofctl dump-tables s1|$ti|tee table_flow.$ni.csv
chmod 777 table_flow.$ni.csv
#tee flow.${t//[[:blank:]]/}.csv
bash testsed.sh
python panda_test.py
