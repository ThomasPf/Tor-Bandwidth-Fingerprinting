## Evaluating experiment
* Store experiment in experiments/{experiment_name}.
* Create all necessary config files for running an experiment with
victim named `victimclient` in `shadow.config.xml` file and adversary named `adversaryclient`. 
* Run it, so you get `shadow.data` log outputs.
* Run `python3 ../../tools/throughput_extractor/throughput_extractor.py` - this by default looks into `shadow.data/hosts/adversaryclient` and `victimclient` directories respectively for corresponding tgen log files and stores extracted throughputs into `./extracted_throughputs/setup` directory for statistical evaluation. (This is because `stats.py` currently looks for setup subdirectories). The default labels for csv files are `timestamp, value`.
* `mkdir stat_results` and `cd` into it. 
* Run `python3 ../../../tools/stats/stats.py -w {windowsize} -p ../extracted_throughputs/`.
* See the results stored in current directory.

## Directory structure
* experiments - contains individual directory for each experiment
* experiments/history - contains all experiments that were run prior to yesterday's setup8, which achieved great correlation
* tools - contains individual directory per tool written
* original_content - contains content created by previous authors - not ours

### Single Experiment Directory structure:
	classic shadow config structure with shadow.data and shadow.log for generated outputs
	+ extracted_results/setup as a target for the extracted csv files // stats.py as it is currently searches for directories named setup, so this is a quick workaround, though not optimal, we might want to change this.

