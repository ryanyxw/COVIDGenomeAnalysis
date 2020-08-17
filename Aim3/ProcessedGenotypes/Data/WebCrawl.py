#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 11:00:54 2020

@author: ryanwang
"""

import urllib.request

#downloadPath = os.path.join(os.getcwd(), "Data")
#link = "http://evidence.personalgenomes.org/genome_download.php?download_genome_id=fe84b12418d4eb010cefd1bdfe3aa8caaa87bd49&download_nickname=Microbiome+report+for+PGP+kit+%232190+%22Caryll%22"
#urllib.request.urlretrieve(link, "demo2.tsv.bz2")



def reporthook(blocks_read, block_size, total_size):

    if not blocks_read:
        print ('Connection opened')
        return
    if total_size < 0:
        # Unknown size
        print ('Read %d blocks' % blocks_read)
        print("Unknown size")

def downloadFile(userName, downloadLink):
    urllib.request.urlretrieve(downloadLink, "TSVRaw/" + userName + ".tsv.bz2", reporthook = reporthook)
    print(userName + " is complete")

def run():
    in1 = open("UserLinkDownload.csv", "r")
    count = 1
    tempLine = in1.readline().strip().split(",")
    for i in range(102):
        tempLine = in1.readline().strip().split(",")
        count += 1
    #for i in range(2):
    while (tempLine != ['']):
        print(repr(count) + "-------------------------")
        downloadFile(tempLine[0], tempLine[1])
        tempLine = in1.readline().strip().split(",")
        count += 1



run()