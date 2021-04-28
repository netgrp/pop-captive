# How to build the nftables setup with commands only

Create the table for the captive portal, and add the different chains we will need. Please not the policy drop for the forward chain.
<code>
nft add table captive
nft 'add chain captive prerouting { type nat hook prerouting priority -100; }'
nft 'add chain captive forward { type filter hook forward priority 0; policy drop; }'
nft 'add chain captive postrouting { type nat hook postrouting priority 100; }'
</code>


This is used to create an map between the captive portal interface and the public ip for that interface. Here with two kitchens as an example
<code>
nft 'add map captive interface_to_ip { type ifname: ipv4_addr; }'
nft 'add element captive interface_to_ip { "kitchen_a" : 82.211.200.200, "kitchen_b" : 82.211.200.201 }'
nft 'add rule ip captive postrouting snat to iifname map @interface_to_ip'
</code>


Reverse Path filter - https://wiki.nftables.org/wiki-nftables/index.php/Matching_routing_information
<code>
nft 'add rule ip captive prerouting fib saddr . iif oif eq 0 drop'
</code>


Captive portal for interfaces that are not open. This is like DNAT, but instead of having to define a targer IP that may change it will redirect to the primary IP for the interface. The result is the same as with DNAT but simpler. Only port 80 because you should not make DNAT on port 443 (certifikat will not match and you gain nothing).
<code>
nft 'add rule ip captive prerouting meta iifname != @open_interfaces tcp dport 80 redirect to :80'
</code>


Set to define open networks by interface. This has a build in timeout so that it expire automatically after 8 hours no-matter what. This means the web appliacation can be stateless and nftables can take care of one more thing
<code>
nft 'add set ip captive open_interfaces { type ifname; timeout 8h; }'
</code>


Set of allowed DNS servers. No matter if the network is closed or open there must be DNS servers. The captive portal will not be triggered if there is not DNS. But if we allow any IP on port 53 one could bypass the captive portal with that port. Therefore we only allow some approved DNS servers. It seems like a great choice to use K-Net DNS servers. They are defined as a set to make rule definition simpler
<code>
nft 'add set ip captive dns_servers { type ipv4_addr; }'
nft 'add element captive dns_servers { 82.211.192.246, 82.211.192.242 }'
</code>


Allow DNS for the set of allowed DNS servers no matter if the network/interface is open or closed. Both sending and receiving.
<code>
nft 'add rule ip captive forward ip daddr @dns_servers udp dport 53 accept'
nft 'add rule ip captive forward ip daddr @dns_servers tcp dport 53 accept'
nft 'add rule ip captive forward ip saddr @dns_servers udp sport 53 accept'
nft 'add rule ip captive forward ip saddr @dns_servers tcp sport 53 accept'
</code>


If the network/interface is closed we rewrite the DNS request for any IP to one of the K-Net DNS servers. That means if they dont respect the DNS servers offered via DHCP and they use Google DNS or CloudFlare DNS anyways the requests will be redirected via DNAT. The result is that any IP has a DNS response when the network interface is closed. DNS works as normal when the internet is open on a network/interface.
<code>
nft 'add rule ip captive prerouting meta iifname != @open_interfaces udp dport 53 dnat to 82.211.192.246'
nft 'add rule ip captive prerouting meta iifname != @open_interfaces tcp dport 53 dnat to 82.211.192.246'
</code>


This is the main bread of the captive portal. The policy for the forward table is by default to deny any traffic. Therefore to allow traffic when the interface/network is open we must allow that explicitly. This takes any open inteface as defined by the set of open interfaces and allow traffic going out and related trafic going in
<code>
nft 'add rule ip captive forward iifname @open_interfaces accept'
nft 'add rule ip captive forward oifname @open_interfaces ct state related,established accept'
</code>


Here is an example of how to open one interface kitchen_a for 8 hours (because the set has a timeout of 8 hours)
<code>
nft 'add element captive open_interfaces { kitchen_a }'
</code>
