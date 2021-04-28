for x in range(26):
    s = '''
subnet 172.16.{number}.0 netmask 255.255.255.0 {{
  range 172.16.{number}.100 172.16.{number}.200;
  option routers 172.16.{number}.1;
  option domain-name-servers 82.211.192.246, 82.211.192.242;
}}
    '''.format(number=x+200)
    print(s)
