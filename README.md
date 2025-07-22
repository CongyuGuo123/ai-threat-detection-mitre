# ai-threat-detection-mitre
AI-Driven Threat Detection with MITRE ATT&amp;CK Mapping

## Setup Instructions

Please run the following steps to regenerate the tokensim data:

### Clone the artifact and run the code.
  - **Fetch the code:** 
    ```bash
    $ git clone https://github.com/CongyuGuo123/ai-threat-detection-mitre.git
    $ cd ai-threat-detection-mitre
    $ cd project
    $ cd scripts
  - **Create the virtual environment in IDE:**
    ```bash
    $ python3 m-venv project
  - **Compile the virtual environment:**
    ```bash
    $ source project/bin/activate
  - **install required python libary:**
    ```bash
    $ pip3 install pandas
    $ pip3 install seaborn
    $ pip3 install scikit-learn
  - **run <dataprocess.py> file to get consolidated datasets for model training and testing:**
    ```bash
    $ python3 dataproess.py
   - **run <trainModel.py> file to get trained model:**
    ```bash
    $ python3 trainModel.py
   - **run <evaluateModel.py> file to get model performance evaluation:**
    ```bash
    $ python3 evaluateModel.py
   - **run <getDocumentation.py> file to browse website to get mitre_attack_documentation.csv file:**
    ```bash
    $ python3 getDocumentation.py
   - **run <attack_frequency.py> file to map relationship between testing dataset through trained model with mitre_attack_documentation.csv file downloaded from the Internet:**
    ```bash
    $ python3 attack_frequency.py
   - **run <graph.py> file to get visualized report:**
    ```bash
    $ python3 graph.py
   - **run <plot_confusion_matrix.py> file to get visualized report:**
    ```bash
    $ python3 plot_confusion_matrix.py
