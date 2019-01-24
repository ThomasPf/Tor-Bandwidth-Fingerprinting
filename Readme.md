## How to transform a tgen log into a csv

```bash
python3 tools/main.py -f Generate/setup6/shadow.data/hosts/adversaryclient/stdout-adversaryclient.tgen.1001.log Generate/setup6/shadow.data/hosts/victimclient/stdout-victimclient.tgen.1001.log -l timestamp value -d extracted/setup6
```

## How to generate a correlation chart from the csv

```bash
python3 stats.py -p <path> -w <windowsize> -c <cherry-picked-test>
```
standard settings <br />
path:     the extracted folder <br />
          window:   200 <br />
          cherry:   none <br />

