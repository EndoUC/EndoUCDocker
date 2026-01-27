# EndoUCDocker

Participants are required to submit their trained model as a **Docker container** so it can be evaluated on unseen data during the final phase.

### 1. Implement your algorithm

- Replace the placeholder code in `python/run_model.py` with your own algorithm.
- You may create additional Python files or folders for better modularity and organization.
- The main entry point **must remain** `run_model.py`.

### 2. Input specification

- **Input directory:** `/input`
- The input directory will contain the test images provided by the challenge organizers.
- Participants should assume that all images are located directly inside the `/input` directory (no nested folders).

Your algorithm must load and process **all images** found in `/input`.

### 3. Output specification

- **Output directory:** `/output`
- Your algorithm must generate **CSV files**, according to submission task .

