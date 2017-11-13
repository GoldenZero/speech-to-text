from TextToPOS import TextToPOS
from transcribe import transcribe_gcs
import os

def main():
    base_str="gs://saas-devel/test/segment"
    uris=[]
    for i in range (1,22):
        uris.append("gs://saas-devel/test/segment{0}.flac".format(i))
    print (uris)
    #for file_names in os.listdir(./data/):
    #    print(file_names)
    t2p = TextToPOS()
    nlp = TextToPOS.load_en_large()
    for uri in uris:
        text = transcribe_gcs(uri)
        result = t2p.get_filter_str(text, nlp)
        print(uri," will have: \n",result)
       
if __name__=='__main__':
    main()




