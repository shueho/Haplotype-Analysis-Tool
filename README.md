# Haplotype-Analysis-Tool

***Script instructions:

1. Get_gb_by_gi.py
Crawl the corresponding genebank file by reading the GI number.

Read all text files ending in "_gi.txt" under the folder where the script is located, and each "_gi.txt" file contains the GI number that needs to be crawled.

This script is run through python3. The preparation of the crawler needs to call the "request" library, which needs to be run in advance:

>pip install request

Executing the script requires running:

>python3 ./Get_gb_by_gi. py

2. Name_gb_by_isolate.py
Read the isolate information in the GB file and name the GB file through the isolate information.It is mainly used for batch processing of a large number of GB files.

When running, you need to put this script in the directory where the GB file is located.

Executing the script requires running:

>python3 ./Name_gb_by_isolate.py
>cd ./output

3. gb_to_fasta.py
Convert the GB file into a FASTA file, and take the GB file name as the content of the modifier after ">" in the FASTA file.It is mainly used for batch processing of a large number of GB files.

When running, you need to put this script in the directory where the GB file is located.

Executing the script requires running:

>python3 ./gb_to_fasta.py
>cd ./output
