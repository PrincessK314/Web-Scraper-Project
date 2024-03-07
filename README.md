## Overview
This program will take input from a text file whose path is taken as an argument. This input file is 5 URLs from the news website KSDK. It takes these URLs and extracts the article text from them. The program then outputs the article texts into 5 separate text files. These text files will be named “article1.txt,” “article2.txt,” etc. and place them in the processed folder within the Data directory. Within the raw folder, 5 files containing the headline, author, and publish date in addition to the article will be created with the same naming convention. This program will remove any text or content from the page that is not part of the main article including ads, other links, and headers.

## How to run
1. Download the run.py, module_1, module_2, Data, and requirements.yml files and directories
2. Either download the url.txt file or create a text file containing URLs from the KSDK website
3. Make sure you have either anaconda or miniconda downloaded and set up
4. Open the conda terminal
5. Type the command “conda create --name my_yaml_env --file requirement.yaml”
6. Type the command “conda activate my_yaml_env”
7. Navigate to the file location of the run.py file using the cd command
8. Run the file with the command “python run.py path" where path is the relative or absolute path of the text file containing the URLs. For example, if the file is named "url.txt" and in the same directory
,,,
python run.py url.txt
,,,
Or, if the file is named "input.txt" within the Documents folder where username is the username of the current user
,,,
python run.py C:\Users\username\Documents\input.txt
,,,
9. The output will be in 5 text files named “article1.txt,” “article2.txt,” etc. within the processed folder in Data
10. Additional information such as the headline, author, and date can be found in the raw folder in Data