#!/usr/bin/expect -f
set USERNAME "cisco"
set PASSWORD "cisco123!"
set ENABLEPSW "enable-password"
set HOST "xx.xx.xx.xx"
spawn ssh -o StrictHostKeyChecking=no $USERNAME@$HOST
expect "Password: "
send "$PASSWORD\n"

expect "CSR1kv#"
send "show ip int br\n\n"

expect "CSR1kv#"
send "\n"
