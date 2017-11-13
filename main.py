from TextToPOS import TextToPOS
from transcribe import transcribe_gcs
def main():
    base_str="gs://saas-devel/test/segment"
    uris=[]
    for i in range (1,12):
        uris.append("gs://saas-devel/test/segment{0}.flac".format(i))
    print (uris)
    
    nlp = TextToPOS.load_en_large()
    for uri in uris:
        text = transcribe_gcs(uri)
        result = TextToPOS.get_filter_text(text, nlp)
        print(uri," will have: \n",result)
       
if __name__=='__main__':
    main()




