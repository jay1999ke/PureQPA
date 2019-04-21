from QgModule.bin_questions import BinQuestion
from QgModule.binary import Binary
from QgModule.wh_question import WH
from QgModule.tokenizeScript import Tokenise

class Ask:

    def main(self,text,parser):
        WH_ques = WH()
        Tokenize = Tokenise()
        Binary_ques = Binary()
        Bin_Question = BinQuestion()
        k=100

        print("\n\n\n\n")
        binary_questions = []
        print("Question generation\n","Check Point 0: Initiation")
        T = Tokenize.main(k=k,article=text)
        sentences_top_k = T[0]
        NE = T[1]
        questions = []
        try:
            for si in sentences_top_k:
                print("	*** org  : ", si)
                # print(" *** original sentence: ", si)
                bin_attempt = Binary_ques.main(si,parser)
                wh_attempt = WH_ques.main(bin_attempt, si, NE,parser)
                if bin_attempt:
                    print("	*** bin : ", bin_attempt)
                    questions.append(bin_attempt)
                if wh_attempt:
                    questions.append(wh_attempt)
                print("\n")
            print("\n\n\n\n")
        except:
            pass
        return questions
        
        # for q in questions:
        #     print q


