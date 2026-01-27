## Write your algorithm(s)

1. Replace the placeholder code in `run_model.py` script with your own algorithm(s). Create additional functions and scripts for modularity and organization as needed.
2. Manage the dependencies:
   * **Python:** Update `requirements.txt` with any required Python libraries.
3. (optional) Locally run `run_model.py` to verify it can run successfully.

The scripts have been designed to accept input and output directories as command-line arguments, allowing you to test with various data locations.

* By default, the scripts look for input in the `/input` directory and write output to the `/output` directory, as expected by the Synapse submission system.
* To use custom directories, specify them as arguments. For example:

**Python**
```bash
python python/run_model.py --input-dir input/ --output-dir output/
```

where:
* `input/` is used as the input directory
* `output/` is used as the output directory


**Input files** 
When running your Docker container, input files will be mounted into a directory called **/input** that expects images

**Output files**
When running your Docker container, an output directory will be mounted as a directory called /output

Predictions file (.csv file):

**Task 1**:  ```id,mes_score_0_3```

**Task 2**:  ```id,uceis_score```

**Task 3**:  ```id,caption```


**Update the Dockerfile**
Ensure all dependencies are listed in `requirements.txt` so that they are installed during this build process, as network access is disabled when your submission is run.
