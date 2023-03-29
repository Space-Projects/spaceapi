# spaceapi
Open sourced API and scripts to download and plot space data.


## Install pyglow

### Step - 1
```shell
cd pyglow
```
```shell
make -C src/pyglow/models source
```
```shell
python3 setup.py install --user
```

## Get your own API KEY from nasa.gov

### Step - 1
visit https://api.nasa.gov/ and fill out the form. You should immediately receive an `API key` in your email.
### Step - 2
Copy the `API key` and save it in a text file named `nasa.key`.