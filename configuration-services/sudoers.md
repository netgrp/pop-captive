# sudo

Allow the server to run sudo for the command that open each and every captive portal interface. This example is with all the interfaces required for P. O. Pedersen Kollegiet when the Flask application runs as pop-captive on a server with the hostname pop-supermicro.

Append this to the this file: /etc/sudoers

    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft add element captive open_interfaces { kitchen_a }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft add element captive open_interfaces { kitchen_b }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft add element captive open_interfaces { kitchen_c }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft add element captive open_interfaces { kitchen_d }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft add element captive open_interfaces { kitchen_e }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft add element captive open_interfaces { kitchen_f }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft add element captive open_interfaces { kitchen_g }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft add element captive open_interfaces { kitchen_h }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft add element captive open_interfaces { kitchen_i }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft add element captive open_interfaces { kitchen_j }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft add element captive open_interfaces { kitchen_k }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft add element captive open_interfaces { kitchen_l }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft add element captive open_interfaces { kitchen_m }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft add element captive open_interfaces { kitchen_n }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft add element captive open_interfaces { kitchen_o }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft add element captive open_interfaces { kitchen_p }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft add element captive open_interfaces { kitchen_q }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft add element captive open_interfaces { kitchen_r }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft add element captive open_interfaces { kitchen_s }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft add element captive open_interfaces { kitchen_t }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft add element captive open_interfaces { kitchen_u }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft add element captive open_interfaces { kitchen_v }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft add element captive open_interfaces { kitchen_x }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft add element captive open_interfaces { kitchen_y }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft add element captive open_interfaces { falladen }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft add element captive open_interfaces { multiroom }


    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft -j list set ip captive open_interfaces


    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft delete element captive open_interfaces { kitchen_a }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft delete element captive open_interfaces { kitchen_b }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft delete element captive open_interfaces { kitchen_c }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft delete element captive open_interfaces { kitchen_d }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft delete element captive open_interfaces { kitchen_e }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft delete element captive open_interfaces { kitchen_f }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft delete element captive open_interfaces { kitchen_g }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft delete element captive open_interfaces { kitchen_h }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft delete element captive open_interfaces { kitchen_i }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft delete element captive open_interfaces { kitchen_j }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft delete element captive open_interfaces { kitchen_k }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft delete element captive open_interfaces { kitchen_l }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft delete element captive open_interfaces { kitchen_m }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft delete element captive open_interfaces { kitchen_n }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft delete element captive open_interfaces { kitchen_o }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft delete element captive open_interfaces { kitchen_p }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft delete element captive open_interfaces { kitchen_q }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft delete element captive open_interfaces { kitchen_r }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft delete element captive open_interfaces { kitchen_s }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft delete element captive open_interfaces { kitchen_t }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft delete element captive open_interfaces { kitchen_u }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft delete element captive open_interfaces { kitchen_v }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft delete element captive open_interfaces { kitchen_x }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft delete element captive open_interfaces { kitchen_y }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft delete element captive open_interfaces { falladen }
    pop-captive pop-supermicro = (root) NOPASSWD: /usr/sbin/nft delete element captive open_interfaces { multiroom }
