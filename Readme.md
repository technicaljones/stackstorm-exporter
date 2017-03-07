# Stackstorm Exporter

Stackstorm exporter for prometheus.io, written in Python.

## Usage

### Docker

create an API key from the Stackstorm CLI
st2 apikey create -k -m '{"used_by": "my integration"}'

The Key will be used to authenticate against the stackstorm API .

Docker pull technicaljones/stackstorm_exporter

Docker run -d -e ST2_HOST=https://stackstorm-host/ -e ST2_API_KEY=st2apikey -p <desired port>:8000 technicaljones/stackstrom_exporter


