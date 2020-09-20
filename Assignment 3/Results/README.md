# Assignment 3

## ALS Algorithm

- Command to run the code :

```bash
bin/spark-submit  als.py <data_location>
```

- Output written to ALSoutput.txt

## FP Growth Algorithm

### First Part

- Command to run the code :

```bash
bin/spark-submit  fp1.py <data_location>
```

- Output written to fp1_out.txt

### Second Part

- Command to run the cleaning code

```bash
python fp_convert_data.py <file_name>
```

- Command to run the code :

```bash
bin/spark-submit  fp2.py <data_location>
```

- Output written to fp2_out.txt
