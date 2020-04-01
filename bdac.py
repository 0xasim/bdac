#!/usr/bin/env python3
import socket
import sys
import argparse
import subprocess as sp

parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f', help="Path to file containing domains")
parser.add_argument('--domains', '-d', help="List of domains", nargs='+')
parser.add_argument('--socket', '-s', help="Use socket method for checking availability. Note: It return available if it fails to resolve domain names to their namesevers and unavailable if domain resolves (It won't show grabbed domains that are available)", action="store_true")
parser.add_argument('--whois', '-w', help="Use whois method for checking availability. Note: There are limited tries an IP can have (No official number but some estimate about 1000/day)", action="store_true")
args = parser.parse_args()
argsDict= vars(args)

#help printing
if len(sys.argv)==1:
	parser.print_help()
	sys.exit(0)

def parseFile(filepath):
	domains = []
	try:
		file = open(filepath, "r")
		readfile = file.readlines()
	except FileNotFoundError:
		print("File not found")
		#raise FileNotFoundError
		sys.exit(0)
	
	for each in readfile:
		domains.append(each.rstrip('\n'))
	return domains

def getDomains(argsDict):
	#if file is proided as argument
	if argsDict["file"]:
		domains = parseFile(argsDict["file"])

	#if domains are proided as argument
	elif argsDict["domains"]:
		domains = argsDict["domains"]

	return domains

def usingSocket(domains):
	print("Using Socket:\n")
	for each in domains:
		try:
			socket.getaddrinfo(each,None)
			print('\tNot available: {domain}'.format(domain=each))

		#not working
		except socket.timeout:
			print("connection timeout")
		except socket.gaierror:
			print('\tAvailable: {domain}:'.format(domain=each))
		except:
			print("Some other error Occured in socket")

def usingWhois(domains):
	print("Using Socket:\n")
	for each in domains:
		try:
			sp.check_output('whois %s'%each, shell=True)
			print('\tNot available: {domain}'.format(domain=each))
		except sp.CalledProcessError:
			print('\tAvailable: {domain}'.format(domain=each))
		except:
			print("Some error Occured in whois")

def main():
	domains = getDomains(argsDict)
	if argsDict["socket"]:
		usingSocket(domains)

	if argsDict["whois"]:
		usingWhois(domains)

if __name__ == "__main__":
	main()
