"""
Verison 0.1
1. Create array of channels 
2. Export to files with names 
3. Create a new playlist from exported files.

1. Creating  a channel's list file: 
python3 shrinker.py -i playlist02052023.m3u8 -c cl1
playlist02052023.m3u8 - input playlist
cl1 - a channel list file

2. Generate playlist based on  a channel lsit file :

 

"""
import argparse
import json


class Libm3u8():

    def __init__(self) -> None:
        self.playlistfile="playlist.m3u8"
        self.channel_list=[]
        self.channel_list_str=[]
        self.dic_channel_list={}
        self.output_playlist=""
        self.file_channel_list=""

    # Gets all names of the  directory (self.directory ) and append to list (self.dir_list)
    def GetChannelLists(self):
         channel={"info":"","group":"","url":""}
         channel_name=""
         with open(self.playlistfile) as f:
              for cur_string in f:
                   if "EXTM3U" in cur_string:
                        pass
                   elif "EXTINF" in cur_string:
                        channel["info"]=cur_string.rstrip()
                        channel_name=cur_string.rstrip().split(",")[-1]
                   elif "EXTGRP" in cur_string:
                        channel["group"]=cur_string.rstrip()
                   elif "http" in cur_string:
                        channel["url"]=cur_string.rstrip()
                        self.channel_list.append(channel)
                        self.dic_channel_list[channel_name]=channel
                        channel={"info":"","group":"","url":""}
                        channel_name=""
    
    def PrintChannelsList(self):
        """
         for d in  self.channel_list:
            info1=d["info"] 
            group1=d["group"]
            print(f"INFO { info1 }, GROUP { group1 }")
        """
        print(self.channel_list_str)
        print("--------------------------------------\n")
        print(self.dic_channel_list)

    def GenerateChannelListStr(self):
         self.channel_list_str=[]
         
         """
         for d in  self.channel_list:
            info1=d["info"] 
            group1=d["group"]
            self.channel_list_str.append(f"INFO { info1 }, GROUP { group1 }\n")
         """  
         for d in  self.dic_channel_list:
            info1=d 
            group1=self.dic_channel_list[d]["group"]
            self.channel_list_str.append(f"{ info1 }, GROUP { group1 }\n")

    def PrintToFile(self,outfile):
         with open(outfile,"w",encoding="utf-8") as f:
              f.writelines(self.channel_list_str)
        
         with open("tmp.json","w",encoding="utf-8") as jf:
              json_dump_str=json.dumps(self.dic_channel_list,indent=4)
              jf.write(json_dump_str)
         

    def GeneratePlaylist(self):
         with open("tmp.json") as jsonfile:
              self.dic_channel_list=json.load(jsonfile) 

         with open(self.file_channel_list) as ch_list:
              for channel_str in ch_list:
                   channel_name=channel_str.split(",")[0] 
                   self.channel_list_str.append(channel_name) 

        
         print(self.channel_list_str)
         with open(self.output_playlist,"w",encoding="utf-8") as f:
              f.write('#EXTM3U\n')
              
              #for cname in self.dic_channel_list:
              for cname in self.channel_list_str:
                      
                f.write(f"{ self.dic_channel_list[cname]['info'] }\n")
                f.write(f"{ self.dic_channel_list[cname]['group'] }\n")
                f.write(f"{ self.dic_channel_list[cname]['url'] }\n")
                   #f.write(c_name["info"]+"\n")
                   #f.write(c_name["group"]+"\n")
                   #f.write(c_name["url"]+"\n")
                 
                   
         

def mainf():
     
    p=argparse.ArgumentParser()
 #  p.add_option('--addFromJsonToOldVision','-o', action="store_true", dest="addOldVision"  )
    p.add_argument('--listchannels','-l', action="store", dest="filelistchannel",help=" A List of channels")
    p.add_argument('--inputplaylists','-i', action="store", dest="inputplaylist",help=" A file with playlist")
    p.add_argument('--outlistchannels','-c', action="store", dest="outlistchannels",help=" A file with list channels")
    p.add_argument('--outputplaylist','-p', action="store", dest="outputplaylist",help=" A output playlist")

    
                   

    
    
    options=p.parse_args()

    

    
    if options.inputplaylist is not None:
         p=Libm3u8()
         p.playlistfile=options.inputplaylist
         p.GetChannelLists()
         p.GenerateChannelListStr()
         p.PrintChannelsList()
         p.PrintToFile(options.outlistchannels)
    
    if options.outputplaylist is not None:
         p=Libm3u8()
         p.file_channel_list=options.outlistchannels
         p.output_playlist=options.outputplaylist
         p.GeneratePlaylist()
    
    '''  
    if options.file is not None:
         b.file=options.file
    
    if options.maskfile is not None:
        if options.dir is not None:
            b.maskfile=options.maskfile
            b.GettingDirlist()
    '''
    # print("0000000000000000000000000000")
    # print(b.dir_list)
    
        
        
     
    """
    logging.basicConfig(filename="log.log")
    logging.basicConfig(format='%(asctime)s %(message)s')
   """

if __name__=="__main__":
        mainf()


