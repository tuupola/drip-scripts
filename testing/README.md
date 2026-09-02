Steps taken from `dki-dat-files/steps.dat`. First run with `--keynameexists=N` also generates the keys. T`.der` is binary representation of a `.pem` file. `.eds` is the endorsement broadcasted as DRIP Link.

## RAA

```
$ python3 ../csr-gen.py --keyname=raa16376 --serialnumber=x2344 --keynameexists=N
CSR Gen Version:  2024.09.17
No RAA provided.  A DET will not be generated

$ python3 ../endorse.py --serverdat=../dki-dat-files/raa16376-server-self --commandfile=../dki-dat-files/raa16376-self
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
DET: 2001003ffe3ff8050325d34f5a5ad186
DET: 2001:003f:fe3f:f805:0325:d34f:5a5a:d186
Client HI: 50a25ed544eb6172c8d130417be7717d8b77ea839cd42f4af827fda5be846c2a
Client Endorsement by CA( 136.0  bytes): 800b2b0d0021ec102001003ffe3ff8050325d34f5a5ad18650a25ed544eb6172c8d130417be7717d8b77ea839cd42f4af827fda5be846c2a2001003ffe0000054fb87c272810704864d2bef54919c668c8ba9579327152c7b7947b21eea49670de5d1a8fb1070001189c660176d11334c0ce15af6b5f6219d962adea380cf5e25f263575d0f65e0e
client SN: x5589

$ openssl x509 -in hda16376-16376A.pem -out hda16376-16376A.der -outform der
$ openssl x509 -in hda16376-16376Apkix.pem -out hda16376-16376Apkix.der -outform der
```

## HDA Issue

```
$ python3 ../csr-gen.py --keyname=hda16376-16376I --serialnumber=x5589 --keynameexists=N
CSR Gen Version:  2024.09.17
No RAA provided.  A DET will not be generated

$ python3 ../endorse.py --serverdat=../dki-dat-files/hda16376-16376A-server --commandfile=../dki-dat-files/hda16376-16376I
CA
DET: 2001003ffe3ff8050325d34f5a5ad186
DET: 2001:003f:fe3f:f805:0325:d34f:5a5a:d186
Client
DET: 2001003ffe3ff8050a8f96a9d7525c19
DET: 2001:003f:fe3f:f805:0a8f:96a9:d752:5c19
Client HI: a492e2039827377aa4d0a8b757048d55e456ff49f6a9b319e40bbd01656509c8
Client Endorsement by CA( 136.0  bytes): 800b2b0d0021ec102001003ffe3ff8050a8f96a9d7525c19a492e2039827377aa4d0a8b757048d55e456ff49f6a9b319e40bbd01656509c82001003ffe3ff8050325d34f5a5ad186a0de89eaf633f2d3752d9a70b8dba35ea2444aaf7cbc7e4808823c81aeeff5953bb373e01db7842460c8e9ec9142d8eb629953bed4225540364f4be6a802f903
client SN: x5589

$ openssl x509 -in hda16376-16376I.pem -out hda16376-16376I.der -outform der
$ openssl x509 -in hda16376-16376Ipkix.pem -out hda16376-16376Ipkix.der -outform der
```

## UA1

```
$ python3 ../csr-gen.py --keyname=ua1-16376-16376 --serialnumber=x1224AABBCCDDEE56789
CSR Gen Version:  2024.09.17
No RAA provided.  A DET will not be generated

$ python3 ../endorse.py --serverdat=../dki-dat-files/hda16376-16376I-server --commandfile=../dki-dat-files/ua1-16376-16376
CA
DET: 2001003ffe3ff8050a8f96a9d7525c19
DET: 2001:003f:fe3f:f805:0a8f:96a9:d752:5c19
Client
DET: 2001003ffe3ff80522879e7592f2d155
DET: 2001:003f:fe3f:f805:2287:9e75:92f2:d155
Client HI: b41176c5b305e1823a47715c398f575dcc2a4f16bbdeebdc42d6518907f23b72
Client Endorsement by CA( 136.0  bytes): 800b2b0d80ed0a0f2001003ffe3ff80522879e7592f2d155b41176c5b305e1823a47715c398f575dcc2a4f16bbdeebdc42d6518907f23b722001003ffe3ff8050a8f96a9d7525c192421d625aca0c454f23747b01dca51c194883444f59d90cdaa7d07022efd76c9bd7449b38b87595619861dde4a86910e3befcd96948a1c4042b6338ed721ea09
client SN: x1224AABBCCDDEE56789

$ openssl x509 -in ua1-16376-16376.pem -out ua1-16376-16376.der -outform der
$ openssl x509 -in ua1-16376-16376pkix.pem -out ua1-16376-16376pkix.der -outform der
```
