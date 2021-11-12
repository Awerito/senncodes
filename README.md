# SENN Code Finder and Submitter

Senn treasure hunt codes finder and auto submitter scripts on python3.

## Setup

Fill the `sample_secrets.py` by replacing the comments with the corresponding data and rename
it to `secrets.py`.

To find the `cookie` and `xrsf-token` just try to submit some data to the page while network
inspectors is open on the browser and copy the *validate-code* and *subscribe* requests data.

## Usage

To find codes by candidates of the form `HUNT[AEU][B-DF-HJ-NP-TV-Z][AEU][B-DF-HJ-NP-TV-Z][AEU]`
(regex notation) witch give us 11907 candidates to test.

To generate those codes you need to run:
> $ python3 validate.py

this will save the valid codes on `data/valid.txt`, invalid codes on `data/invalid.txt` and failed attempts on `data/errors.txt`.

To submit the valid codes automatically after finding the valid codes you need to run:
> $ python3 submit.py

## Observations

- *The valid codes are already generated so run the `validate.py` script is for testing purpose.*
- *The valid codes ended up being exactly 300 out of 11907 candidates, giving the code a 
performance of ~2.5% of likelihood to find a valid code*
- *The scripts don't search for audio codes, they do not share the same pattern*
- *The `data/extras.txt` contains codes found manually doe to not have the same patterns*
