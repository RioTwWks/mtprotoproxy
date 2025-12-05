# Async MTProto Proxy #

Fast and simple to setup MTProto proxy written in Python.

## Starting Up ##
    
1. `git clone -b stable https://github.com/alexbers/mtprotoproxy.git; cd mtprotoproxy`
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Or install as a package:
   ```bash
   pip install -e .
   ```
3. *(optional, recommended)* edit *config.py*, set **PORT**, **USERS** and **AD_TAG**
4. `docker-compose up -d` (or just `python3 mtprotoproxy.py` if you don't like Docker)
5. *(optional, get a link to share the proxy)* `docker-compose logs`

## Dependencies ##

The proxy requires the following Python packages:
- `cryptography` (recommended for better performance)
- `pyaes` (required fallback if cryptography is not available)
- `uvloop` (optional, for better performance on Linux/macOS)

All dependencies are listed in `requirements.txt` and will be installed automatically when using pip.

![Demo](https://alexbers.com/mtprotoproxy/install_demo_v2.gif)

## Channel Advertising ##

To advertise a channel get a tag from **@MTProxybot** and put it to *config.py*.

## Performance ##

The proxy performance should be enough to comfortably serve about 4 000 simultaneous users on
the VDS instance with 1 CPU core and 1024MB RAM.

## More Instructions ##

- [Running without Docker](https://github.com/alexbers/mtprotoproxy/wiki/Running-Without-Docker)
- [Optimization and fine tuning](https://github.com/alexbers/mtprotoproxy/wiki/Optimization-and-Fine-Tuning)

## Advanced Usage ##

The proxy can be launched:
- with a custom config: `python3 mtprotoproxy.py [configfile]`
- several times, clients will be automaticaly balanced between instances
- with uvloop module to get an extra speed boost
- with runtime statistics exported to [Prometheus](https://prometheus.io/)
