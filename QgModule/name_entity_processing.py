from parse import Parse
from nltk.tree import Tree as Tree


class NEP:
    def transform_pronoun(self, raw_data):
        
        word_list = raw_data.lower().split(" ")
        he_count = word_list.count("he")
        she_count = word_list.count("she")
        if he_count >= she_count:
            ne_gender = "he"
        else:
            ne_gender = "she"
        
        sentences = raw_data.split("\n")
        NE = sentences[0]
        first_name = NE.split(" ")[0]
        last_name = NE.split(" ")[1]


        NE = last_name
        sentences_nep = []
        if ne_gender == "he":
            print("\nCheck Point 1: Pronoun transformation")
            i=0
            for s in sentences:
                print(i," Before:",s)
                tmp = s.replace(" he ", " " + NE + " ")
                tmp = tmp.replace("He ", NE + " ")
                tmp = tmp.replace(" his ", " " + NE + "'s ")
                tmp = tmp.replace("His ", " " + NE + "'s ")
                tmp = tmp.replace(" him ", " " + NE + " ")
                print(i," After:",tmp)
                sentences_nep.append(tmp)
                i+=1
        else:
            print("\nCheck Point 1: Pronoun transformation")
            i=0
            for s in sentences:
                print(i," Before:",s)
                tmp = s.replace(" she ", " " + NE + " ")
                tmp = tmp.replace("She ", " " + NE + " ")
                tmp = tmp.replace(" She ", " " + NE + " ")
                tmp = tmp.replace(" her ", " " + NE + " ")
                tmp = tmp.replace("Her ", " " + NE + "'s ")
                print(i," After:",tmp)
                sentences_nep.append(tmp)
                i+=1
        print('\n')
        return ["\n".join(sentences_nep), [NE, first_name, last_name]]
    
        


# NEP = NEP()
# output = NEP.transform_pronoun()
# # print(test) 
# print("************************ \n\n\n\n *******************")
# print(output)

