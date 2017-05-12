# JEAP - Jodah Encryption Algorithm in Python

A python implementation of a code my friends and I developed back in high school. Shhh, it's top secret!

There are 4 intended releases:
- [x] Basic implementation
- [x] Add custom callback function
- [ ] Add wrapping on self
- [ ] Add support for using binary files instead of text strings

## Basic Usage
* Make sure you have Python3
* `git clone https://github.com/Rudedog9d/JEAP.git`
  * Or download the zip file
* Run it! (via CLI):
```
$ ./JEAP.py -e "Jodah Encryption Algorithm in Python"
 
J6owddaFh9-bE+nKc]r_y.pkt}i~oanc-KA@lpgTo6rNigtZh-m5-?i#nK-AP-y$t.hao}n!
 
$ ./JEAP.py -d 'J6owddaFh9-bE+nKc]r_y.pkt}i~oanc-KA@lpgTo6rNigtZh-m5-?i#nK-AP-y$t.hao}n!'
 
Jodah-Encryption-Algorithm-in-Python
```

You can see all the available options by running `JEAP.py --help`:
```
usage: JEAP.py [-h] [-k KEY] [-s START] [-E END] [-F FILE] [-v] [-e] [-d]
               text [text ...]

Encrypt and Decrypt Strings using the JODAH Encryption Algorithm

positional arguments:
  text                  text to encrypt/decrypt

optional arguments:
  -h, --help            show this help message and exit
  -k KEY, --key KEY     encryption/decryption key
  -s START, --start START
                        padding at start of encrypted text
  -E END, --end END     padding at end of encrypted text
  -F FILE, --file FILE  file to read/write data to
  -v, --verbose         Verbose output
  -e, --encrypt         Encrypt the text
  -d, --decrypt         Decrypt the text
```

Specify a different key using `-k`/`--key`:
```
$ ./JEAP.py -k 3 -e Jodah Encryption Algorithm in Python
 
J&}wo,F#dI_Va6<2h4}(-v0+EiC#n41Bc=HwrW;%y,_#p+oztfwGihqXo0N3n)Ay-u1DAxAVl3b6gBWwo?yWr3x7ikKftm}Jh-$Fm.4o-:V$iDiSn@)5-^&vPe49yT_>tC7Ph(_CoG(YnAW1
 
./JEAP.py -k 3 --decrypt 'J&}wo,F#dI_Va6<2h4}(-v0+EiC#n41Bc=HwrW;%y,_#p+oztfwGihqXo0N3n)Ay-u1DAxAVl3b6gBWwo?yWr3x7ikKftm}Jh-$Fm.4o-:V$iDiSn@)5-^&vPe49yT_>tC7Ph(_CoG(YnAW1'
 
Jodah-Encryption-Algorithm-in-Python
```
