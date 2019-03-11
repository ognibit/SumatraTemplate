# SumatraTemplate
A very simple Python structure to setup a Sumatra environment for data experimenting.

For Italian users, see [OgniBit](https://www.ognibit.it/2019/03/11/sumatra/)

# Init and run
```
pip install gitpython sumatra	
git clone https://github.com/ognibit/SumatraTemplate.git
cd SumatraTemplate
smt init SumatraTemplate
mkdir archive
smt configure \
    --executable=/home/omar/.virtualenvs/cv/bin/python \
    --main=main.py \
    --archive ./archive
smt run -o ./Data/run.log conf/default.yaml
smt list -l
```
