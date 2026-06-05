Steps taken from `dki-dat-files/steps.dat`. First run with `--keynameexists=N` also generates the keys. T`.der` is binary representation of a `.pem` file. `.eds` is the endorsement broadcasted as DRIP Link.

## RAA
```
$ python3 ../csr-gen.py --keyname=raa16376 --serialnumber=x2344 --keynameexists=N
CSR Gen Version:  2024.09.17
No RAA provided.  A DET will not be generated

$ python3 ../endorse.py --serverdat=../dki-dat-files/raa16376-server-self --commandfile=../dki-dat-files/raa16376-self
CA
DET: 2001003ffe0000054fb87c2728107048
DET: 2001:003f:fe00:0005:4fb8:7c27:2810:7048
Client
DET: 2001003ffe0000054fb87c2728107048
DET: 2001:003f:fe00:0005:4fb8:7c27:2810:7048
Client HI: 3fbe40d4d5c1e58c5e80ee49f3671adde1b48512d593c9bcff6bf369ca66cc1f
Client Endorsement by CA( 136.0  bytes): 800b2b0d80d9af142001003ffe0000054fb87c27281070483fbe40d4d5c1e58c5e80ee49f3671adde1b48512d593c9bcff6bf369ca66cc1f2001003ffe0000054fb87c27281070481281eb8d57fde4780edbe79f4c5c63ab2fa67987f9db9405bf7b5983d2da9a77aaf67f1d6b58f3cb1514c27d166be3cad6ac4f9f2d9593c9c159a9a455838401
client SN: x2344

$ openssl x509 -in raa16376.pem -out raa16376.der -outform der
$ openssl x509 -in raa16376pkix.pem -out raa16376pkix.der -outform der
```

## HDA Auth

```
$ python3 ../csr-gen.py --keyname=hda16376-16376A --serialnumber=x5589 --keynameexists=N
CSR Gen Version:  2024.09.17
No RAA provided.  A DET will not be generated

$ python3 ../endorse.py --serverdat=../dki-dat-files/raa16376-server --commandfile=../dki-dat-files/hda16376-16376A
CA
DET: 2001003ffe0000054fb87c2728107048
DET: 2001:003f:fe00:0005:4fb8:7c27:2810:7048
Client
DET: 2001003ffe000005bda1f422e71a9354
DET: 2001:003f:fe00:0005:bda1:f422:e71a:9354
Client HI: 50a25ed544eb6172c8d130417be7717d8b77ea839cd42f4af827fda5be846c2a
Client Endorsement by CA( 136.0  bytes): 800b2b0d0021ec102001003ffe000005bda1f422e71a935450a25ed544eb6172c8d130417be7717d8b77ea839cd42f4af827fda5be846c2a2001003ffe0000054fb87c2728107048af6aaff8f37cb367320c5a2b76b6fe558e6f0114519bc606313e393089027d78f7d09e2ebe5b37437a9f9a44be08901db2019c4af10bb1180ce436ac9760190b
client SN: x5589

$ openssl x509 -in hda16376-16376A.pem -out hda16376-16376A.der -outform der
$ openssl x509 -in hda16376-16376Apkix.pem -out hda16376-16376Apkix.der -outform der
```

## HDA Issue

```
$ python3 ../csr-gen.py --keyname=hda16376-16376I --serialnumber=x5589 --keynameexists=N
CSR Gen Version:  2024.09.17
No RAA provided.  A DET will not be generated

$  python3 ../endorse.py --serverdat=../dki-dat-files/hda16376-16376A-server --commandfile=../dki-dat-files/hda16376-16376I
CA
DET: 2001003ffe3ff8050325d34f5a5ad186
DET: 2001:003f:fe3f:f805:0325:d34f:5a5a:d186
Client
DET: 2001003ffe3ff8050a8f96a9d7525c19
DET: 2001:003f:fe3f:f805:0a8f:96a9:d752:5c19
Client HI: a492e2039827377aa4d0a8b757048d55e456ff49f6a9b319e40bbd01656509c8
Client Endorsement by CA( 136.0  bytes): 800b2b0d0021ec102001003ffe3ff8050a8f96a9d7525c19a492e2039827377aa4d0a8b757048d55e456ff49f6a9b319e40bbd01656509c82001003ffe3ff8050325d34f5a5ad186a0de89eaf633f2d3752d9a70b8dba35ea2444aaf7cbc7e4808823c81aeeff5953bb373e01db7842460c8e9ec9142d8eb629953bed4225540364f4be6a802f903
client SN: x5589
