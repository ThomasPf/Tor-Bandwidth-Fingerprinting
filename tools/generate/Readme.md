### Prepare Alexa website data

Download the latest alexa top 1m list, csv file: rank, domain
```
wget http://s3.amazonaws.com/alexa-static/top-1m.csv.zip
unzip top-1m.csv.zip
```

Takes the first 1000 domains and looks up the IP, outputs to the csv file alexa-top-1000-ips.csv: rank, domain, ip
```
python ~/shadow-plugin-tor/tools/parsealexa.py
```


### Prepare Tor metrics data
See https://metrics.torproject.org/collector.html for more info

Download server desciptors, contains routers IP, name, port, contact, certs etc.
```
wget https://collector.torproject.org/archive/relay-descriptors/server-descriptors/server-descriptors-2018-12.tar.xz
tar xaf server-descriptors-2018-12.tar.xz
```

Download extra info descriptors, contain relay information that Tor clients do not need in order to function.
```
wget https://collector.torproject.org/archive/relay-descriptors/extra-infos/extra-infos-2018-12.tar.xz
tar xaf extra-infos-2018-12.tar.xz
```

Download consensus/network status document, published every hour by directory authorities, contains router status entries containing flags, heuristics used for relay selection, etc.
```
wget https://collector.torproject.org/archive/relay-descriptors/consensuses/consensuses-2018-12.tar.xz
tar xaf consensuses-2018-12.tar.xz
```

Download relay users by country statistics in csv file: date,country,users,lower,upper,frac
Formatting info: https://metrics.torproject.org/stats.html#userstats-relay-country
```
wget https://metrics.torproject.org/userstats-relay-country.csv
```


### Generate new Tor network

Some requirements
```
pip install numpy lxml
```

Add tools scripts to PATH
```
export PATH=${PATH}:~/shadow-plugin-tor/build/tor/src/or:~/shadow-plugin-tor/build/tor/src/tools
```

Create a directory for the new shadow topology
```
mkdir 9relays7clients
cd 9relays7clients
```

View help
```
python generate_custom.py --help
```

Example setting optional arguments
```
python generate_custom.py --nauths 1 --nrelays 9 --nclients 7 --num_web 5 --num_bulk 2 --nservers 7 --num_guards 3 --num_middles 3 --num_exits 3 ../alexa-top-1000-ips.csv ../2018-12-12-12-00-00-consensus ../server-descriptors-2018-12/ ../extra-infos-2018-12/ ../userstats-relay-country.csv > generate.log
```
This will create a shadow.config.xml base with 3 guard nodes, 3 middle nodes, 3 exit nodes, 2 clients generating bulk traffic, 5 clients generating web traffic. 

### Adjust config files to requirements
Now that we have a base topology to use we can manually tweak the configuration files for each of our different experiment scenarios.
