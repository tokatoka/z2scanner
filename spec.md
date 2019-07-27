# Specification for z2scanner
## 1. Basic
#### Usage: python z2scanner.py [TARGET_FILE]
TODO: if a file md5 match 26cd7ef06f358bdb5bf20f109f41aead, detect it.


#### OUTPUT format:
- Basically, output format is tsv(tab-separated value)
-- Do not insert whitespace above/bellow comma and `\t`
```
> python z2scanner.py test/samples/sample01
target_path:[TARGET_FILE_PATH]\tscanner_version:[version]\tscan_date: [YYYY-MM-DD_HH-mm-SS]\tis_malicious:[True or False]\treason_method:[Signature or Something]
```

#### Expected output:
```
> python z2scanner.py test/samples/good/good_sample_01
target_path:test/samples/good/good_sample_01\t scanner_version:0.0.1\t scan_date:[YYYY-MM-DD_HH-mm-SS]\t is_malicious:False\t reason_method:
> python z2scanner.py test/samples/bad/bad_sample_01
target_path:test/samples/bad/bad_sample_01\t scanner_version:0.0.1\t scan_date:[YYYY-MM-DD_HH-mm-SS]\t is_malicious:True\t reason_method:Embedded-Signatures
```

## 2. Directory scan mode
TODO: if a file  md5 match 26cd7ef06f358bdb5bf20f109f41aead of target directory, detect it.

### Must be support `-d` switch to scan with directory
#### Usage: python z2scanner.py -d [TARGET_DIR]

#### OUTPUT:
- Basically, output format is tsv(tab-separated value)
-- Do not insert whitespace above/bellow comma and `\t`
```
> python z2scanner.py -d test/samples
target_path:[TARGET_FILE_PATH]\tscanner_version:[version]\tscan_date: [YYYY-MM-DD_HH-mm-SS]\tis_malicious:[True or False]\treason_method:[Signature or Something]
```

#### Expected output:
```
> python z2scanner.py test/samples
target_path:test/samples/good/good_sample_01\tscanner_version:0.0.1\t scan_date:[YYYY-MM-DD_HH-mm-SS]\tis_malicious:False\t reason_method:
target_path:test/samples/bad/bad_sample_01\tscanner_version:0.0.1\t scan_date:[YYYY-MM-DD_HH-mm-SS]\tis_malicious:True\t reason_method:Embedded-Signatures
```