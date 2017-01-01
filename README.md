# SDNopenflowSwitchAnalysis
install mininet library in your linux system

1.Download ece671

2.paste proj_controller_ece671_switch.py in pox 

3.use command ./pox.py proj_controller_ece671_switch

4.cd ece671/SwitchAnalysis

5.bash 2n_topo.sh #runs topology

6.xtrem h1 h2 s1

7.in h1 run iperf -c h2

8.in h2 run iperf -s -l

9.in s1 run sudo bash switch.sh

10.bash snaptry.sh

11(a).python Instantplot.py #plot current data

12(a).create a directory and transfer files from directory PlotDump to it

13(a).Inculde the path to all your data directories in  FinalPlot.py

11(b).python FinalPlot.py #plots the statistics for all your full runs

13.bash ClearDump.sh #clears dir for next set of full run
14.bash ClearPlot.sh #clears dir for next set of full run

