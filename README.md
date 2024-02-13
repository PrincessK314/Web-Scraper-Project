## Overview
This program will take input from a text file called “url.txt.” This input is 5 URLs from the news website KSDK. It takes these URLs and extracts the article text from them. The program then outputs the article texts into 5 separate text files. These text files will be named “article1.txt,” “article2.txt,” etc. This program will remove any text or content from the page that is not part of the main article including ads, other links, and headers.

## How to run
1. Download the webscraper.py, url.txt, and requirements.yml files
2. Make sure you have either anaconda or miniconda downloaded and set up
3. Open the conda terminal
4. Type the command “conda create --name my_yaml_env --file requirement.yaml”
5. Type the command “conda activate my_yaml_env”
6. Navigate to the file location of the webscraper.py file using the cd command
7. Run the file with the command “python webscraper.py”
8. The output will be in 5 text files named “article1.txt,” “article2.txt,” etc.