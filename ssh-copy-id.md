

ssh-copy-id.expect

```bash
#!/usr/bin/expect -f
spawn ssh-copy-id $argv
expect "password:"
send "YOUR_PASSWORD\n"
expect eof
```

then copy id_rsa.pub without interactive prompt

```bash
chmod +x ssh-copy-id.expect
./ssh-copy-id.expect root@your_ip
```