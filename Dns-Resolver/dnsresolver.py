import socket

class DnsResolver:
    def main(self, host):
        try:
            addr = socket.gethostbyaddr(host)
            print("Target:",host)
            print("Host:", addr[0])
        except Exception as e:
            print("Error:", e)

        try:
            getaddr = socket.gethostbyname_ex(host)
            print("Ip Address",  (getaddr[-1]))
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    host = input("Enter a Hostname or IP Address: ")
    resolver = DnsResolver()
    resolver.main(host)
