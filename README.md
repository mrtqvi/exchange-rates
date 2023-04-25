# exchange_rates
Obtaining the latest exchange rates along with convert, fluctuation and their rates in the past.
<br>
<h2>How to use</h2>
<br>
first clone 
<br>
<code>git clone git@github.com:mrtqvi/exchange_rates.git</code>
<br>
Then install all the requirements of the project
<br>
<code>pip install -r requirements.txt</code>
<br>
<h2>How to work</h2>
<br>
<code>
python main.py -h
</code>
<br>
<b>Or how each option works</b>
<br>
<br>
'(**)' field is required and '*' is all items

<br>
latest         | default: latest base=USD symbols=*

convert        | default: convert from_rate=USD to_rate=IRR

historical     | default: historical date=(**) base_rate=USD to_rate=IRR

fluctuation    | default: historical start_date=(**) end_date=(**) base_rate=USD to_rate=IRR

<code>python main.py -h [option]</code>

<h2>Config</h2>
<br>
<b>To determine which requests to archive</b>
<br>
first open config.py
<br>
default parameters in config dictionary
<br>
<code>
config = {
<br>
    &nbsp; &nbsp;'save_json': {
<br>
        &nbsp; &nbsp; &nbsp; &nbsp;'latest': True,<br>
        &nbsp; &nbsp; &nbsp; &nbsp;'convert': True,<br>
        &nbsp; &nbsp; &nbsp; &nbsp;'historical': False,<br>
        &nbsp; &nbsp; &nbsp; &nbsp;'fluctuation': False<br>
    &nbsp; &nbsp;},
<br>
}
</code>


