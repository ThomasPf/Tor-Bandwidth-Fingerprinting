## Dependencies
* shadow installed with tor-plugin
* shadow tor-plugins code changed so the manual selection of tor circuits is possible

### Python Dependencies
Python          3.7.2

with the following packages installed:
* cycler	        0.10.0	0.10.0
* kiwisolver	    1.0.1	1.0.1
* matplotlib	    3.0.2	3.0.2
* numpy	        1.16.0	1.16.0
* pandas	        0.23.4	0.23.4
* pip	            10.0.1	19.0.1
* pyparsing	    2.3.1	2.3.1
* python-dateutil	2.7.5	2.7.5
* pytz	        2018.9	2018.9
* scipy	        1.2.0	1.2.0
* setuptools	    39.1.0	40.6.3
* six	            1.12.0	1.12.0

## Evaluating experiment
Here, by experiment we mean self-stand network scenario with complete shadow configuration structure (shadow.config.xml and corresponding /conf directory)
* Store experiment in experiments/{experiment_name}.
* Make sure that the desired victim is named `victimclient` in `shadow.config.xml` file and adversary is named `adversaryclient`. 
* Run it, so you get `shadow.data` log outputs.
* Run `python3 ../../tools/throughput_extractor/throughput_extractor.py` - this by default looks into `shadow.data/hosts/adversaryclient` and `victimclient` directories respectively for corresponding tgen log files and stores extracted throughputs into `./extracted_throughputs/setup` directory for statistical evaluation. (This is because `stats.py` looks for setup subdirectories). The default labels for csv files are `timestamp, value`.
* `mkdir stat_results`. 
* Run `python3 ../../../tools/stats/stats.py -w {windowsize}.`
* Run `python3 ../../../tools/stats/stats.py -h` for help
* See the results stored in current directory.

## Directory structure
* experiments - contains individual directory for each experiment
* experiments/history - contains all experiments that were run prior to setup8
* tools - contains individual directory per tool written
* original_content - contains content created by previous authors - not ours

### Single Experiment Directory structure:
	classic shadow config structure with shadow.data and shadow.log for generated outputs
	+ extracted_results/setup as a target for the extracted csv files
