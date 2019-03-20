#include <iostream>
#include <SFML/Network.hpp>
#include <string>

static bool port_is_open(const std::string& address, int port)
{
        return (sf::TcpSocket().connect(address, port) == sf::Socket::Done);
}


int main()
{
        std::string address;
        int port;
        // Get the address.
        std::cout << "Address: " << std::flush;
        std::getline(std::cin, address);
        // Scan!
        for(int i=0;i<65535;i++){
                std::cout << "Scanning " << address << "...\n" << "Port " << i << " : ";
                if (port_is_open(address, i))
                        std::cout << "OPEN" << std::endl;
                else
                        std::cout << "CLOSED" << std::endl;
        }
        return 0;
}
