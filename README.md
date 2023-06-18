# SPFscript

Automation for checking spf records in mxtoolbox.com 
Checks given domain name in mxtoolbox.com/supertool.aspx

1. Create "list.txt" file and write all domain addresses line by line manually.
2. Create "spfrecords" folder to hold spf reports in .txt file for each domain address
3. Create 3 txt files named as "NoSPF.txt", "MultipleSPF.txt", "SPFfound.txt" to collect SPF records 
   If mxtoolbox finds valid spf record domain name will be saved in "SPFfound.txt"
   If mxtoolbox finds more than one spf record domain name will be saved in "MultipleSPF.txt"
   If mxtoolbox finds no spf record domain name will be saved in "NoSPF.txt"

In the end, all records will be categorized and saved in those .txt files.
You should change value for each file path variable proper to your file locations.
If program fails, try to increase time delays between keystrokes.

   
